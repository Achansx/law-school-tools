---
section: "05"
fact_type: example
source_path: "Chandler Constitutional Law Vault/Cases/Marbury v Madison (1803).md"
verified: true
notes: "A real, populated case brief showing what the schema looks like once Enrich has filled it. Marbury's frontmatter carries midpage_id 84759, midpage_url to the Midpage opinion record, cited_by 3995 (pulled from CourtListener), an applied_in list naming six downstream SCOTUS cases (Martin, McCulloch, Prize Cases, Rahimi, Cohens, City of Boerne), the four-bucket doctrine_family value, and the full holding-bar block. Section V uses this to make the abstract 'schema makes pages machine-readable' claim concrete — the build script can render a holding bar, a citation count, an authority lineage graph, and a downstream-citing-cases table directly off these fields, without parsing the prose."
---

A real populated brief shows what the schema produces once Enrich has filled the empty Ingest-time fields. The Marbury v Madison (1803) brief carries `midpage_id: '84759'`, a canonical Midpage `midpage_url`, `cited_by: 3995` (pulled from CourtListener `find_citing_cases`), a populated `applied_in` list naming six downstream Supreme Court cases (Martin v Hunter's Lessee, McCulloch v Maryland, The Prize Cases, United States v Rahimi, Cohens v Virginia, City of Boerne v Flores), the locked four-bucket value `doctrine_family: Separation of Powers`, the full holding-bar block (`issue`, `holding`, `reasoning`), and `verified: '2026-04-24'`. The build script renders a holding bar, a citation count, an authority lineage display, and a downstream-citing-cases table directly off these typed fields, without parsing the prose.

Exact source excerpt, `Chandler Constitutional Law Vault/Cases/Marbury v Madison (1803).md` lines 1 to 43 (frontmatter, abbreviated):

> ```yaml
> case_name: Marbury v Madison
> citation: 5 U.S. 137
> year: 1803
> midpage_id: '84759'
> midpage_url: https://app.midpage.ai/document/marbury-v-madison-84759
> cited_by: 3995
> verified: '2026-04-24'
> applied_in:
> - Martin v Hunter's Lessee (1816)
> - McCulloch v Maryland (1819)
> - The Prize Cases (1863)
> - United States v Rahimi (2024)
> - Cohens v Virginia (1821)
> - City of Boerne v Flores (1997)
> doctrine_family: Separation of Powers
> author: Marshall, C.J
> decided: '1803-02-24'
> vote: Unanimous (Marshall for the Court; no dissents recorded)
> disposition: Rule discharged (writ of mandamus denied for want of original jurisdiction)
> ```
