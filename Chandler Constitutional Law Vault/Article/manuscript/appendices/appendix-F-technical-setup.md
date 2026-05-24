---
id: appendix-F
title: "Technical Setup"
status: none
words: 0
target_min: 500
target_max: 800
last_phase: none
source_files:
  - "<vault>/.site/build.py"
  - "<vault>/.site/dist/netlify.toml"
  - "<vault>/.site/dist/index.html"
  - "<vault>/DEPLOY.md"
  - "<vault>/RUNBOOK.md (Deploy phase section)"
---

# Appendix F: Technical Setup

<!-- TODO (Harvest appendix tick): The vault → website pipeline, in enough detail that a replicating faculty member can stand up the same architecture.

Structure:

## F.1 Component stack

A diagram or list:
- Obsidian (markdown editor)
- Git (version control)
- .site/build.py (custom static site generator — describe what it does)
- Netlify CLI (deploy)
- PostHog (analytics)
- (any other components)

## F.2 The vault layout

Top-level folder structure with one-line descriptions:
- Cases/
- Topics/
- Lectures/
- Source Materials/
- Templates/
- .site/
- (etc.)

## F.3 Build pipeline

Step-by-step:
1. Markdown files in vault (Obsidian-native, wikilinks)
2. `.site/build.py` traverses, resolves wikilinks, renders HTML
3. Output to .site/dist/
4. Netlify CLI uploads to the live site
5. PostHog tracks page views (privacy-respecting; document opt-out)

Include the actual netlify.toml configuration (skip-processing flags).

## F.4 Quotation verification protocol

The Midpage MCP + indexed-opinion workflow (the Prize Cases / Grier example walkthrough belongs in Section VII; this appendix gives the reproducible procedure).

## F.5 Costs of reproduction

- Required: Obsidian (free), Git, a static-site-friendly host (Netlify free tier covers most needs), Claude API or Claude Code (paid), Midpage account (if doing legal-quote verification)
- Optional: PostHog (free tier), custom domain

## F.6 Forking notes

If a faculty member wants to clone the vault structure for their own course:
- Vault is git-tracked at github.com/Achansx/law-school-tools (this paper's commits live there too)
- Templates/ and rubric/ folders are the most reusable artifacts
- Walk-through: clone → edit PROJECT_PRIMER.md → adapt rubrics → start your own ingest

Footnote anchors: Section VIII (Vault to Website) is the main consumer; Section III (Case Study) may also cite for screenshot context.
-->
