---
section: "03"
fact_type: example
source_path: "Chandler Constitutional Law Vault/.site/dist/app.js"
verified: true
notes: "The Cases and Topics index pages a student opens after the entry shell. Cases is a filter-rail-plus-year-blocks digest; Topics is a four-family grid keyed to the doctrine_family enum that Section V documents in evidence-05-doctrine-family-enum.md. These are the gallery surfaces between the entry nav and the destination pages — the Section III walkthrough has to show that the deployed site has navigation affordances above the page level, not just hyperlinked content. The four-family grid is also one of the workplan §3.2 screenshot needs."
---

Once a student clicks Cases or Topics in the top-nav, the deployed site renders an index page rather than a flat alphabetical list. The Cases index (`#/cases`) is a filter rail down the left side keyed to the area frontmatter field (Federalism, Separation of Powers, Individual Rights, Justiciability and similar one-word area labels) with year-grouped case blocks in the main panel; clicking an area on the rail filters via the URL parameter (`#/cases?area=Federalism`) without a page reload. The Topics index (`#/topics`) renders a four-family grid keyed to the same `doctrine_family` enum Section V documents — Federalism, Separation of Powers, Individual Rights, Justiciability — each family showing its constituent Topic pages as cards under the family heading. The Dashboard route (`#/`) wraps both with a stats table showing case counts by area and a "See all cases" CTA into the Cases index. The walkthrough Section III has to convey is that a student does not have to know a case name in advance; the indexes let the student start from a doctrine or an area and drill down to the pages.

Exact source excerpt, `Chandler Constitutional Law Vault/.site/dist/app.js` lines 4 to 7 (route header):

> ```
> *   #/cases              Cases digest (filter rail + year blocks)
> *   #/topics             Topics spotlight + four-family grid
> ```

Exact source excerpt, `Chandler Constitutional Law Vault/.site/dist/app.js` line 308 and lines 319 to 320 (Dashboard area table linking into the Cases filter rail):

> ```
> <a class="more" href="#/cases">See all cases →</a>
> ...
> <a class="dash-table-row" href="#/cases?area=${encodeURIComponent(name)}">
> ```

Exact source excerpt, `Chandler Constitutional Law Vault/.site/dist/app.js` lines 486 to 487 and line 493 (route dispatch into the index renderers):

> ```
> if (kind === 'case')    return renderCasesIndex(params);
> if (kind === 'topic')   return renderTopicsIndex(params);
> ...
> function renderCasesIndex(params) {
> ```
