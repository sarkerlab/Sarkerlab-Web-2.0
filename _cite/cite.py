"""
Fetch publications from Google Scholar and merge into _data/citations.yaml.

Usage:
    python _cite/cite.py           # run without proxy (local dev)
    python _cite/cite.py --proxy   # run with free proxy (CI)

Fetches all publications for the configured Google Scholar author ID,
converts them to the site's citation YAML schema, and merges with
existing entries (preserving manual edits like tags).
"""

import json
import re
import signal
import string
import time
from functools import partial
from pathlib import Path

# Force unbuffered output so CI and background runs show progress
print = partial(print, flush=True)

import yaml
from scholarly import scholarly, ProxyGenerator
from Levenshtein import ratio as levenshtein_ratio

# Google Scholar author ID for Dr. Abeed Sarker
SCHOLAR_ID = "ShFx9OAAAAAJ"

# Paths relative to repo root
REPO_ROOT = Path(__file__).resolve().parent.parent
CITATIONS_PATH = REPO_ROOT / "_data" / "citations.yaml"

# Default path for caching fetched publications
CACHE_PATH = REPO_ROOT / "_cite" / "scholar_cache.json"

# Title similarity threshold for deduplication (0.0 to 1.0)
SIMILARITY_THRESHOLD = 0.90

# Delay between individual publication fill requests (seconds)
FILL_DELAY = 3

# Timeout for individual fill requests (seconds)
FILL_TIMEOUT = 30

# Number of consecutive failures before stopping fill attempts
MAX_CONSECUTIVE_FAILURES = 5

# Month names for date formatting
MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]


def normalize_title(title: str) -> str:
    """Normalize a title for comparison: lowercase, strip punctuation/whitespace."""
    title = title.lower()
    title = title.translate(str.maketrans("", "", string.punctuation))
    title = re.sub(r"\s+", " ", title).strip()
    return title


def find_matching_entry(title: str, existing: list[dict]) -> dict | None:
    """Find an existing citation that matches the given title."""
    norm = normalize_title(title)
    for entry in existing:
        existing_norm = normalize_title(entry.get("title", ""))
        if levenshtein_ratio(norm, existing_norm) >= SIMILARITY_THRESHOLD:
            return entry
    return None


def format_authors_vancouver(authors: list[str]) -> str:
    """Format author list in abbreviated Vancouver style: 'Sarker A, Klein AZ, ...'"""
    formatted = []
    for author in authors:
        parts = author.strip().split()
        if len(parts) >= 2:
            last = parts[-1]
            initials = "".join(p[0] for p in parts[:-1] if p)
            formatted.append(f"{last} {initials}")
        else:
            formatted.append(author.strip())
    return ", ".join(formatted)


def format_date(pub: dict) -> str:
    """Extract a 'Month YYYY' date string from a publication dict."""
    bib = pub.get("bib", {})

    # Try publication_date first (from Semantic Scholar cache: "YYYY-MM-DD")
    pub_date = bib.get("publication_date", "")
    if pub_date and "-" in pub_date:
        parts = pub_date.split("-")
        if len(parts) >= 2:
            try:
                year = int(parts[0])
                month_idx = int(parts[1]) - 1
                if 0 <= month_idx < 12:
                    return f"{MONTHS[month_idx]} {year}"
            except (ValueError, IndexError):
                pass

    year = bib.get("pub_year", "")
    if not year:
        return ""
    return f"January {year}"


def build_description_from_filled(pub: dict) -> str:
    """Build a Vancouver-style citation string from a filled publication."""
    bib = pub.get("bib", {})
    author_str = bib.get("author", "")
    if author_str:
        authors_raw = author_str.split(" and ")
        authors_fmt = format_authors_vancouver(authors_raw)
    else:
        authors_fmt = ""
    title = bib.get("title", "")
    venue = bib.get("venue", "") or bib.get("journal", "") or bib.get("booktitle", "")
    year = bib.get("pub_year", "")

    parts = []
    if authors_fmt:
        parts.append(authors_fmt + ".")
    if title:
        parts.append(title + ".")
    if venue:
        parts.append(venue + ".")
    if year:
        parts.append(year + ".")
    return " ".join(parts)


def build_description_from_unfilled(pub: dict) -> str:
    """Build a description from the unfilled citation string."""
    bib = pub.get("bib", {})
    title = bib.get("title", "")
    citation = bib.get("citation", "")
    if citation:
        return f"{title}. {citation}"
    return title


def get_publication_link(pub: dict) -> str:
    """Get the best available link for a publication."""
    bib = pub.get("bib", {})
    if bib.get("doi"):
        return f"https://doi.org/{bib['doi']}"
    if pub.get("pub_url"):
        return pub["pub_url"]
    if pub.get("eprint_url"):
        return pub["eprint_url"]
    # Build a Google Scholar link from author_pub_id as last resort
    author_pub_id = pub.get("author_pub_id", "")
    if author_pub_id:
        return f"https://scholar.google.com/citations?view_op=view_citation&hl=en&citation_for_view={author_pub_id}"
    return ""


