---
section: "06"
fact_type: example
source_path: "Chandler Constitutional Law Vault/RUNBOOK.md"
verified: true
notes: "The Midpage-verification prompt enforces a practitioner habit: quotations from a judicial opinion must be confirmed against the indexed opinion, not against the paraphrased PDF the professor distributed. Both Ingest and Enrich are required to gate Key Quotations on Midpage's findInOpinion or analyzeOpinion API; the LESSONS.md Midpage discipline entries record what happens when the prompt does not enforce this (the Prize Cases / Grier story, in which a modernized PDF silently rewrote archaic phrasing and only an adversarial Verify pass caught the drift). Section VI should use this card to make the point that the vault's prompt design encodes a pedagogical commitment that is also a malpractice avoidance commitment: a student or attorney who internalizes the no-verify habit through AI tools will repeat the Mata v. Avianca error in practice (Section XII develops the malpractice frame; Section VI carries the prompt-design frame). The vault's own L-004 quote-verification protocol mirrors the same rule, which is why the article describes its own method using the same discipline."
---

The Ingest and Enrich phase prompts both gate Key Quotations on Midpage verification. Ingest requires exactly one Midpage-verified pin-cited quotation per new case brief, with `midpage_id` and `midpage_url` populated; the rubric's midpage_verification criterion scores the run at 1 if no new brief carries the verification. Enrich adds two to three more Midpage-verified quotations per brief beyond the Ingest pull. The prompt-level commitment is that a quotation that has not been confirmed against the indexed opinion does not enter the vault, regardless of how plausible the language reads in the source PDF. The Prize Cases / Justice Grier example documents what happens when the discipline lapses: the professor's modernized PDF silently rewrote Grier's "never solemnly declared . . . by its accidents" as "never formally declared . . . by its character," and an Ingest pass plus a Lint pass plus two Enrich passes plus an Expand pass all reproduced the modernized phrasing faithfully because none of them re-checked against the indexed opinion. Only the adversarial Verify pass, switching from keyword search to Midpage analyzeOpinion of the indexed text, returned the actual language.

Exact source quote, `Chandler Constitutional Law Vault/RUNBOOK.md` Phase: Enrich cardinal rules (line 114):

> Cardinal rules for Enrich: never invent details; every filled stub traces to a PDF, a Midpage result, or a web-search citation; Key Quotations are Midpage-verified text with pin-cite URLs or they do not go in.

Exact source quote, `Chandler Constitutional Law Vault/rubric/ingest.md` midpage_verification criterion (line 14):

> | midpage_verification | 0.10 | 0 | Each new case brief carries exactly one Midpage-verified pin-cited quote and populated `midpage_id`/`midpage_url`. 100% -> 5. 50% -> 3. 0% -> 1. N/A on a pure-backfill run. |
