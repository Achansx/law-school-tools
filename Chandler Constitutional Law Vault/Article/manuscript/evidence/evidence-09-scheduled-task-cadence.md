---
section: "09"
fact_type: statistic
source_path: "Chandler Constitutional Law Vault/Article/BUILD_NARRATIVE_2026-05.md"
verified: true
notes: "The cadence anchors that ground the per-tick cost line for both the vault-maintenance scheduled task and the article-writing scheduled task. The article scheduled task fires every two hours per the BUILD_NARRATIVE timestamps (every BUILD_NARRATIVE entry sits two hours after its predecessor, e.g., 2026-05-19T05:00 Cite, 07:00 Polish, 11:00 Stitch, 13:00 Verify) and the vault scheduled task fires every thirty minutes per the vault CHANGELOG note that explicitly logs '30-min interval, tiered context loading; Ingest 3-5 files/run'. Two cadences plus the per-tick token-economy mechanism (Tier 1 always, Tier 2 current-phase-only per the Article RUNBOOK and per L-007) give Section IX the back-computation it needs: per-tick token spend times tick frequency equals weekly token spend, which can then be checked against the email's 60-percent-of-weekly-Claude anchor. Cardinal honesty rule for Section IX: the cadence numbers are vault-anchored and citable; the per-tick token-spend figures are not yet reconstructed and stay open under PI-049 until the workplan §8 backfill protocol runs."
---

The article scheduled task fires every two hours; the vault scheduled task fires every thirty minutes. The article cadence is observable in the BUILD_NARRATIVE_2026-05.md entry timestamps, where each phase tick sits two hours after its predecessor (Cite at 05:00 UTC, Polish at 07:00 UTC, Stitch at 11:00 UTC, Verify at 13:00 UTC on 2026-05-19, for example). The vault cadence is logged in CHANGELOG.md as a thirty-minute interval with tiered context loading and an Ingest budget of three to five files per run. Two cadences plus the per-tick token-economy mechanism (Tier 1 reads always, Tier 2 current-phase-only per the Article RUNBOOK and per L-007) give Section IX the back-computation lever it needs: per-tick token spend multiplied by tick frequency yields weekly token spend, which can then be checked against the email's 60-percent-of-weekly-Claude anchor. The cadence numbers are vault-anchored and citable; the per-tick token-spend figures themselves are not yet reconstructed and stay open under PI-049 until the workplan §8 backfill protocol runs against the email trail and the git log.

Exact source quote, `Chandler Constitutional Law Vault/CHANGELOG.md` line 198 (vault scheduled-task cadence):

> - 30-min interval, tiered context loading; Ingest 3-5 files/run.

And the Article BUILD_NARRATIVE_2026-05.md entry sequence for 2026-05-19 (lines 161 to 175, illustrative; each phase tick is two hours after the previous):

> ## 2026-05-19 — Cite tick (Section 07) [...] `cite_completed_at: 2026-05-19T05:00:00Z`
>
> ## 2026-05-19 — Polish tick (Section 07) [...] `polish_completed_at: 2026-05-19T07:00:00Z`
>
> ## 2026-05-19 — Stitch tick (partial-noop, six-section contiguous assembly closing the V-to-VIII non-adjacency) [...] `stitched_at: 2026-05-19T11:00:00Z`
>
> ## 2026-05-19 — Verify tick (six-section partial-assembly read, first contiguous III-VIII sextet) [...] (verify ran at 2026-05-19T13:00:00Z)