def generate_id(pub: dict) -> str:
    """Generate a citation ID, preferring DOI."""
    bib = pub.get("bib", {})
    if bib.get("doi"):
        return bib["doi"]
    return bib.get("title", "Untitled")


def scholar_pub_to_citation(pub: dict, filled: bool = True) -> dict:
    """Convert a scholarly publication dict to our citation YAML schema."""
    bib = pub.get("bib", {})

    if filled and bib.get("author"):
        authors_raw = bib["author"].split(" and ")
        authors = [a.strip() for a in authors_raw if a.strip()]
        description = build_description_from_filled(pub)
    else:
        authors = ["Abeed Sarker"]  # at minimum, we know the profile author
        description = build_description_from_unfilled(pub)

    return {
        "id": generate_id(pub),
        "title": bib.get("title", ""),
        "authors": authors,
        "date": format_date(pub),
        "tags": [],
        "description": description,
        "link": get_publication_link(pub),
    }


def parse_date_for_sort(date_str: str) -> tuple[int, int]:
    """Parse 'Month YYYY' into (year, month) for sorting. Returns (0, 0) on failure."""
    if not date_str:
        return (0, 0)
    parts = date_str.strip().split()
    if len(parts) == 2:
        month_name, year_str = parts
        try:
            year = int(year_str)
        except ValueError:
            return (0, 0)
        month = MONTHS.index(month_name) + 1 if month_name in MONTHS else 1
        return (year, month)
    try:
        return (int(parts[0]), 1)
    except (ValueError, IndexError):
        return (0, 0)


def load_existing_citations() -> list[dict]:
    """Load existing citations from YAML file."""
    if not CITATIONS_PATH.exists():
        return []
    with open(CITATIONS_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data if isinstance(data, list) else []


def save_citations(citations: list[dict]) -> None:
    """Write citations to YAML file, sorted newest first."""
    citations.sort(key=lambda c: parse_date_for_sort(c.get("date", "")), reverse=True)

    with open(CITATIONS_PATH, "w", encoding="utf-8") as f:
        for i, entry in enumerate(citations):
            if i > 0:
                f.write("\n")
            f.write(f"- id: {_yaml_quote(entry.get('id', ''))}\n")
            f.write(f"  title: {_yaml_quote(entry.get('title', ''))}\n")
            f.write("  authors:\n")
            for author in entry.get("authors", []):
                f.write(f"  - {author}\n")
            f.write(f"  date: {_yaml_quote(entry.get('date', ''))}\n")
            if entry.get("tags"):
                f.write("  tags:\n")
                for tag in entry["tags"]:
                    f.write(f"  - {tag}\n")
            f.write(f"  description: {_yaml_quote(entry.get('description', ''))}\n")
            f.write(f"  link: {entry.get('link', '')}\n")


def _yaml_quote(value: str) -> str:
    """Quote a YAML string value with double quotes, escaping inner quotes."""
    if not value:
        return "''"
    escaped = value.replace('"', '\\"')
    return f'"{escaped}"'


def save_cache(publications: list[dict], path: Path = CACHE_PATH) -> None:
    """Save fetched publications to a JSON cache file."""
    # scholarly objects aren't directly JSON-serializable; extract relevant fields
    cache_data = []
    for pub in publications:
        entry = {
            "bib": dict(pub.get("bib", {})),
            "pub_url": pub.get("pub_url", ""),
            "eprint_url": pub.get("eprint_url", ""),
            "author_pub_id": pub.get("author_pub_id", ""),
            "num_citations": pub.get("num_citations", 0),
        }
        cache_data.append(entry)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cache_data, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(cache_data)} publications to cache: {path}")


