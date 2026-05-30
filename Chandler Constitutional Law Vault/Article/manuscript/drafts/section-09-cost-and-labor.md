---
section: "09"
title: "Cost and Labor: The Honest Accounting"
status: needs_polish
target_words: 700
word_count: 829
word_count_prior_run_275: 770
last_phase: draft
draft_status: needs_cite
cite_status: needs_cite
polish_status: needs_polish
footnotes_count: 16
draft_note_run330: "Mirrored polished/section-09 PI-ER-IXTABLE Draft tick at the drafts leg per L-035 three-site discipline. Body: IX.A column-set sentence re-anchored; §9.5 master Table 9.1 inserted (Article-loop ticks by phase, runs 66-329; 7-row aggregation including total row); §9.5 closer rewritten to stop saying the master table 'remains owed' and to frame token-spend and person-hours columns as structural scope rather than capture-pending. Footnotes [^3]/[^4]/[^15]/[^16] re-anchored to App. E § E.5 with in-section Table 9.1 anchors. Also caught up the App. C -> App. E re-lettering this drafts file missed at the run-326 Cite tick (footnotes [^1]/[^4]/[^7]/[^12]/[^15]/[^16] now correctly point to App. E (Cost and Time Log) matching appendix-E-cost-and-labor.md). Full draft.md propagation deferred to next Stitch tick per L-035. draft_status needs_polish -> needs_cite; provenance side held in polished frontmatter only since the drafts file does not carry the provenance fields."
evidence_cards:
  - evidence-09-workplan-cost-table-spec
  - evidence-09-sixty-percent-weekly-claude-anchor
  - evidence-09-netlify-cli-zero-build-minutes
  - evidence-09-deploy-wall-clock-fast-path
  - evidence-09-scheduled-task-cadence
  - evidence-09-credit-block-as-external-cost-signal
  - evidence-09-tiered-loading-as-token-economy
  - evidence-09-ingest-cap-as-throughput-anchor
  - evidence-09-labor-categories-workplan
  - evidence-09-downstream-consumers
---

# Section IX. Cost and Labor: The Honest Accounting

## 9.1 The accounting the article promised

An honest cost-and-labor table is essential for a method paper of this kind: without one, the cost arguments throughout Sections III, VIII, and IX read as unfalsifiable. The existing record’s single anchored figure, about sixty percent of weekly Claude usage consumed to reach the 198-page progress snapshot, is a hand-wave that does not split by phase, by labor category, or by snapshot-anchored dollar count.[^1] [^2] Section IX reports the column set the article loop’s per-tick cost log instruments (phase, ticks logged, and words generated in new or changed prose) and frames the two columns the earlier accounting promised but the log does not capture as scope rather than capture-pending.[^3] [^4]

## 9.2 Hosting cost: bounded under normal operation, blocked when credits exhaust

The deployed-site hosting bill is a two-state architectural property rather than a single number. The preferred deploy path is Netlify CLI direct upload from the scheduled task, which does not consume Netlify build minutes because the build runs in the local sandbox and only the produced assets cross the wire; the Netlify MCP fallback is demoted because it does consume build minutes.[^5] Under normal operation, the deploy phase lands at zero marginal hosting cost on the free tier. The honest hedge is the credit-block pattern: when account credits exhaust, the free-tier ceiling reasserts itself as an HTTP 403 carrying the body “Account credit usage exceeded,” and three sequential credit-block events on May 7, 2026, at 18:41Z, 19:11Z, and 19:42Z tripped the dispatcher’s three-strike guard, which skips the fast-deploy POST until human action restores credits or upgrades the tier.[^6] [^7]

## 9.3 Wall-clock and cadence anchors

Three vault-primary wall-clock figures and two cadence figures anchor the per-tick line. The fast-deploy script completes in approximately six seconds and fits inside the forty-five-second sandbox cap; the clean CLI-path deploy on the 205-page corpus logs approximately sixteen seconds build plus approximately eight seconds upload; the Step 3.5 verification budget is approximately ten to fifteen seconds across the three sub-checks (page sample, search sanity probe, source-materials sample).[^8] The full deploy-phase wall-clock floor reads as approximately twenty to forty seconds end-to-end depending on which upload path the run takes. The vault scheduled task fires every thirty minutes with an Ingest budget of three to five files per run, and the article scheduled task fires every two hours, observable in the rolling build-narrative entry timestamps.[^9] The vault Ingest cap is ten files per tick across new files and Step 8 backfills (fifteen when Steps 1 through 7 produce nothing), enforced by a *scope_discipline* score of zero (run score 4.5 instead of 5.0) when crossed.[^10]

