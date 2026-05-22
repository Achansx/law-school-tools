---
section: "08"
fact_type: argument
source_path: "Chandler Constitutional Law Vault/.site/build.py"
verified: true
notes: "The build pipeline shape. Section VIII needs to be specific about what the build actually does: it is a Python script that walks the three content folders (Cases, Topics, Lectures), renders markdown with markdown-it, resolves wiki-links into hash-route SPA links, extracts a holding bar and citation metadata per case, and emits three JSON artifacts (pages.json, manifest.json, search.json) that the hand-written shell loads at runtime. There is no React build, no Jekyll or Hugo, no headless CMS, no LLM in the request path. The build is roughly 700 lines of Python and a static shell of three hand-edited files (index.html, app.js, style.css). This shape matters: it keeps the production surface narrow enough that a single attorney-author can reason about every step from markdown to page render."
---

The build pipeline is one Python script (`.site/build.py`) plus three hand-written static-shell files (`index.html`, `app.js`, `style.css`). The script reads the vault's three content folders — `Cases/`, `Topics/`, `Lectures/` — parses each page's YAML frontmatter, renders the markdown body with `markdown-it`, resolves Obsidian-style `[[wiki-link]]` syntax into in-app hash routes of the form `#/p/<kind>/<slug>`, extracts a structured holding-bar and citation-metadata block from each case page, and writes three JSON artifacts to `.site/dist/`: `pages.json` (full corpus with rendered HTML and search text), `manifest.json` (lightweight index for nav and counts), and `search.json` (compact text index for the search palette). The shell loads those JSON files at runtime and renders client-side; no server framework, no headless CMS, no LLM in the request path. The architectural payoff is in Section XII: the production surface is narrow enough that the attorney-author can reason about every step from markdown source to rendered page without a model in the loop.

Exact source quote, `Chandler Constitutional Law Vault/.site/build.py` lines 1 to 15 (module docstring and imports):

> #!/usr/bin/env python3
> """Build pages.json and search index from the Chandler Con Law Vault.
>
> Produces:
> - pages.json: full corpus (frontmatter + rendered HTML + plaintext for search)
> - manifest.json: lightweight list of pages for index/nav
> - search.json: compact index {id, title, kind, area, doctrines, text}
> """

And lines 32 to 39 (vault walk and renderer setup):

> VAULT = Path(os.environ.get("VAULT_DIR", "/sessions/adoring-dreamy-hypatia/mnt/Chandler Constitutional Law Vault"))
> OUT   = Path(os.environ.get("OUT_DIR", "/sessions/adoring-dreamy-hypatia/mnt/outputs/conlaw-site/dist"))
> KINDS = [("Cases", "case"), ("Topics", "topic"), ("Lectures", "lecture")]
>
> WIKILINK_RE  = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
> CALLOUT_RE   = re.compile(r"^> \[!([a-z]+)\](.*)$", re.IGNORECASE)
>
> md = MarkdownIt("commonmark", {"html": True, "linkify": True, "breaks": False}).enable("table").enable("strikethrough")
