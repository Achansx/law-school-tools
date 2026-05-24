---
id: appendix-F
title: "Technical Setup"
status: drafted
words: 791
target_min: 500
target_max: 800
last_phase: harvest-appendix
source_files:
  - "<vault>/.site/build.py"
  - "<vault>/.site/dist/netlify.toml"
  - "<vault>/.site/dist/index.html"
  - "<vault>/DEPLOY.md"
  - "<vault>/RUNBOOK.md (Deploy phase section)"
---

# Appendix F: Technical Setup

The `.site/` pipeline files (`build.py`, the `dist/` shell, `netlify.toml`, `DEPLOY.md`) were not pushed to this repository checkout, which holds only `Article/` and `Article-Workplan.md`. This appendix is reconstructed from the verified Section VIII, IX, III, and VI evidence cards that quote those files directly (per the article’s own L-055).

## F.1 Component stack

| Layer | Tool | Role |
|-------|------|------|
| Authoring | Obsidian (free) | Markdown editor over the vault |
| Version control | Git | Vault tracked at github.com/Achansx/law-school-tools |
| Build | `.site/build.py` (~700 lines Python, `markdown-it`) | Renders the corpus to JSON |
| Static shell | `index.html`, `app.js`, `style.css` (hand-written) | Client-side single-page app |
| Deploy | Netlify CLI direct upload (`--no-build`) | Zero Netlify build minutes |
| Hosting | Netlify free tier | Serves constitutionallaw.netlify.app |
| Analytics | PostHog (free tier) | Privacy-respecting usage counts |
| Quote verification | Midpage MCP | `findInOpinion` / `analyzeOpinion` |

No LLM sits in the request path; the model runs only at build time.

## F.2 Vault layout

The build reads three content folders; the maintenance rotation and publication pipeline live beside them.

- `Cases/`: one structured brief per opinion (roughly 30-field schema).
- `Topics/`: doctrinal synthesis pages.
- `Lectures/`: lecture summaries that preserve the professor’s framing.
- `Source Materials/`: original decks and PDFs, served as downloads.
- `Templates/`: frontmatter schemas for each content type.
- `.site/`: `build.py`, the `dist/` shell, and the deploy scripts.
- `rubric/`, `RUNBOOK.md`, `PROJECT_PRIMER.md`, `LESSONS.md`, `CHANGELOG.md`: the maintenance harness.

## F.3 Build and deploy pipeline

1. `build.py` walks `Cases/`, `Topics/`, and `Lectures/`, parses each page’s frontmatter, renders the body with `markdown-it`, and resolves `[[wiki-link]]` syntax into `#/p/<kind>/<slug>` hash routes.
2. It extracts a holding-bar and citation-metadata block per case and writes three JSON artifacts to `.site/dist/`: `pages.json` (corpus plus rendered HTML), `manifest.json` (counts and nav), and `search.json` (text index).
3. It copies `Source Materials/` into `dist/source/` and renders each `[[Source Materials/...]]` link as an `<a class="source-download">` element, so a reader can open the original behind any brief.
4. The hand-written shell loads the JSON at runtime: hash-route nav (`#/cases`, `#/topics`, `#/lectures`, `#/recent`, `#/about`), a ⌘K search palette, and a theme toggle. PostHog is configured with `disable_session_recording: true`, `respect_dnt: true`, and an `app: 'con-law-wiki'` tag on every event.
5. Deploy is a direct upload to Netlify (the CLI `--no-build` path or the `fast_deploy.py` uploader); neither consumes build minutes, the Netlify MCP fallback does. The access token is a gitignored local file.
6. Post-deploy verification compares the live `manifest.json` counts against the build, GETs a deterministic sample of five case briefs and three topics, confirms the live `search.json` surfaces “Marbury” for the query “judicial review,” and HEADs five `Source Materials` files for HTTP 200.

Deployed `dist/netlify.toml`, reproduced verbatim:

```toml
[build]
  publish = "."
  command = ""

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[build.processing]
  skip_processing = true
```

The empty `command` and `skip_processing` mean the uploaded artifact is exactly what is served; the redirect supports hash-route navigation.

## F.4 Quotation verification protocol

Every Key Quotation is confirmed against the indexed opinion at Midpage, not the professor’s modernized PDF, before it enters the vault: Ingest requires one Midpage-verified pin-cited quotation per new brief, and Enrich adds two or three more. Each pull-quote on the deployed page links to its Midpage line anchor (`https://app.midpage.ai/document/<slug>-<id>?utm_source=mcp&lines=<n>`) so a reader lands on the cited line. The reproducible step is the switch from keyword search to Midpage `findInOpinion` / `analyzeOpinion` against the indexed text; the Prize Cases / Grier near-miss that motivates it is narrated in Section VII.

## F.5 Cost of reproduction

Required: Obsidian (free), Git, a static host (Netlify’s free tier suffices), a paid Claude API or Claude Code subscription for the rotation, and a Midpage account for quote verification. Optional: PostHog (free tier) and a custom domain.

On the preferred path the deploy consumes zero Netlify build minutes and runs roughly twenty to forty seconds end-to-end (about sixteen seconds of build, eight of upload on a 205-page corpus, and ten to fifteen for the post-deploy check). The free-tier ceiling is bandwidth and file count, not build throughput; when credits exhaust, deploys are blocked (HTTP 403) until a human restores them.

## F.6 Forking notes

The vault is git-tracked at github.com/Achansx/law-school-tools. To adapt it: clone, edit `PROJECT_PRIMER.md` for the new course, adapt the `Templates/` schemas and `rubric/` files, then start ingesting. `Templates/` and `rubric/` are the most reusable artifacts.

## Intentionally excluded

Not reproduced here: the full source of `app.js`, `style.css`, and the deploy scripts; the prompt and rubric text (Appendices B and D); and figures of the interface (Section III).

Cross-reference: this appendix is referenced by Section VIII (Vault to Website) and Section III (Case Study).
