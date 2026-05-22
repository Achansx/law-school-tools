---
section: "06"
fact_type: example
source_path: "Chandler Constitutional Law Vault/PERSONAS.md"
verified: true
notes: "The Verify phase prompt is three adversarial personas (Staleness Auditor, Contradiction Hunter, Template Enforcer) plus a rotation lever and a per-persona focus-mutation lever, both keyed off state.verify_run_count to prevent any single charter from anchoring every run. Every persona MUST return at least one finding; a persona that finds nothing must record 'persona-produced-nothing' as its finding. This is the prompt-engineering pattern Section VI needs to anchor the article's claim that adversarial reading is a pedagogical move, not just a quality gate. The three-persona structure mirrors moot-court and law-review-editor pedagogy where the work is exposed to readers with different reading commitments rather than to a single generic reader. Section VI should use this card to make the point that the vault implements adversarial reading at the prompt level rather than as an external review process; the same approach maps onto Section XII's risk argument (a static reviewed site exposes outputs to inspection in a way a runtime chatbot does not)."
---

The Verify phase prompt instantiates three adversarial personas (Staleness Auditor, Contradiction Hunter, Template Enforcer) and requires each to return at least one finding per run; a persona that finds nothing must record `persona-produced-nothing` as its own finding rather than report a clean read. Two diversity levers prevent the same persona from setting the framing of every run: a three-row rotation table rotates which persona runs first, second, and third (keyed off `state.verify_run_count % 3`), and each persona's own four-row focus table narrows what it samples on each run (keyed off `state.verify_run_count % 4`, deliberately offset from the lead-rotation cycle so that lead-and-focus pairings change every run rather than locking into a twelve-run loop). The forced-finding requirement is what converts the prompt from a quality check into a pedagogical move: a Verify pass that returns nothing is not a Verify pass, the way a moot-court bench that asks no hard questions has not done its work.

Exact source quote, `Chandler Constitutional Law Vault/PERSONAS.md` opening paragraphs (lines 1 to 21):

> # Personas
>
> Three hostile personas for the Verify phase of the Con Law wiki. Each must return at least one concrete finding per run. If a persona genuinely finds nothing, it records `persona-produced-nothing` as its own finding.
>
> [...]
>
> The three personas always run on every Verify pass, but the order they run in cycles so that no single persona gets to set the framing of the run every time. The lead persona is the one whose findings are listed first in the Verify summary, and whose output is loaded first when the next run scores its red flags. Order matters because later personas tend to read earlier findings before deciding what to flag, so a fixed order silently anchors the entire vault on one charter.
>
> Order is determined by `state.verify_run_count` (zero-indexed integer that Verify increments by 1 at the start of every successful run, before scoring).
