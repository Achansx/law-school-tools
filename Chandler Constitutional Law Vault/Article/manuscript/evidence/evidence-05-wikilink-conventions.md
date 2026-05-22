---
section: "05"
fact_type: example
source_path: "Chandler Constitutional Law Vault/PROJECT_PRIMER.md"
verified: true
notes: "The Obsidian wiki-link grammar plus the source-attribution convention. Two structural points: (1) cross-page links use [[folder/filename|Display Text]] and the deployed site renders these as anchor tags; (2) every page carries a source_files frontmatter list in sync with a ## Sources footer section, both pointing at Source Materials/ entries. These conventions are what let the vault behave as a navigable graph instead of a folder of isolated files. Section V uses this to support the claim that structure does retrieval work pure semantic similarity cannot."
---

The vault uses a small fixed grammar of structural conventions that the build script reads directly. Cross-page wiki-links take the form `[[folder/filename|Display Text]]` and the build emits anchor tags for navigation. Tags are lowercase-hyphenated and placed at file end before a closing `---` (Cases close with `#con-law-i #case`; Topics with `#con-law-i #topic`; Lectures with `#con-law-i #lecture`). Every page carries a provenance trail: `source_files` in frontmatter and a `## Sources` footer section both list the inputs that fed the page, kept one-to-one in lockstep. Cases and Lectures attribute upward to `Source Materials/` files; Topics attribute upward to the Cases and Lectures wiki pages that were directly consulted. The Lint phase enforces frontmatter-footer sync as a structural check.

Exact source quote, `Chandler Constitutional Law Vault/PROJECT_PRIMER.md` lines 47 to 55:

> - Every page opens with YAML frontmatter delimited by `---`, before the H1.
> - One H1 per file (matches filename minus `.md`).
> - H2 sections follow template order.
> - Wiki-links: `[[folder/filename|Display Text]]`.
> - Tags: lowercase-hyphenated, placed at file end before the final `---`.
> - Section separators: `---` with blank lines above and below.
> - Case briefs scale the 9-section standard by importance.

Exact source quote, `Chandler Constitutional Law Vault/RUNBOOK.md` source-attribution convention section:

> **Source attribution convention.** Every wiki page carries a provenance trail:
> - **Cases and Lectures:** `source_files` in frontmatter and a `## Sources` footer section both list the raw Source Materials entries that fed the page. One-to-one with `.ingested-files.jsonl`.
> - **Topics:** `source_files` in frontmatter and `## Sources` footer list the **direct-input** Case and Lecture wiki pages that were actually consulted to draft the Topic, not every case wiki-linked in passing.
