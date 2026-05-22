---
section: "09"
fact_type: argument
source_path: "Chandler Constitutional Law Vault/Article/RUNBOOK.md"
verified: true
notes: "The per-tick token-economy mechanism that keeps phase cost bounded. The Article RUNBOOK plus the Article LESSONS.md L-007 (per-phase rubric only) plus the vault LESSONS.md tiered-loading rule together make 'load only what this phase needs' the controlling architectural property for per-tick token spend. The scheduled-task SKILL.md is explicit: Tier 1 reads always (PROJECT_PRIMER, .article-state.json, RUNBOOK section for current_phase); Tier 2 reads current phase only (rubric/<current_phase>.md, LESSONS.md, optionally PERSONAS.md for Verify, and the current month's BUILD_NARRATIVE). 'Do not read other rubrics. Do not read archived narratives.' is the per-tick token-spend ceiling expressed as a load policy. Section IX uses this as the structural account of why per-tick cost is bounded and reproducible across rotations: the load policy makes one tick of one phase a predictable token unit, and weekly token spend can then be back-computed by multiplying per-tick spend by tick frequency (per evidence-09-scheduled-task-cadence). The card's claim is qualitative architectural (the load policy bounds per-tick cost) rather than numeric; the per-tick token-spend numbers themselves stay open under PI-049."
---

The Article RUNBOOK names tiered context loading as the controlling per-tick token-economy mechanism: every run loads PROJECT_PRIMER, the state file, and the runbook section for the current phase as Tier 1; the current phase's rubric, LESSONS.md, the current month's BUILD_NARRATIVE, and PERSONAS only for Verify as Tier 2. The scheduled-task instructions are explicit that other rubrics and archived narratives are not loaded. The same architectural property runs in the vault scheduled task per its own RUNBOOK and per the vault LESSONS.md tiered-loading rule, and Article LESSONS.md L-007 (per-phase rubric only) makes the cross-rubric-reading prohibition explicit because cross-rubric loading would create conflicting incentives at the rubric level and conflicting token-spend ceilings at the cost level. Section IX uses this as the structural account of why per-tick cost is bounded and reproducible across rotations: the load policy makes one tick of one phase a predictable token unit, and per evidence-09-scheduled-task-cadence weekly token spend can then be back-computed by multiplying per-tick spend by tick frequency.

Exact source quote, `Chandler Constitutional Law Vault/Article/RUNBOOK.md` Dispatcher protocol (lines 5 to 16):

> ## Dispatcher protocol (every run)
>
> 1. Read `Article/.article-state.json`. Identify `current_phase` and `gates`.
> 2. If any gate has `awaiting_human: true`, log one line to `BUILD_NARRATIVE` and stop. Do not advance.
> 3. Otherwise, load `Article/rubric/<current_phase>.md` and `Article/LESSONS.md`.
> 4. Execute the phase per the section below.
> [...]

And `Chandler Constitutional Law Vault/Article/LESSONS.md` L-007 (lines 68 to 74):

> ## L-007: Per-phase rubric only
>
> phase: dispatcher
> impact_score: 4
> date: 2026-05-15
> rule: Each run loads only its own phase rubric, not the others. Cross-rubric reading creates conflicting incentives.
> context: Vault maintenance hit this same problem; splitting the rubric fixed it. Same architecture here.
