---
section: "03"
fact_type: example
source_path: "Chandler Constitutional Law Vault/archive/vault-blog-post-draft.md"
verified: true
notes: "The Recent tab and the ⌘K search palette as the deployed site's discovery surfaces. The Recent tab carries 'whatever the maintenance cycle has been doing lately' per the professor-facing progress report excerpted in archive/vault-blog-post-draft.md (and in the email itself); the ⌘K palette is the keyboard-driven search surface bound from index.html line 73. Section III walks both as the student-facing discovery affordances above the page level — a student who does not know where to start can open Recent to see what the system most recently touched, or hit ⌘K to type a case or doctrine name and jump directly to the page. Different framing from evidence-08-spa-shell-and-routing (which covers the SPA architecture); this card covers the same two surfaces as student-discovery affordances."
---

The deployed site carries two discovery surfaces above the page level. The Recent tab (`#/recent` from the top-nav) lists pages the maintenance rotation has most recently touched, so a student returning to the site can see what was rebuilt or expanded since the prior visit; this is the surface the professor-facing progress report names by saying "the Recent tab shows whatever the maintenance cycle has been doing lately." The ⌘K search palette (the `cl-search` button on the top-nav, keyboard-shortcut to Command-K) opens an overlay search input with placeholder text "Search cases, topics, doctrines"; the palette indexes case names, topic names, doctrine families, and lecture titles. A student who knows the doctrine name (Commerce Clause) or the case name (Marbury) can jump directly without traversing the index pages; a student who knows neither but remembers the area (Federalism, Separation of Powers, Individual Rights, Justiciability) can use the four-family Topics grid or the area filter rail on the Cases index. Section III walks the three discovery surfaces (Recent, ⌘K palette, four-family Topics grid) as the student-facing layer above the Topic-Case-Lecture destination pages.

Exact source excerpt, `Chandler Constitutional Law Vault/archive/vault-blog-post-draft.md` (the live-site progress passage quoted from `email-to-chandler-progress.md`):

> Quick update on the wiki. It is now live at https://constitutionallaw.netlify.app. Search is in the top bar, and the Recent tab shows whatever the maintenance cycle has been doing lately.
>
> 198 pages so far: 92 cases, 27 topics, 79 lecture summaries.

Exact source excerpt, `Chandler Constitutional Law Vault/.site/dist/index.html` lines 70 and 73 to 77 (Recent nav link and ⌘K search palette trigger):

> ```html
>     <a class="cl-navlink" href="#/recent" data-route="recent">Recent</a>
> ...
>     <button class="cl-search" id="palette-trigger" type="button" aria-label="Open search palette">
>       <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
>       <span class="cl-search-text">Search cases, topics, doctrines&hellip;</span>
>       <kbd>⌘K</kbd>
>     </button>
> ```
