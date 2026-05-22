---
section: "07"
fact_type: example
source_path: "Chandler Constitutional Law Vault/PROJECT_PRIMER.md"
verified: true
notes: "PROJECT_PRIMER names the canonical phase rotation as Ingest -> Lint -> Enrich -> Expand -> Synthesize -> Verify -> repeat. RUNBOOK extends the rotation with a Deploy phase that runs after Verify and owns its own scorecard, but Deploy is the territory of Section VIII; Section VII covers the six maintenance phases that produce the deployed artifact. Each scheduled-task tick executes one phase per run. Per-phase procedures live in RUNBOOK.md and are referenced rather than duplicated in PROJECT_PRIMER; per-phase rubrics live in rubric/<phase>.md and are loaded only by the active phase per the tiered-loading discipline that closed the token problem (see evidence-07-token-problem-rubric-split). The one-phase-per-run constraint is the article's structural answer to the Karpathy loop: instead of running an autonomous loop that touches every phase every pass, the vault commits one phase per pass and lets the rotation be the loop, which keeps each pass small enough for a professor to inspect and lets phase-specific quality differ instead of being averaged into a single per-pass score. Per L-031 the article must not anthropomorphize the rotation or the deployed artifact; the rotation is what the scheduled-task runs against the vault, not what the vault does to itself."
---

The Constitutional Law vault runs a six-phase rotation: Ingest, Lint, Enrich, Expand, Synthesize, Verify, then repeat. Each phase has a documented procedure in `RUNBOOK.md` and a separate scoring rubric in `rubric/<phase>.md`. Each scheduled-task tick selects one active phase, executes its procedure once, writes the resulting state, and advances `next_phase` for the following tick. The one-phase-per-tick commitment is the loop's central structural choice; an autonomous Karpathy-style loop touches every phase every pass, while the vault commits one phase per pass so the professor can inspect each pass on its own terms and the rotation itself becomes the loop.

Exact source quote, `Chandler Constitutional Law Vault/PROJECT_PRIMER.md` lines 60 to 62:

> ## Phase Rotation
>
> Ingest -> Lint -> Enrich -> Expand -> Synthesize -> Verify -> repeat
