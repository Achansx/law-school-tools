---
section: "06"
fact_type: argument
source_path: "Chandler Constitutional Law Vault/RUNBOOK.md"
verified: true
notes: "The Ingest prompt is a deliberately under-completed prompt. It is the clearest example in the vault of a prompt whose pedagogical move is to refuse a request rather than fulfill it: the run that produces a full nine-section brief in a single pass is the run that is scored down, because it starves the next phase of analytical work. The Enrich rubric's scope_discipline criterion makes this mechanical. Section VI should use this card to make the point that prompt design in the vault is partly about what the prompt is NOT allowed to do. The RUNBOOK Step 5 and rubric/ingest.md scope_discipline excerpts together carry the convention. This is the same pattern Karpathy's autoresearch loop uses (a single experiment per overnight run, scored against the prior run) imported into a pedagogical setting; Section VII develops the broader Karpathy-loop framing."
---

The Ingest phase prompt deliberately under-completes the case brief. The RUNBOOK instructs the prompt to populate Memory Jogger, Facts, Procedural History, Judicial Votes, and Holding at full depth, to write a majority-only Analysis sketch of roughly 150 words, to place exactly one Midpage-verified pin-cited quotation in Key Quotations, and to leave every other section as a one-line `<!-- ENRICH: -->` stub marker. The Ingest rubric then scores a run down if it produced a finished brief in a single pass: scope_discipline returns 0 and a red flag for any brief written at nine-section depth or flipped to a today-dated `verified` during Ingest. The pedagogical move is the under-completion itself. A nine-section brief written in a single pass loses the iterative pressure that produces analytical depth on the second and third reads; the stub markers are the mechanism that forces a later phase to read the opinion again with a different question in mind.

Exact source quote, `Chandler Constitutional Law Vault/RUNBOOK.md` Phase: Ingest Step 5 (lines 34 to 42):

> 5. For each case PDF, produce a **skeleton case brief**, not a finished one:
>    [...]
>    - Fill at full depth ONLY: Memory Jogger, Facts, Procedural History, Judicial Votes, and Holding. These are factual and should not require re-reading during Enrich.
>    - Write a majority-only Analysis sketch of roughly 150 words that captures the rule the majority adopted and its chief reasoning. Do not write the concurrence or dissent analysis.
>    - Put exactly one Midpage-verified pin-cited quotation in Key Quotations.
>    - Stub the remaining sections with single-line `<!-- ENRICH: {one-sentence description of what Enrich should add} -->` markers. Stub at minimum: concurrence reasoning, dissent reasoning, Hypothetical Applications (all five), Critique (both progressive and originalist), additional Key Quotations, and Connections.

Exact source quote, `Chandler Constitutional Law Vault/rubric/ingest.md` scope_discipline criterion (line 13):

> | scope_discipline | 0.10 | 0 | Verify none of the skeleton briefs were written at 9-section depth. `verified` on every new brief is `"pending-enrich"`. Any brief written at full depth or flipped to today's date during Ingest -> 0 here and a red flag.
