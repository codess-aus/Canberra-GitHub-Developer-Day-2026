# Canberra GitHub Developer Day 2026

A [MkDocs](https://www.mkdocs.org/) site (using the [Material](https://squidfunk.github.io/mkdocs-material/) theme) for the day, published on GitHub Pages:
<https://codess-aus.github.io/Canberra-GitHub-Developer-Day-2026/>

Each chapter is a section, each topic is a page, and every page opens with a hero image. The home page links to each chapter with a thumbnail and title. There is a light/dark switch, and the colour gradients are matched to each chapter's hero.

## Preview locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve          # http://127.0.0.1:8000/Canberra-GitHub-Developer-Day-2026/
mkdocs build --strict # what CI runs
```

## Add or edit content

Pages live in `docs/` and are listed in the `nav` of `mkdocs.yml`. Each page uses front matter to drive the hero and cards:

```yaml
---
title: Set up
chapter: 4                  # 0 = home, 1 to 6 = chapters (picks the gradient)
hero: Home Page Hero Image.png  # image, relative to docs/assets/
hero_alt: Describes the image for screen readers
thumb: thumbs/4-5-set-up.webp  # card thumbnail
summary: One line shown on the card
cards: topics               # optional: chapters (home) or topics (chapter page)
---
```

Put `<!-- cards -->` in the Markdown where the card grid should appear.

A chapter with only a landing page is listed in the nav as a plain page. Once it has topics, make it a section whose first entry is its `index.md`.

## Images

Chapters 2, 3, 5 and 6 use generated hero art. After adding or changing images in `docs/assets/`, regenerate the thumbnails and hero art:

```bash
pip install pillow
python scripts/build_images.py
```

## Deploy

The workflow in `.github/workflows/pages.yml` builds and deploys on every push to `main`. In the repository, set **Settings > Pages > Source** to **GitHub Actions** once.