## 9.4 Per-tick token-economy: tiered loading and per-phase rubric

The controlling per-tick token-economy mechanism is tiered context loading. Every scheduled-task run loads the project primer, the state file, and the runbook section for the current phase as Tier 1, and the current phase’s rubric, the lessons file, the current month’s build narrative, and the personas file for the adversarial review pass only as Tier 2; other rubrics and archived narratives are not loaded.[^11] The same architectural property runs in the vault scheduled task per its own runbook and tiered-loading guidance, and the cross-rubric-reading prohibition is explicit because cross-rubric loading would create both conflicting incentives at the rubric level and conflicting token-spend ceilings at the cost level. The load policy makes one tick of one phase a predictable token unit, which is the precondition for the cadence-times-per-tick-spend back-computation the master cost-table row depends on.[^12]

## 9.5 The master table, the downstream consumers, and what is still open

The four labor categories map cleanly to the system’s own phases.[^13] Ingest maps to the vault Ingest phase and the Article Harvest phase. Prompt tuning maps to the per-tick rubric-and-lessons work the author does offline, plus the Article Outline and Cite work that builds each phase’s prompt commitments. Review maps to the per-tick scorecard reads, the periodic lessons-consolidation sweep, and the Verify-phase forced-finding adversarial pass. Debugging maps to the per-tick pending-issue resolution work and the multi-tick pending-issue lifecycle the system carries across rotations.

**Table 9.1. Article-loop ticks by phase, runs 66 to 329** (source: `manuscript/cost-log.jsonl`).

| Phase | Ticks | Words generated |
|-------|------:|----------------:|
| Harvest | 36 | 26,909 |
| Outline | 25 | 15,066 |
| Draft | 38 | 19,032 |
| Cite | 40 | 13,512 |
| Polish | 37 | 15,533 |
| Stitch | 38 | 25,883 |
| Verify | 50 | 135,132 |
| **Total** | **264** | **251,067** |

Verify out-produces every other phase because words-generated counts every new or changed prose unit each tick wrote, including verify-findings and build-narrative entries, not only main-text prose. Three downstream cost-line consumers forward-reference this owning table: Section IV’s ingest line, Section VIII’s deploy line, and Section VII’s iteration line.[^14] The master table delivers the columns the cost log instruments; two omissions are scope rather than items owed. Per-tick token-level model spend is not recorded by either the article-loop log or the vault-construction logs,[^15] and a person-hours backfill across the four labor categories is not loggable by a system that records only its own runs.[^16] External pricing lookups for Anthropic API pricing, Netlify tier pricing, and metered MCP service prices remain deferred to a later citation pass.

## Footnotes

[^1]: *See infra* App. A (Vault Architecture and File Layout) (recording the cost-and-labor table as one of the five most-important gaps the article must close before it can ship, identifying the existing record’s single anchored figure as a hand-wave that does not split by phase, by labor category, or by snapshot-anchored dollar count, and naming the retroactive-reconstruction protocol as email trail plus git log plus best-memory entries committed to `Appendix-Cost-Log.md`); *see also infra* App. E (Cost and Time Log), Methodology Note (retroactive-reconstruction protocol with the four-labor-category mapping in note [^13] *infra*).

[^2]: *See infra* App. A (Vault Architecture and File Layout) (progress report to Professor Chandler at the 198-page snapshot of 92 case briefs, 27 doctrinal topic pages, and 79 lecture summaries, naming approximately sixty percent of weekly Claude usage consumed to reach that snapshot); *see also supra* Section IV (The Input Corpus) note 33 (cross-reference to the same progress-report source used as Section IV’s 198-page snapshot anchor under the article’s snapshot-and-drift convention). The anchored figure is the author’s self-reported subscription utilization at the snapshot date and does not split by phase, labor category, or dollar count, which is exactly the gap cited *supra* at note [^1] that this section closes.