def load_cache(path: Path = CACHE_PATH) -> list[dict]:
    """Load publications from a JSON cache file."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"Loaded {len(data)} publications from cache: {path}")
    return data


def fetch_scholar_publications(use_proxy: bool = False, save_to_cache: bool = False) -> list[dict]:
    """Fetch all publications from Google Scholar for the configured author."""
    print(f"Fetching publications for Google Scholar ID: {SCHOLAR_ID}")

    if use_proxy:
        try:
            pg = ProxyGenerator()
            success = pg.FreeProxies()
            if success:
                scholarly.use_proxy(pg)
                print("Using free proxy for Google Scholar requests")
        except Exception as e:
            print(f"Warning: Could not set up proxy ({e}), proceeding without proxy")
    else:
        print("Running without proxy (use --proxy flag to enable)")

    # Wrap entire fetch in a timeout — scholarly can hang when rate-limited
    old_handler = signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(120)  # 2 minute timeout
    try:
        print("Looking up author profile...")
        author = scholarly.search_author_id(SCHOLAR_ID)
        print("Fetching publication list from profile...")
        author = scholarly.fill(author, sections=["publications"])
    except _FillTimeout:
        print("ERROR: Timed out fetching author publications. Google Scholar may be "
              "rate-limiting. Try again later or use --proxy.")
        raise SystemExit(1)
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old_handler)

    publications = author.get("publications", [])
    print(f"Found {len(publications)} publications on Google Scholar")

    if save_to_cache:
        save_cache(publications)

    return publications


class _FillTimeout(Exception):
    pass


def _timeout_handler(signum, frame):
    raise _FillTimeout("Fill request timed out")


def _fill_with_timeout(pub, timeout=FILL_TIMEOUT):
    """Fill a publication with a timeout to avoid hanging on rate limits."""
    old_handler = signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(timeout)
    try:
        result = scholarly.fill(pub)
        return result
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old_handler)


def fill_new_publications(
    publications: list[dict], existing: list[dict]
) -> list[tuple[dict, bool]]:
    """
    For publications not already in existing citations, attempt to fill
    details from Google Scholar. Returns list of (pub, was_filled) tuples.
    Only fills publications that are NEW (not matched in existing).
    """
    results = []
    fill_count = 0
    skip_count = 0
    consecutive_failures = 0
    stop_filling = False

    for i, pub in enumerate(publications):
        bib = pub.get("bib", {})
        title = bib.get("title", "")
        if not title:
            continue

        match = find_matching_entry(title, existing)
        if match is not None:
            skip_count += 1
            continue

        fill_count += 1

        if stop_filling:
            # Rate limited — just use basic data for remaining pubs
            results.append((pub, False))
            continue

        try:
            filled = _fill_with_timeout(pub)
            results.append((filled, True))
            print(f"  [{fill_count}] Filled: {title[:70]}")
            consecutive_failures = 0
            time.sleep(FILL_DELAY)
        except Exception as e:
            print(f"  [{fill_count}] Fill failed ({e}), using basic data: {title[:70]}")
            results.append((pub, False))
            consecutive_failures += 1
            if consecutive_failures >= MAX_CONSECUTIVE_FAILURES:
                print(f"  ** {MAX_CONSECUTIVE_FAILURES} consecutive failures — "
                      f"skipping fills for remaining publications")
                stop_filling = True

    print(f"Skipped {skip_count} existing publications, "
          f"processed {fill_count} new ones")
    return results


def merge_citations(
    existing: list[dict], new_pubs: list[tuple[dict, bool]]
) -> list[dict]:
    """
    Merge new publications into existing citations.
    new_pubs is a list of (pub_dict, was_filled) tuples — only contains
    publications NOT already matched in existing.
    """
    merged = list(existing)
    added = 0

    for pub, was_filled in new_pubs:
        citation = scholar_pub_to_citation(pub, filled=was_filled)
        if not citation["title"]:
            continue

        # Double-check dedup (in case of near-duplicates within new pubs)
        match = find_matching_entry(citation["title"], merged)
        if match is None:
            merged.append(citation)
            added += 1
            print(f"  + Added: {citation['title'][:80]}")

    print(f"Merge complete: {added} new publications added, {len(existing)} existing preserved")
    return merged


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Update citations from Google Scholar")
    parser.add_argument(
        "--proxy", action="store_true",
        help="Use free proxies for Google Scholar requests (recommended for CI)",
    )
    parser.add_argument(
        "--no-fill", action="store_true",
        help="Skip filling individual publications (faster, uses basic metadata only)",
    )
    parser.add_argument(
        "--save-cache", action="store_true",
        help="Save fetched publications to a local JSON cache",
    )
    parser.add_argument(
        "--load-cache", action="store_true",
        help="Load publications from local JSON cache instead of fetching from Google Scholar",
    )
    args = parser.parse_args()

    print("=" * 60)
    print("Google Scholar Citation Updater")
    print("=" * 60)

    existing = load_existing_citations()
    print(f"Loaded {len(existing)} existing citations from {CITATIONS_PATH}")

    if args.load_cache:
        all_pubs = load_cache()
    else:
        all_pubs = fetch_scholar_publications(
            use_proxy=args.proxy, save_to_cache=args.save_cache
        )

    if args.no_fill or args.load_cache:
        # Skip individual fill requests; cache entries already have author data
        new_pubs = []
        for pub in all_pubs:
            bib = pub.get("bib", {})
            title = bib.get("title", "")
            has_authors = bool(bib.get("author"))
            if title and find_matching_entry(title, existing) is None:
                new_pubs.append((pub, has_authors))
        print(f"No-fill mode: {len(new_pubs)} new publications found")
    else:
        new_pubs = fill_new_publications(all_pubs, existing)

    merged = merge_citations(existing, new_pubs)

    save_citations(merged)
    print(f"Saved {len(merged)} total citations to {CITATIONS_PATH}")
    print("Done!")


if __name__ == "__main__":
    main()
