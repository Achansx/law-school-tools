---
section: "06"
fact_type: argument
source_path: "Chandler Constitutional Law Vault/LESSONS.md"
verified: true
notes: "LESSONS.md is the prompt-iteration memory file. Each entry follows a fixed schema (Rule. Why. How to apply. Seen.) capped at 60 words and 35 entries with a consolidation sweep; entries are loaded only by content-editing phases (Ingest, Enrich, Expand, Synthesize) because Lint and Verify do not need them. The file is what converts one-time prompt failures into durable prompt amendments. Examples worth naming in the article body: 'Match house style: prefer commas, colons, parentheses, sentence breaks over em dashes' is a Polish-rule mirror at the prompt level; 'Do not invent case details' is the fabrication-discipline rule the prompt restates every run; 'Ingest skeletons must always carry an ENRICH stub in Connections, not pre-filled wiki-links' is a prompt rule that was added after Learning Resources Inc v Trump showed the failure mode. Section VI should use this card to make the point that the vault's prompt library is not static; it is a living memory of what each prompt has previously gotten wrong, with the corrections compounded back into the prompt as durable amendments. The file's tiered-loading rule ('loaded only for content-editing phases') is itself an instance of the same prompt-engineering discipline applied to prompt-loading economics; the same architecture appears in Article/LESSONS.md, which is what makes the article's own method legible."
---

The vault's LESSONS.md file is the prompt-iteration memory. Each entry follows a fixed schema (Rule, one sentence; Why, consequence or root cause; How to apply, the concrete check; Seen, italic footer of up to three dated instances) capped at 60 words and 35 total entries with an out-of-rotation Consolidate sweep that triggers on accumulation. Content-editing phases (Ingest, Enrich, Expand, Synthesize) load the file at the start of every run; Lint and Verify skip it unless a phase-specific persona needs it, an economy that reduces the per-run token cost without losing the corrections that matter for content generation. Three representative entries: "Match house style: prefer commas, colons, parentheses, sentence breaks over em dashes" amends every content prompt with the JLE-idiomatic typography rule; "Do not invent case details" restates the fabrication-discipline rule at the top of every Enrich pass; "Ingest skeletons must always carry an ENRICH stub in Connections, not pre-filled wiki-links" is an amendment added after the Learning Resources Inc v Trump skeleton seeded three broken links by filling Connections at Ingest time and bypassing Expand's target-existence check. The file is what makes the vault's prompt library compound rather than restart.

Exact source quote, `Chandler Constitutional Law Vault/LESSONS.md` header (lines 5 to 11):

> **Entry cap: 35.** When at or above the cap, do NOT append new lessons. Log the candidate to `pending_issues` with `type: lesson-candidate` and let the next Consolidate sweep merge duplicates and prune superseded entries.
>
> **Entry shape (60 words max).** Rule, one sentence. **Why:** consequence or root cause. **How to apply:** the concrete check, command, or trigger. _Seen:_ italic footer with up to three dated instances; drop the oldest when adding a fourth.
>
> **Loaded only for content-editing phases.** The scheduled task reads this file during Ingest, Enrich, Expand, and Synthesize. Lint and Verify skip it unless a phase-verify persona specifically needs it.

Exact source quote, `Chandler Constitutional Law Vault/LESSONS.md` Connections-stub rule (line 61):

> **Ingest skeletons must always carry an ENRICH stub in Connections, not pre-filled wiki-links.** **Why:** filling Connections at Ingest bypasses Expand's target-existence check and seeds broken links. **How to apply:** drop a `<!-- ENRICH: ... -->` marker noting intended connections; let Expand verify and add. _Seen: Learning Resources Inc v Trump (4 wiki-links, 3 to non-existent files)._
