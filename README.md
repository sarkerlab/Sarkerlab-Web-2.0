# Sarker Lab Website

Research website for the [Sarker Lab](https://sarkerlab.org) at Emory University's Department of Biomedical Informatics. Built with [Jekyll 4.3.3](https://jekyllrb.com/), derived from the [Greene Lab website template](https://github.com/greenelab/lab-website-template).

## Hosting

The site is hosted on **Netlify**, which automatically rebuilds on every push to `main`. The domain `sarkerlab.org` is managed through WordPress (domain provider) and mapped to the Netlify deployment.

## Local Development

### Prerequisites

Install Ruby and Jekyll:

```bash
brew install ruby        # macOS
gem install bundler jekyll
```

### Install & Run

```bash
bundle install                  # install dependencies
bundle exec jekyll serve        # start dev server at http://127.0.0.1:4000/
```

There is no test suite. Verify changes visually via the local dev server before pushing.

## Directory Structure

```
├── _data/                  # YAML data files (citations, events, media, dashboards, types)
├── _members/               # Team member profiles (one .md per person)
├── _posts/projects/        # Research project pages
├── _includes/              # Reusable HTML partials (rarely changed)
├── _layouts/               # Page templates (rarely changed)
├── _styles/                # SCSS stylesheets
├── _scripts/               # Client-side JavaScript
├── _plugins/               # Custom Ruby filters (do not modify)
├── _cite/                  # Citation automation script
├── dbsubpages/             # Dashboard sub-pages
└── images/                 # All site images
    ├── team/
    ├── research/
    ├── events/
    └── dashboard/
```

## Updating Content

Most updates involve editing YAML or Markdown files, not templates.

### Publications

Publications are stored in `_data/citations.yaml`. Each entry follows this format:

```yaml
- id: 'unique-identifier-or-doi'
  title: 'Paper Title'
  authors:
    - Author One
    - Author Two
  description: 'A One, A Two. Paper Title. Journal Name. Year.'
  date: 'Month YYYY'
  link: https://example.com/paper
  tags:
    - Social Media
    - Opioids
```

Field details:
- **id** — unique identifier (DOI preferred, or paper title)
- **title** — full paper title
- **authors** — list of authors, one per line
- **description** — Vancouver-format citation string
- **date** — publication date as "Month YYYY" (e.g., "March 2023")
- **link** — URL to the paper
- **tags** — list of topic tags (used for filtering on the publications page)

#### Automated Citation Updates

The script `_cite/cite.py` fetches publications from [Semantic Scholar](https://www.semanticscholar.org/) and merges them into `citations.yaml`. It preserves manually edited fields (tags, description, links) for existing entries and only adds new papers.

Run manually:

```bash
pip install -r _cite/requirements.txt
python _cite/cite.py                    # fetch from API
python _cite/cite.py --load-cache       # use cached data (offline)
python _cite/cite.py --save-cache       # save fetched data to cache
python _cite/cite.py --proxy            # use free proxies (for CI)
```

A GitHub Actions workflow (`update-citations.yaml`) runs this weekly and opens a PR with any new publications.

### Team Members

Create or edit Markdown files in `_members/`. Each file generates its own page at `/members/<filename>`.

```yaml
---
name: Full Name
image: images/team/photo.jpg
role: member          # member, collaborator, or alumni
description: Ph.D. Student
links:
  email: user@email.com
  twitter: username
  google-scholar: scholar-id
  github: username
---

Optional bio text here.
```

- **role** — determines which section the member appears in (`member`, `collaborator`, or `alumni`)
- **links** — use usernames only, not full URLs. See `_data/types.yaml` for available link types and their icons.

### Research Projects

Create Markdown files in `_posts/projects/`. Filenames **must** follow the format `YYYY-MM-DD-title.md`.

```yaml
---
title: Project Title
image: images/research/project-image.png
tags:
  - tag1
  - tag2
---

Project description here.
```

### Events

Add entries to `_data/events.yaml`. Event photos go in `images/events/`.

### Media Coverage

Add entries to `_data/media.yaml`:

```yaml
- title: Article Title
  subtitle: Publisher Name
  group: featured       # optional, shows in featured section
  image: images/path.jpg
  link: https://article-url.com
  description: Short description
```

### Dashboards

1. Create a `.md` file in `dbsubpages/` with `layout: dashboardsubpage`
2. Add the entry to `_data/dashboards.yaml`
3. Add to the dropdown menu in `_includes/dashboarddropdown.html`

## Tags

The publications page has a tag filter menu that lets visitors filter papers by topic. Tags are defined per-publication in `citations.yaml`. Current tags include: Social Media, Opioids, Pharmacovigilance, Machine Learning, Evidence-Based Medicine, Clinical Care, and others.

When adding new publications, assign relevant tags from the existing set. Create new tags only when no existing tag fits.

## CI/CD

| Workflow | Trigger | Purpose |
|---|---|---|
| `update-citations.yaml` | Weekly (Monday) | Fetches new publications, opens PR |
| `build-site.yaml` | Push to main | Builds the Jekyll site |
| `build-preview.yaml` | Pull request | Builds preview for PR review |
| `on-schedule.yaml` | Weekly | Orchestrates scheduled tasks |

Netlify deploys automatically from `main` on every push.

## Troubleshooting

**Site not updating after push?**
1. Clear browser cache and reload
2. Check the Actions tab on GitHub for build errors
3. Verify Netlify and WordPress services are running

**Ruby installation issues on macOS?**
macOS restricts modifications to the system Ruby. Use a version manager like `rbenv` or install via Homebrew. See [this guide](https://www.moncefbelyamani.com/how-to-install-xcode-homebrew-git-rvm-ruby-on-mac/) for a full walkthrough.

**Citation script blocked by rate limiting?**
Use `--load-cache` to work with previously cached data, or `--save-cache` after a successful fetch to store results for later use.
