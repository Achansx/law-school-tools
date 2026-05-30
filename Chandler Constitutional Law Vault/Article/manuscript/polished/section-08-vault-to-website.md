---
id: "08"
title: "From Vault to Website"
status: needs_polish
target_words: 700
word_count: 736
last_phase: verify-provenance
draft_status: needs_polish
cite_status: needs_polish
polish_status: needs_polish
provenance_audited: true
provenance_score: 4.4
claims_total: 23
claims_mapped: 22
unsupported_claims:
  - claim_text: "VIII.A states a fixed-date corpus snapshot of 198 pages (92 case briefs, 27 doctrinal topic pages, 79 lecture summaries) captured in the same progress report that anchors Section IV, but neither the prose nor footnote [^1] states the progress-report date; the snapshot's as-of date is undetermined pending PI-004."
    paragraph: 1
    reason: evidence-gap
---

# VIII. From Vault to Website

## A. What the deployed site is

The vault is published at https://constitutionallaw.netlify.app, with a fixed-date corpus snapshot of 198 pages (92 case briefs, 27 doctrinal topic pages, and 79 lecture summaries) captured in the same progress report that anchors Section IV’s input-corpus inventory.[^1] The deployed site, not the local vault on disk, is the artifact a student or peer reviewer actually opens; the vault on disk is the upstream source that the build script reads. Section VIII opens by naming the URL and the snapshot, then walks the pipeline that produces what the CDN serves, so the IV-V-VIII trio triangulates on a single fact rather than restating page counts at every pass.[^2]

## B. The build pipeline: markdown to JSON to SPA shell

The build is one Python script, `.site/build.py`, supported by three hand-written shell files: `index.html`, `app.js`, and `style.css`.[^3] The script walks the three content folders (Cases, Topics, Lectures), parses each page’s YAML frontmatter, renders the markdown body with `markdown-it`, resolves Obsidian-style wiki-link syntax into in-app hash routes of the form `#/p/<kind>/<slug>`, extracts the structured holding-bar and citation-metadata block from each case page, and writes three JSON artifacts into `.site/dist/`: `pages.json` (full corpus with rendered HTML and search text), `manifest.json` (lightweight index for navigation and counts), and `search.json` (compact text index for the search palette).[^4] The runtime shell loads those artifacts client-side, defines a hash-route navigation that reaches every page through a stable URL, wires a ⌘K search palette to `search.json`, registers a Netlify `page-feedback` form stub at build time, and embeds PostHog analytics with session recording disabled and Do Not Track respected.[^5] The production surface is narrow enough that the author can reason about every step from markdown source to rendered page without a model in the request path, and the search palette is the visible artifact of that narrow surface.[^6]

## C. Deploy as a first-class rotation phase

Deployment is a Netlify CLI direct upload using a local personal access token, gitignored and never committed.[^7] The `netlify.toml` disables post-processing and registers a single SPA-style redirect, so the artifact uploaded is exactly the artifact served; a three-tier fallback chain (CLI direct upload preferred, Netlify MCP fallback, `.site/deploy.sh` shell wrapper as last resort) keeps deploys reproducible from a scheduled task without leaking credentials and, on the preferred path, without consuming Netlify build minutes.[^8] Deploy is a first-class rotation phase, with its own per-phase rubric, its own pending-issue lifecycle, and a cardinal rule that no vault failing Verify may be published; a stale live site is recoverable, a broken wiki in front of the professor is not.[^9] Post-deploy verification distinguishes a successful upload from a successful publication via four sub-checks against the production CDN: a manifest-count comparison, a deterministically sampled eight-page fetch, a search-sanity probe confirming the live `search.json` returns *Marbury* for the query “judicial review,” and a Source Materials HEAD sample; each failure mode opens a typed pending issue and blocks state advance.[^10]

## D. Auditable inputs and a closed feedback loop

The deployed site serves the professor’s original source materials behind direct download links the build emits whenever a page wiki-links to a file under `Source Materials/`, with `_headers` rules giving source files long-lived caching while the generated JSON artifacts stay on short TTLs.[^11] A reader can click from a brief to the original slide deck or annotated opinion it was built from; the auditable-input commitment pairs with the auditable-output commitment of a reviewed static page. Every run also begins with Step 0, which pulls submissions from the Netlify `page-feedback` form, triages each into the phase that can fix it (Lint for typos, Enrich for content gaps, Synthesize for new topics, Verify for disputed facts), and either fixes inline or logs a typed pending issue carrying the page identifier, title, submitter identity, verbatim comment, and Netlify submission identifier; the scope-selection step of the next-running phase prefers pages with open `professor-feedback` issues routed to that phase.[^12] The published site talks back to the vault, and the vault routes the talk-back through the same rotation that produced the page.[^13]

## E. Static site, not chatbot

Section VIII’s most load-bearing claim is the architectural one: the case study is a reviewed static site, not a chatbot.[^14] No LLM sits in the request path. The published page is a stable HTML and JSON artifact, written and verified by the rotation phases at publish time and served by the CDN without further model inference; risk lives in the build pipeline where Verify can catch it and the Deploy entry guard can hold it back, not in the response a student gets when opening a page. Section XII develops this contrast against contemporaneous chatbot architectures and the Magesh hallucination findings.[^15]

## Footnotes

