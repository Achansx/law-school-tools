---
section: "06"
fact_type: example
source_path: "Chandler Constitutional Law Vault/RUNBOOK.md"
verified: true
notes: "The `<!-- ENRICH: -->` stub markers are the prompt-to-prompt handoff convention. Ingest places stub markers naming what the next phase should add; Enrich reads each marker and fulfills it as a distinct sub-prompt; once a brief carries zero stubs, `verified` flips from 'pending-enrich' to today's date. The Ingest rubric's stub_markers_present criterion requires every deferred section to carry a one-sentence ENRICH description; the Enrich rubric's stubs_resolved criterion measures the fraction of markers each Enrich run resolved. The markers are not internal scaffolding the deployed site needs to hide; they are the prompt design pattern that decomposes a complex generation task across multiple phases without losing track of what each phase is supposed to do. Section VI should use this card to make the point that prompt design in the vault is at least as much about prompt-to-prompt handoffs as about any single prompt's wording. The same pattern shows up in the LESSONS.md 'Ingest skeletons must always carry an ENRICH stub in Connections' rule, where filling Connections at Ingest bypasses Expand's target-existence check and seeds broken links."
---

The vault's prompt architecture decomposes case-brief generation across phases using HTML-comment stub markers as the handoff convention. Each Ingest skeleton carries `<!-- ENRICH: one-sentence description -->` markers in every section it deliberately did not fill: concurrence reasoning, dissent reasoning, all five Hypothetical Applications, both Critique angles, additional Key Quotations, and Connections. The Ingest rubric's stub_markers_present criterion scores 5 only when every deferred section across the batch carries a stub with a one-sentence description; missing markers on one brief drops the score to 3 and on two or more drops it to 1. Enrich then reads each marker as a distinct sub-prompt and fulfills it; the Enrich rubric's stubs_resolved criterion, weighted at 0.22 of the run score, measures the fraction of markers each Enrich run actually closed. A brief flips from `verified: "pending-enrich"` to a today-dated `verified` only when every stub on the brief has been resolved. The markers are the mechanism that decomposes a long generation task into a sequence of smaller, gradable, individually inspectable sub-tasks, each owned by the phase whose prompt is best suited to it.

Exact source quote, `Chandler Constitutional Law Vault/rubric/ingest.md` stub_markers_present criterion (line 12):

> | stub_markers_present | 0.15 | 0 | Every deferred section has a `<!-- ENRICH: one-sentence description -->` marker (at minimum: concurrence, dissent, Hypothetical Applications, Critique, additional Key Quotations, Connections). All stubs present across all new briefs -> 5. Missing on one brief -> 3. Missing on two or more -> 1. N/A on a pure-backfill run. |

Exact source quote, `Chandler Constitutional Law Vault/rubric/enrich.md` stubs_resolved criterion (line 9):

> | stubs_resolved | 0.22 | 0 | Fraction of `<!-- ENRICH: -->` markers in-scope briefs that were replaced with substantive prose. 100% on 3+ briefs -> 5. 80 to 99% -> 4. 50 to 79% -> 3. Below 50% -> 1. |
