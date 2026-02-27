# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Sarker Lab research website (sarkerlab.org) — a Jekyll 4.3.3 static site for Emory University's Department of Biomedical Informatics. Derived from the [Greene Lab website template](https://github.com/greenelab/lab-website-template). Hosted on Netlify (not GitHub Pages), with DNS mapped via WordPress.

## Build & Development Commands

```bash
# Install dependencies
bundle install

# Run local dev server (http://127.0.0.1:4000/)
bundle exec jekyll serve

# Build static site
bundle exec jekyll build

# Docker alternative
./.docker/run.sh
```

There is no test suite — verify changes visually via the local dev server.

## Architecture

**Static site generator:** Jekyll with Liquid templates, SCSS styles, and YAML-driven content.

**Content is data-driven.** Most site updates involve editing YAML/Markdown files, not templates:

| Content Type | Data Location | Images |
|---|---|---|
| Publications | `_data/citations.yaml` | — |
| Team members | `_members/*.md` (one file per person) | `images/team/` |
| Research projects | `_posts/projects/YYYY-MM-DD-title.md` | `images/research/` |
| AI prompt showcase | `_data/prompts.yaml` + `_posts/prompts/YYYY-MM-DD-title.md` | — |
| Events/news | `_data/events.yaml` | `images/events/` |
| Media coverage | `_data/media.yaml` | — |
| Dashboards | `_data/dashboards.yaml` + `dbsubpages/*.md` | `images/dashboard/` |
| Role/icon definitions | `_data/types.yaml` | — |

**Template layers:**
- `_layouts/` — page templates (default, member, post, prompt, dashboardsubpage)
- `_includes/` — reusable HTML partials (citation, member, card, grid, footer, etc.)
- `_styles/` — SCSS stylesheets (sass_dir configured in `_config.yaml`)
- `_scripts/` — client-side JS (search, dark mode, anchors, drug lookup, citation modal)
- `_plugins/` — custom Ruby filters (array, hash, regex, file, misc)

**Collections:** `members` and `posts` both have `output: true` — each Markdown file auto-generates its own page.

## Content Editing Conventions

**Member files** (`_members/*.md`): YAML front matter with `name`, `image`, `role` (member/collaborator/alumni), `description`, and `links` (usernames only, not full URLs). See `_data/types.yaml` for available link types.

Available link types for `links:` in member files (from `_data/types.yaml`):
- Social/profile: `orcid`, `google-scholar`, `github`, `twitter`, `linkedin`, `facebook`, `instagram`, `youtube`
- Contact: `email`, `phone`, `address`, `website`, `link`

**Research posts** (`_posts/projects/`): Filenames must follow `YYYY-MM-DD-title.md` format. Front matter includes `title`, `image`, and `tags`.

**Prompt posts** (`_posts/prompts/`): Filenames must follow `YYYY-MM-DD-title.md` format. Uses `layout: prompt`. Entries in `_data/prompts.yaml` have `title`, `group` (e.g., "Information Extraction"), `link`, `paper` (URL), `description`, and `tags`.

**Citations** (`_data/citations.yaml`): Each entry needs `id` (unique), `title`, `authors` (list), `description` (Vancouver format), `date` ("Month YYYY"), and `link`. The automated `_cite/cite.py` script fetches from Google Scholar (author ID `ShFx9OAAAAAJ`), deduplicates by title using Levenshtein distance (90% threshold), and caches results in `scholar_cache.json`. Run via GitHub Actions weekly.

**Dashboard pages**: Create `.md` in `dbsubpages/` with `layout: dashboardsubpage`, add to `_data/dashboards.yaml`, and add to `_includes/dashboarddropdown.html`.

**Events** (`_data/events.yaml`): Fields are `title`, `date` (YYYY-MM-DD), `categories` (list, e.g., "academic"/"social"), `image` (filename in `images/events/`), and optional `description`.

## CI/CD

Five GitHub Actions workflows:
- `on-schedule.yaml` — orchestrator; runs weekly (Monday 00:00 UTC) calling `update-citations.yaml` then conditionally triggering a build
- `update-citations.yaml` — reusable; fetches citations, opens a PR or auto-commits
- `build-site.yaml` — builds Jekyll and commits output to main
- `build-preview.yaml` — builds preview deployments for PRs
- `on-pull-request.yml` — runs checks on PRs

Netlify deploys from the main branch on push.

## Key Configuration

- `_config.yaml` — Jekyll settings, collections, plugins, sass config
- `Gemfile` — Ruby dependencies (jekyll 4.3.3, jekyll-sass-converter 3.0.0, webrick)
- Jekyll plugins: jekyll-spaceship, jekyll-sitemap, jekyll-redirect-from, jekyll-feed, jekyll-last-modified-at, jekyll_picture_tag (responsive images for events)
- Frontend JS deps: chart.js (dashboards), moment.js

## Notes

- `_includes/` and `_layouts/` rarely need changes. The exception is `_includes/footer.html` where the copyright year should be updated annually.
- `_plugins/` and `_scripts/` should not be modified for routine content updates.
- The `Gemfile.lock` is excluded from builds (removed by CI before `jekyll build`).
- `drug_lookup.md` and `search.md` are root-level special-purpose pages backed by `_scripts/drug_lookup.js` and `_scripts/search.js` respectively.
