---
id: appendix-F
title: "Technical Setup"
status: drafted
words: 773
target_min: 500
target_max: 800
last_phase: harvest-appendix
source_files:
  - "<vault>/.site/build.py"
  - "<vault>/.site/dist/netlify.toml"
  - "<vault>/.site/dist/index.html"
  - "<vault>/DEPLOY.md"
  - "<vault>/RUNBOOK.md (Phase: Deploy)"
provenance_note: "Refiled verbatim from the in-repo .site/build.py, .site/dist/ shell, netlify.toml, DEPLOY.md, and the vault RUNBOOK Deploy section, which are now present in the checkout. Supersedes the run-121 reconstruction from evidence cards (per L-055)."
---

# Appendix F: Technical Setup

Built directly from the vault's `.site/build.py`, the hand-written `dist/` shell, `netlify.toml`, and `DEPLOY.md`.

## F.1 Component stack

| Layer | Tool | Role |
|-------|------|------|
| Authoring | Obsidian (free) | Markdown editor over the vault |
| Version control | Git | Vault tracked at github.com/Achansx/law-school-tools |
| Build | `.site/build.py` (~1,100 lines Python; `markdown-it-py`, `PyYAML`) | Renders the corpus to JSON |
| Static shell | `index.html`, `app.js`, `style.css`, `_headers`, `_redirects` (hand-written) | Client-side single-page app |
| Deploy | Netlify CLI direct upload (`--no-build`) | Zero Netlify build minutes |
| Hosting | Netlify free tier | Serves constitutionallaw.netlify.app |
| Feedback | Netlify Forms (`page-feedback`) | Reader notes routed to the rotation |
| Analytics | PostHog (free tier) | Privacy-respecting usage counts |
| Quote verification | Midpage MCP | `findInOpinion` / `analyzeOpinion` |

No LLM sits in the request path; the model runs only at build time.

## F.2 Vault layout

- `Cases/`: one structured brief per opinion (roughly 30-field schema).
- `Topics/`: doctrinal synthesis pages.
- `Lectures/`: lecture summaries that preserve the professor's framing.
- `Source Materials/`: original decks and PDFs, served as downloads.
- `Templates/`: frontmatter schemas for each content type.
- `.site/`: `build.py`, the `dist/` shell, and `deploy.sh`.
- `rubric/`, `RUNBOOK.md`, `PROJECT_PRIMER.md`, `LESSONS.md`, `CHANGELOG.md`: the maintenance harness.

## F.3 Build and deploy pipeline

1. `build.py` reads `VAULT_DIR` and `OUT_DIR` from the environment, walks `Cases/`, `Topics/`, and `Lectures/`, parses each page's frontmatter with `PyYAML`, renders the body with `markdown-it-py` (CommonMark, tables and strikethrough enabled), and resolves `[[wiki-link]]` syntax into `#/p/<kind>/<slug>` hash routes.
2. It writes five JSON artifacts to `dist/`: `pages.json` (corpus plus rendered HTML and plaintext), `manifest.json` (counts and nav), `search.json` (`{id, title, kind, area, doctrines, text}`), `recent.json`, and `build_errors.json` (pages whose frontmatter failed to parse, for the Lint phase).
3. It mirrors `Source Materials/` into `dist/source/` (cleared each build via `shutil.rmtree(ignore_errors=True)` to survive iCloud quarantine) and rewrites every `[[Source Materials/...]]` wikilink into an `<a class="source-download" ... download>` element.
4. The hand-written shell loads the JSON at runtime: hash-route nav (`#/`, `#/cases`, `#/topics`, `#/lectures`, `#/recent`, `#/about`), a ⌘K search palette, a pre-paint theme toggle (`localStorage` key `cl-theme`), and a `page-feedback` Netlify Form. PostHog is initialized with `disable_session_recording: true`, `respect_dnt: true`, `capture_pageview: false`, and an `app: 'con-law-wiki'` tag on every event; the write key is public and embedded.
5. Deploy is a direct upload via the Netlify CLI (`npx netlify-cli deploy --no-build --prod --dir . --site <id>`) using the gitignored PAT at `.site/.netlify-token`; this consumes no build minutes. The Netlify MCP (`netlify-deploy-services-updater`) is the fallback and does consume minutes; `deploy.sh` (exit 42 if the token is missing) is the last resort.
6. Post-deploy verification cross-checks the live `manifest.json` counts (`case`, `topic`, `lecture`, `total`) against the build, confirms the deploy record is `ready`, GETs a deterministic sample of five case briefs and three topics for their titles, confirms the live `search.json` surfaces "Marbury" for "judicial review," and HEADs five `Source Materials` files for HTTP 200 and the right `Content-Type`. The budget is ten to fifteen seconds.

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

Every Key Quotation is confirmed against the indexed opinion at Midpage, not the professor's modernized PDF, before it enters the vault. Each pull-quote on the deployed page links to its Midpage line anchor so a reader lands on the cited line. The reproducible step is the switch from keyword search to Midpage `findInOpinion` / `analyzeOpinion` against the indexed text; the Prize Cases / Grier near-miss that motivates it is narrated in Section VII.

## F.5 Cost of reproduction

Required: Obsidian (free), Git, a static host (Netlify's free tier suffices), a paid Claude API or Claude Code subscription for the rotation, and a Midpage account for quote verification. Optional: PostHog (free tier) and a custom domain. The preferred deploy path consumes zero Netlify build minutes; the free-tier ceiling is bandwidth and file count, not build throughput, and when credits exhaust, deploys are blocked (HTTP 403) until a human restores them.

## F.6 Forking notes

The vault is git-tracked at github.com/Achansx/law-school-tools. To adapt it: clone, edit `PROJECT_PRIMER.md` for the new course, adapt the `Templates/` schemas and `rubric/` files, then start ingesting. `Templates/` and `rubric/` are the most reusable artifacts.

## Intentionally excluded

Not reproduced here: the full source of `app.js` and `style.css`; the `deploy.sh` and `_headers`/`_redirects` contents; the prompt and rubric text (Appendices B and D); and figures of the interface (Section III).

Cross-reference: this appendix is referenced by Section VIII (Vault to Website) and Section III (Case Study).
