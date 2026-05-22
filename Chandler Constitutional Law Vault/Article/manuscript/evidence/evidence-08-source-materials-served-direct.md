---
section: "08"
fact_type: example
source_path: "Chandler Constitutional Law Vault/.site/build.py"
verified: true
notes: "The Source Materials mirror. The deployed site does not just publish the AI-authored briefs; it also serves the professor's original PDFs and PowerPoints behind <a class='source-download'> links emitted by the build. This is the transparency artifact that makes the vault different from a chatbot that paraphrases its sources without exposing them: a reader can click through from a brief to the original slide deck or annotated opinion the brief was built from. Section VIII can frame this as the auditable-input commitment that pairs with the auditable-output (reviewed static page) commitment from the static-vs-chatbot card. The _headers caching rules (source PDFs cacheable, JSON artifacts short-TTL) are the operational detail that supports the framing."
---

The site does not only publish the AI-authored briefs; it also serves the professor's original source materials — the PowerPoint lecture decks, the modernized PDFs, the annotated opinions — behind direct download links the build emits whenever a page wiki-links to a file under `Source Materials/`. The build copies the `Source Materials/` tree into `dist/source/`, URL-encodes each filename, and renders any `[[Source Materials/...]]` wiki-link as an `<a class="source-download" href="source/...">` element so a reader on the deployed site can click through from a brief to the original artifact the brief was built from. The `_headers` rules treat these source files with long-lived public caching (`max-age=604800`) while keeping the generated JSON artifacts on short TTLs, so the source layer behaves like a stable archive even as the brief layer turns over. Section VIII can frame this as the auditable-input commitment that pairs with the auditable-output commitment named in the static-versus-chatbot card: a reader can inspect both what the system was given and what it produced.

Exact source quote, `Chandler Constitutional Law Vault/.site/build.py` lines 126 to 135 (wiki-link rendering for Source Materials):

> # Source Materials wikilinks render as direct download links served from
> # /source/<url-encoded-filename>. The build also copies the Source
> # Materials folder into OUT/source so these hrefs actually resolve on
> # the deployed site. We emit the <a> tag directly (mirroring the
> # broken-link span pattern above) so markdown-it does not mangle the
> # URL-encoded filename.
> if target_clean.startswith("Source Materials/"):
>     sub = target_clean[len("Source Materials/"):]
>     href = "source/" + "/".join(_urlquote(part) for part in sub.split("/"))
>     return f'<a class="source-download" href="{href}" download>{label}</a>'
