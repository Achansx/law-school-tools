# Rubric: Verify

Scale: 5 exemplary, 4 solid, 3 acceptable, 2 below expectations, 1 serious, 0 failure. Weighted average rounded to one decimal.

| Criterion | Weight | Red Flag At | Method |
|-----------|--------|-------------|--------|
| adversarial_findings | 0.28 | 0 | Forced-finding count from the three personas. 0 -> 0. 1 to 2 -> 2. 3 to 4 -> 4. 5 or more -> 5. |
| holding_verification | 0.17 | 1 | Sample of case briefs had holdings spot-checked against Midpage. All correct -> 5. One inaccuracy -> 3. More -> 1. |
| cross_file_consistency | 0.15 | 0 | Inter-page contradictions flagged (same case described differently in two pages). 0 -> 2. 1 or more with evidence -> 5. |
| pending_issues_emitted | 0.20 | 1 | Every finding yielded a pending issue for the next phase. All -> 5. Any unlogged -> 2. |
| pending_issue_aging | 0.10 | 0 | The aging sweep ran (auto-close at 14d stale-without-touch, escalate at 30d to `triage.md`) and `state.pending_issues` shrank or held steady relative to last Verify. Sweep ran AND no entry older than 30 days remains in state -> 5. Sweep ran but at least one 30+ day entry still in state without a documented reason -> 3. Sweep skipped -> 0 AND a `aging-sweep-skipped` red flag. |
| scope_discipline | 0.10 | 0 | Verify stayed inside its declared scope — three adversarial personas only, each within its declared PERSONAS.md sample size, plus the aging sweep. No cross-cutting "while I was here I also" rewrites of touched pages, no Topic page authoring masquerading as findings, no out-of-scope content authoring. All three personas in scope -> 5. One persona drifted -> 3. Two or more drifted, OR Verify wrote new content beyond the inline trivial-fix exception -> 0 AND a red flag. |
| brevity | 0.05 | 0 | This run's CHANGELOG entry stays inside the 120-word cap and uses the fixed shape from SKILL.md Step 2.3 (Did/Found/Files/Score/State bullets, optional fenced JSON extras — no prose paragraphs); aging+timeline sweep counts go in the JSON extras block, not in prose. The BUILD_NARRATIVE paragraph stays inside the 80-word cap (sweep counts fold into the sentence). Compliant on both -> 5. One overflow under 50% over cap -> 3. Either overflow over 50% over OR per-phase JSON extras rendered as prose OR persona-by-persona prose preambles -> 0 AND a red flag. |
