---
section: "09"
fact_type: argument
source_path: "Chandler Constitutional Law Vault/Article-Workplan.md"
verified: true
notes: "Section IX's scope-defining anchor. The workplan §3.1 is explicit that the article cannot ship without a real cost-and-labor table and enumerates exactly what the table must contain. Three downstream-consumer pending issues (PI-003 Section IV ingest line, PI-018 Section VIII deploy line, PI-042 Section VII iteration line) all forward-reference this owning section per L-027 / L-032. The 60-percent-of-weekly-Claude hand-wave that the email-to-chandler-progress.md carries (see evidence-09-sixty-percent-weekly-claude-anchor) is exactly the 'hand-wave' the workplan §3.1 calls out as insufficient, so the section's central argumentative move is replacing that single anchored number with a table that covers four labor categories and the per-phase token spend. Phase A item 2 in workplan §4 (Evidence Harvest) names the retroactive reconstruction protocol: email trail plus git log plus best-memory entries committed to Appendix-Cost-Log.md. The card scope is the spec itself, not the table; the table lands during Draft once the reconstruction completes."
---

The workplan §3.1 names the cost-and-labor table as one of the five most-important gaps to close before the article can land. The current state is a single anchored number: about 60 percent of weekly Claude usage as of the 198-page progress snapshot, with everything else (per-phase token spend, hours by labor category, hosting cost, total dollars, total person-hours) outstanding. Section IX cannot ship without replacing the hand-wave with a real table, and the workplan §3.1 enumerates exactly which columns the table must carry. The same workplan §4 Phase A item 2 names the reconstruction protocol: email trail plus git log plus best-memory entries committed to Appendix-Cost-Log.md, with prospective logging from that point forward. Three other sections already forward-reference the cost-and-labor table as their owning anchor: Section IV needs the ingest-phase line per PI-003, Section VIII needs the deploy-phase line per PI-018, and Section VII needs the iteration-phase line per PI-042. Per L-027 and L-032 those downstream consumers route through Section IX's master cost table rather than fabricating numbers inline.

Exact source quote, `Chandler Constitutional Law Vault/Article-Workplan.md` §3.1 (line 56):

> 1. **Cost and time log.** We have a hand-wave at 60% of weekly Claude usage. The article needs a real table: hours spent by category (ingest, prompt tuning, review, debugging), token spend by phase, hosting cost, total dollars, total person-hours. Start logging retroactively now (memory plus git history) and prospectively going forward.

And `Article-Workplan.md` §4 Phase A item 2 (line 73):

> - Reconstruct the cost and time log from email trail, git log, and best-memory entries; commit `Appendix-Cost-Log.md`.
