---
section: "05"
fact_type: example
source_path: "Chandler Constitutional Law Vault/Templates/Case Brief.md"
verified: true
notes: "The YAML frontmatter schema is what makes vault pages machine-readable, not just prose. Each page type carries a typed header that downstream phases and the build script read directly. The Case Brief schema has roughly 30 fields covering doctrine labels, citation metadata, authority lineage, and a holding-bar block the deployed site renders as a structured banner above the prose. This is the load-bearing 'schema-not-just-prose' point in Section V."
---

Every Cases page opens with a roughly 30-field YAML frontmatter block before the H1. The fields cover doctrinal labels (`doctrines`, `concepts`), citation metadata (`citation`, `argued`, `decided`, `author`, `vote`, `disposition`), authority lineage (`relies_on`, `distinguishes`, `applied_in`, `overrules`, `overruled_by`), Midpage verification anchors (`midpage_id`, `midpage_url`), and a structured holding-bar block (`issue`, `holding`, `reasoning`, `doctrine_family`) that the deployed site promotes into a banner above the prose. Topic and Lecture pages carry analogous but smaller schemas. The schema lives inline in each `Templates/*.md` file as an HTML comment block directly below the YAML, with per-field population guidance.

Exact source excerpt, `Chandler Constitutional Law Vault/Templates/Case Brief.md` lines 1 to 43:

> ```
> ---
> case_name: "{{Case Name}}"
> citation: "{{Volume}} {{Reporter}} {{Page}}"
> year: "{{Year}}"
> court: "{{Court}}"
> doctrines:
>   - "{{Doctrine 1}}"
>   - "{{Doctrine 2}}"
> concepts:
>   - "{{Concept 1}}"
> status: "{{good law | superseded | overruled | limited | narrowed}}"
> midpage_id: "{{Midpage opinion ID if available}}"
> midpage_url: "{{Midpage URL if available}}"
> treatment: "{{Neutral | Positive | Negative | Cautionary}}"
> cited_by: "{{number of citing cases if known}}"
> verified: "{{YYYY-MM-DD}}"
> source_files:
>   - "{{Source Materials/filename.pdf or Source Materials/Midpage analyzeOpinion (opinionId N)}}"
>
> # Holding-bar fields. The deployed site promotes these into a structured
> # banner above the prose. Ingest leaves empty strings / lists; Enrich fills.
> issue: ""
> holding: ""
> reasoning: ""
> doctrine_family: ""
>
> # Citation metadata. Ingest fills what's on the opinion face; Enrich completes.
> argued: ""
> decided: ""
> panel: ""
> author: ""
> vote: ""
> disposition: ""
>
> # Authority lineage. Ingest leaves empty; Enrich populates from the opinion +
> # CourtListener find_cited_cases / find_citing_cases.
> relies_on: []
> distinguishes: []
> applied_in: []
> overrules: ""
> overruled_by: ""
> ---
> ```