[^3]: *See infra* App. E (Cost and Time Log) § E.5 (Honest Caveats), recording that the cost log’s fields at the per-tick level are run_count, phase, model, files_read, files_written, words_generated, and notes; *see also infra* Table 9.1 (in-section per-phase aggregate of the same fields across runs 66 to 329). The two non-delivered columns, per-tick token-level model spend and human review hours, are framed at notes [^15] and [^16] *infra* as structural scope rather than capture-pending items.

[^4]: *See infra* App. E (Cost and Time Log) § E.5 (recording that neither this paper’s cost log nor the vault’s run-scores records per-tick token counts, so no dollar figure for model usage can be derived from either, and that human review hours are not loggable by a system that records only its own runs); *see also infra* Table 9.1 (in-section delivery of the columns the cost log does instrument). The omission is recorded as a structural property of the logging system rather than as a defect to be repaired by retroactive reconstruction.

[^5]: *See infra* App. A (Vault Architecture and File Layout) (DEPLOY.md Step 2 designating the Netlify CLI direct-upload path as canonical specifically because it does not consume Netlify build minutes and uses the local PAT so deploys are reproducible from the scheduled task without proxy-token TTL pressure; DEPLOY.md fallback-path entry demoting the Netlify MCP `netlify-deploy-services-updater` call with `operation: deploy-site` and `siteId: f78a098b-9a9e-412a-8d4f-dd8ccda13bfe` because it consumes Netlify build minutes); *see also supra* Section VIII (From Vault to Website) note 78 (cross-reference to the same DEPLOY.md Step 2 cited in Section VIII’s build-pipeline framing of the deploy path).

[^6]: *See infra* App. A (Vault Architecture and File Layout) (vault `LESSONS.md` Deployment item 5 naming the HTTP 403 “Account credit usage exceeded” pattern as an external block rather than a code defect, recording that build still succeeds and upload aborts before any deploy record is created, and specifying the RUNBOOK guard fires after `consecutive_same_type_failures>=3` and `type=deploy-credit-blocked` to skip the fast-deploy POST until credits are restored; same entry’s Seen-record logging 2026-05-07T18:41Z, T19:11Z, and T19:42Z as the three sequential credit-block events that tripped the three-strike guard against a 281-page corpus build of 131 cases, 53 topics, and 97 lectures).

[^7]: *See infra* App. E (Cost and Time Log), tbl. 9.2 (deploy-phase line; two-state hosting framing carrying the qualitative free-tier-bounded-under-normal-operation property paired with the credit-block-when-credits-exhaust hedge, without fabricating a dollar figure for either state; in-section row reference uses local Table 9.N numbering per the convention named at note [^4] *supra*).

[^8]: *See infra* App. A (Vault Architecture and File Layout) (vault `LESSONS.md` Deployment item 1 recording that `.site/fast_deploy.py` walks `dist/`, POSTs the manifest, uploads only required bytes, and calls finalize, completing in approximately six seconds and fitting inside the forty-five-second sandbox cap; vault `CHANGELOG.md` 2026-05-01 deploy entry logging a clean CLI-path deploy at approximately sixteen seconds build plus approximately eight seconds upload on a 205-page corpus build of 100 cases, 28 topics, and 77 lectures via `netlify-cli --no-build --prod --dir .` from `.site/dist`; DEPLOY.md Step 3.5 verification budget at approximately ten to fifteen seconds total across the three sub-checks of page sample, search sanity probe, and source-materials sample, capturing the wall-clock cost in the run summary before Step 4 advances `last_deploy`). The aggregated approximately twenty-to-forty-second deploy-phase wall-clock floor is the sum of the build, upload, and verification ranges and is presented as a range rather than a point estimate, following the article’s numeric-caveat discipline for anchored-empirical-precision claims.

[^9]: *See infra* App. A (Vault Architecture and File Layout) (vault `CHANGELOG.md` line 198 documenting the vault scheduled-task cadence as a thirty-minute interval with tiered context loading and an Ingest budget of three to five files per run; Article `BUILD_NARRATIVE_2026-05.md` entry timestamps for 2026-05-19 demonstrating the two-hour article scheduled-task cadence at Cite 05:00:00Z, Polish 07:00:00Z, Stitch 11:00:00Z, and Verify 13:00:00Z, with the same two-hour spacing observable across all entries in the rolling narrative). The two cadences are the multipliers that, combined with the per-tick token-economy mechanism at note [^11] *infra*, let the master cost-table row at note [^4] *supra* back-compute weekly token spend against the [^2] sixty-percent-of-weekly-Claude anchor.