[^1]: *See infra* App. A (Vault Architecture and File Layout) (deployed-site URL https://constitutionallaw.netlify.app and 198-page corpus snapshot of 92 case briefs, 27 doctrinal topic pages, and 79 lecture summaries as of the progress-report date).

[^2]: *See infra* fig. 3.9 (deployed site’s About page as the deployed shell’s self-description naming the rotation-built provenance; captured from the deployed site at https://constitutionallaw.netlify.app, May 26, 2026).

[^3]: *See infra* App. A (Vault Architecture and File Layout) (`.site/build.py` Python build script, approximately 700 lines, plus three hand-written static-shell files `.site/dist/index.html`, `.site/dist/app.js`, and `.site/dist/style.css`).

[^4]: *Id.* (build pipeline walking Cases/, Topics/, and Lectures/ content folders; YAML frontmatter parsing; markdown-it rendering; Obsidian wiki-link resolution to hash routes of the form #/p/<kind>/<slug>; structured holding-bar and citation-metadata extraction per case page; emission of `.site/dist/pages.json`, `.site/dist/manifest.json`, and `.site/dist/search.json`).

[^5]: *See infra* App. A (Vault Architecture and File Layout) (hand-written SPA shell at `.site/dist/index.html`, `.site/dist/app.js`, and `.site/dist/style.css`; hash-route navigation reaching #/cases, #/topics, #/lectures, #/recent, #/about, and #/p/<id>; ⌘K search palette wired to search.json; PostHog analytics configured with `disable_session_recording: true` and `respect_dnt: true`; hidden Netlify `page-feedback` form stub registered at build time).

[^6]: *See infra* fig. 3.8 (deployed site’s ⌘K search palette open with a *Marbury* query active; captured from the deployed site at https://constitutionallaw.netlify.app, May 26, 2026).

[^7]: *See infra* App. A (Vault Architecture and File Layout) (Netlify CLI direct-upload deploy procedure in vault `DEPLOY.md`, authenticated by a local personal access token at `.site/.netlify-token` that is gitignored and never committed).

[^8]: *Id.* (`.site/dist/netlify.toml` disabling post-processing via `skip_processing = true` and registering a single `/*` to `/index.html` SPA-style redirect; three-tier fallback chain documented in `DEPLOY.md` with the Netlify CLI direct upload as the preferred path because it does not consume Netlify build minutes, the Netlify MCP as fallback when the local PAT is missing, and `.site/deploy.sh` as last-resort shell wrapper).

[^9]: *See infra* App. A (Vault Architecture and File Layout) (vault `RUNBOOK.md` Phase: Deploy section, treating Deploy as a first-class rotation phase with its own per-phase rubric file at `rubric/deploy.md`, its own pending-issue lifecycle with `applies_to_phase: deploy`, and a cardinal rule prohibiting publication of any vault that failed the preceding Verify run).

[^10]: *See infra* App. A (Vault Architecture and File Layout) (vault `DEPLOY.md` Step 3.5 post-deploy verification protocol: manifest-count comparison against the production CDN at `https://constitutionallaw.netlify.app/manifest.json`; deterministically sampled five-case-brief-plus-three-topic GET sample with title-presence check; live `search.json` sanity probe confirming a *Marbury*-titled entry whose text contains “judicial review”; five-page Source Materials HEAD sample with Content-Type check; each failure mode opening a typed pending issue (`deploy-count-mismatch`, `deploy-page-sample-failed`, `deploy-search-sanity-failed`, `deploy-source-sample-failed`) and blocking state advance).

[^11]: *See infra* App. A (Vault Architecture and File Layout) (`.site/build.py` wiki-link rendering for any target prefixed `Source Materials/`, emitting `<a class="source-download" href="source/<url-encoded-filename>" download>` and copying the `Source Materials/` tree into `.site/dist/source/`; `.site/dist/_headers` rule applying long-lived `max-age=604800` caching to the `/source/*` path while keeping the generated JSON artifacts on short TTLs).

[^12]: *See infra* App. A (Vault Architecture and File Layout) (vault `RUNBOOK.md` Step 0 feedback-intake protocol pulling submissions from the Netlify `page-feedback` form via the `manage-form-submissions` MCP, triaging each submission to the maintenance phase that can fix it, logging typed pending issues carrying `metadata.page_id`, `metadata.page_title`, `metadata.submitter_name`, `metadata.submitter_email`, `metadata.comment`, and `metadata.netlify_submission_id`, deleting each submission after triage, and requiring each subsequent phase’s scope-selection step to prefer pages with open professor-feedback issues routed to that phase).

[^13]: *See infra* fig. 3.10 (deployed site’s `page-feedback` form in its open state on a case page; captured from the deployed site at https://constitutionallaw.netlify.app, May 26, 2026).

[^14]: *See infra* App. A (Vault Architecture and File Layout) (deployed-site architecture: stable HTML and JSON artifacts produced at publish time by the build pipeline described above and served by the Netlify CDN without further model inference at request time; no LLM in the request path); *see also infra* Section XII (Risks and Limits) (developing the architectural contrast between the static-site case study and chatbot architectures, with reference to the Magesh et al. hallucination findings).

[^15]: *See* Ramteja Sajja, Yusuf Sermet, David M. Cwiertny & Ibrahim Demir, *Platform-Independent and Curriculum-Oriented Intelligent Assistant for Higher Education*, 20 Int’l J. Educ. Tech. Higher Educ., Art. 42 (2023), https://link.springer.com/article/10.1186/s41239-023-00412-7 (last visited May 17, 2026) (presenting a large-language-model-backed curriculum-oriented virtual teaching assistant deployable to any course as a conversational helper; cited here as a representative chatbot-architecture contrast to this article’s static-site case study, the architectural difference Section XII develops as a difference in where runtime risk lives).