[^10]: *See infra* App. A (Vault Architecture and File Layout) (vault `LESSONS.md` Ingest combined-cap entry specifying the cap at ten across new files plus Step 8 backfills per tick, with the backfill budget equal to `max(0, 10 - new_files_count)` and the exception that when Steps 1 through 7 produce zero new files the backfill-only ceiling rises to fifteen; same entry naming the enforcement mechanism as a `scope_discipline 0` score that drops the run score from 5.0 to 4.5 when the cap is crossed; Seen-record dated 2026-04-22T18:45Z capturing the eight-new-plus-three-backfill total of eleven that triggered the red flag).

[^11]: *See infra* App. A (Vault Architecture and File Layout) (dispatcher protocol enumerating per-run loads as Tier 1 covering the state file, the rubric for the current phase, and the lessons file, with Tier 2 covering the current phase’s rubric, the lessons file, the current month’s build narrative, and the personas file only for the adversarial review pass, and naming the explicit prohibition against reading other rubrics or archived narratives; same source recording the cross-rubric-reading prohibition that each run loads only its own phase rubric because cross-rubric reading creates conflicting incentives, with the same dispatcher-protocol architecture mirrored in the vault scheduled task per its own runbook and tiered-loading guidance); *see also supra* Section VI (Prompting as Pedagogical Design) note 63 (cross-reference to the prompt-design framing of the same tiered-loading architecture as the lessons-as-prompt-iteration-memory contract).

[^12]: *See infra* App. E (Cost and Time Log), tbl. 9.3 (per-tick token-spend by phase carrying the cadence-times-per-tick-spend back-computation against the sixty-percent-of-weekly-Claude anchor at note [^2] *supra* with the cadence multipliers from note [^9] *supra* and the per-tick token-economy mechanism from note [^11] *supra*; capture pending, with the article’s numeric-caveat discipline requiring verified figures only).

[^13]: *See supra* note [^1] (enumerating ingest, prompt tuning, review, and debugging as the four labor-category columns the cost-and-labor table must carry). The body-prose mapping from the four labor categories to the system’s own phases (ingest to vault Ingest plus Article Harvest; prompt tuning to per-tick rubric-and-lessons work plus Article Outline and Cite; review to per-tick scorecard reads plus the periodic lessons-consolidation sweep plus the Verify-phase forced-finding adversarial pass; debugging to per-tick pending-issue resolution plus the multi-tick pending-issue lifecycle) is this article’s own contribution; the four-column structure comes from the source at note [^1] and this section maps it to the loop architecture Sections III through VIII develop.

[^14]: *See supra* Section IV (The Input Corpus) note 22 (Section IV ingest-line forward reference closing through this section’s master table); *see also supra* Section VII (Iterative Improvement Under Professorial Control) note 68 (Section VII iteration-line forward reference closing through this section’s master table); *see also supra* Section VIII (From Vault to Website) note 82 (Section VIII deploy-line forward reference closing through this section’s master table). The three forward references flow under the article’s single-owner-section routing convention, which assigns one owning section to any cost or throughput figure that more than one section touches.

[^15]: *See* Table 9.1 *supra* (master cost-and-labor table for the article loop). Per-tick token counts are not recorded in `manuscript/cost-log.jsonl`; the log’s per-run fields are run_count, phase, model, files_read, files_written, words_generated, and notes. *See infra* App. E (Cost and Time Log) § E.5 (recording the absence of per-tick token counts in both the article loop’s cost log and the vault’s `.run-scores.jsonl` as a structural property of the logging system, with the consequence that no dollar figure for model usage can be derived from either).

[^16]: *See infra* App. E (Cost and Time Log) § E.5 (the scheduled tasks log only their own runs, so professorial review time and the offline rubric-and-lessons-tuning work the author performs between ticks are not loggable by a system that records only its own runs, and a person-hours backfill across the four labor categories is therefore not deliverable from the system’s own records). The honest move is to name the structural limit rather than fabricate a range from sources that do not exist.
