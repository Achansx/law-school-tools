---
section: "09"
title: "Cost and Labor: The Honest Accounting"
status: needs_polish
target_words: 700
word_count: 768
word_count_prior_run_353: 829
word_count_prior_run_275: 770
last_phase: draft
last_draft_run: 353
last_draft_at: 2026-05-31T09:00:00Z
draft_status: needs_cite
cite_status: needs_cite
polish_status: needs_polish
footnotes_count: 14
footnotes_count_prior_run_353: 16
draft_note_run353: "Mirrored polished/section-09 PI-ER2-VAULTCOST Draft tick at the drafts leg per L-035 three-site discipline. Body: §IX completely reframed from article-writing-loop cost to vault-construction cost per the runbook PROVENANCE-CORRECTION PASS PI-ER2-VAULTCOST directive (substantial standalone rewrite). §9.1 unfalsifiability opener re-pointed at vault cost (the case study is the vault); §9.2 retitled 'Deploy cost' (vault deploy phase); §9.3 NEW subsection delivering the verified vault facts (255 runs over Apr 16-May 8 2026, 22 days; ingest 35 / enrich 24 / expand 29 / synthesize 30 / lint 34 / verify 34 / consolidate 10 / deploy 59; 198pp at ~92% coverage = 92 briefs + 27 topics + 79 lectures; only 6/255 runs logged wall-clock so NO compute-hours and NO dollar figure); §9.4 tightened (dropped the article-loop-parallel sentence); §9.5 new Table 9.1 (vault-construction ticks by phase, replacing the old article-loop runs-66-329 Table 9.1) plus reframed four-labor-category mapping to vault's eight-phase rotation. Footnotes [^1]-[^14] new structure: drops the old [^7] (App. E tbl. 9.2 deploy-line), [^8] (App. F fast-deploy wall-clock figures), [^9] (App. E cadence figures), [^10] (App. D Ingest-cap), [^12] (App. E tbl. 9.3 token-spend back-computation), [^15] (Table 9.1 cost-log fields with PI-266 literal-filename leak); adds NEW [^2] (article-writing-loop log -> packet companion 04-How-This-Article-Was-Written), [^6] (App. E § E.3 vault-tick-total source with per-phase sums), [^8] (6-of-255-wall-clock caveat), [^12] (deploy-row outlier source). Net footnotes 16 -> 14. PI-266 (Table 9.1 caption + [^15] literal-filename leak) closed by the new prose. Word count 829 -> 768 prose (-7.4%, within +10% rubric band of 770). Mechanical hygiene clean (zero em dashes, zero straight ASCII doubles, zero straight ASCII apostrophes; curly throughout). Full draft.md propagation deferred to next Stitch tick per L-035. draft_status holds at needs_cite (the new prose carries new internal forward references the next Cite tick verifies); polish_status held at needs_polish. provenance side held in polished frontmatter only since the drafts file does not carry the provenance fields."
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

## 9.1 The cost the case study can claim

An honest cost-and-labor table is essential for a method paper: without one, the architectural claims in Sections III, VIII, and X read as unfalsifiable. The case study is the vault, so the costs Section IX reports are the vault’s, not this article’s; the article-writing loop that produced this paper was a comparable scheduled-task system whose log lives in a companion note.[^1] [^2] The vault’s record supports a counted tick total over a counted calendar window with a counted deliverable, and it does not support a compute-hours or dollar figure; what follows reports the column the record instruments and names what it does not.[^3]

## 9.2 Deploy cost: bounded under normal operation, blocked when credits exhaust

The deployed-site hosting bill is a two-state architectural property rather than a single number. The preferred deploy path is Netlify CLI direct upload from the scheduled task, which does not consume Netlify build minutes because the build runs in the local sandbox and only the produced assets cross the wire; the Netlify MCP fallback is demoted because it does consume build minutes.[^4] Under normal operation, the deploy phase lands at zero marginal hosting cost on the free tier. The honest hedge is the credit-block pattern: when account credits exhaust, the free-tier ceiling reasserts itself as an HTTP 403 carrying the body “Account credit usage exceeded,” and three sequential credit-block events on May 7, 2026, at 18:41Z, 19:11Z, and 19:42Z tripped the dispatcher’s three-strike guard, which skips the fast-deploy POST until human action restores credits or upgrades the tier.[^5]

## 9.3 What the vault’s run log counts and what it does not

The vault scheduled task logs one line per run to its run-scores log. Across the snapshot window of April 16 to May 8, 2026 (twenty-two calendar days), the log records 255 runs, distributed by phase as ingest 35, enrich 24, expand 29, synthesize 30, lint 34, verify 34, consolidate 10, and deploy 59.[^6] The deliverable at the end of the window is 198 pages at approximately ninety-two percent coverage of the doctrinal scope: 92 case briefs, 27 doctrinal topic pages, and 79 lecture summaries.[^7] The log does not record the cost most readers want to see: only six of the 255 runs carry a wall-clock field, and none carry token counts or a price. Section IX therefore reports no compute-hours and no dollar figure, and frames the absence as a structural property of the logging system rather than a defect to be repaired.[^8]

## 9.4 Per-tick token-economy: tiered loading and per-phase rubric

The controlling per-tick token-economy mechanism is tiered context loading. Every scheduled-task run loads the project primer, the state file, and the runbook section for the current phase as Tier 1, and the current phase’s rubric, the lessons file, the current month’s build narrative, and the personas file for the adversarial review pass only as Tier 2; other rubrics and archived narratives are not loaded.[^9] The cross-rubric-reading prohibition is explicit, because cross-rubric loading creates conflicting incentives. The load policy makes one tick of one phase a predictable unit of work, but the predictability does not become a token bill without instrumentation neither scheduled task carries.[^10]

## 9.5 The master table, the downstream consumers, and what is still open

The four labor categories map cleanly to the vault’s own phases.[^11] Ingest maps to the vault Ingest phase. Prompt tuning maps to the per-tick rubric-and-lessons work the author performs offline, plus the synthesize and consolidate phases that build each iteration’s prompt commitments. Review maps to the per-tick scorecard reads, the periodic lessons-consolidation sweep, and the vault’s verify phase. Debugging maps to the per-tick pending-issue resolution work and the multi-tick pending-issue lifecycle the scheduled task carries across rotations.

**Table 9.1. Vault-construction ticks by phase, April 16 to May 8, 2026** (source: the vault scheduled task’s run-scores log).

| Phase | Ticks |
|-------|------:|
| Ingest | 35 |
| Enrich | 24 |
| Expand | 29 |
| Synthesize | 30 |
| Lint | 34 |
| Verify | 34 |
| Consolidate | 10 |
| Deploy | 59 |
| **Total** | **255** |

The deploy row is the honest outlier: a substantial fraction of the fifty-nine deploy ticks were absorbed by the credit-block pattern named at IX.B, an expense the run log records and an email estimate would have hidden.[^12] Three downstream cost-line consumers forward-reference this owning table: Section IV’s ingest line, Section VIII’s deploy line, and Section VII’s iteration line.[^13] The master table delivers the column the run log instruments; two omissions are scope rather than items owed. Per-tick token-level model spend is not recorded, and a person-hours backfill across the four labor categories is not loggable by a system that records only its own runs.[^14] External pricing lookups for Netlify and metered MCP services remain deferred to a later Cite pass.

## Footnotes

[^1]: *See infra* App. E (Cost and Time Log), Methodology Note (recording the cost-and-labor table as one of the gaps the article must close before it can ship, and identifying the prior anchored figure of approximately sixty percent of weekly Claude usage to the 198-page progress snapshot as a hand-wave that did not split by phase, by labor category, or by dollar count); the table this section reports is the counted-runs reconstruction the appendix’s methodology note describes. The four-labor-category mapping at note [^11] *infra*.

[^2]: *See infra* App. E (Cost and Time Log), Methodology Note (recording that this paper was produced by a comparable article-writing scheduled task whose own per-tick log is the source for the companion document `04-How-This-Article-Was-Written` in the submission packet; the article-writing-loop figures are not reproduced in Section IX because the case study the article describes is the vault, not the article, and conflating the two costs would mislead the reader about which deliverable the cost record describes).

[^3]: *See infra* App. E (Cost and Time Log) § E.3 (Vault-Construction Cost), recording that the vault scheduled task’s run-scores log carries per-run fields for run_count, phase, weighted score, and (sparsely) wall-clock; *see also infra* Table 9.1 (in-section per-phase aggregate across the snapshot window of April 16 to May 8, 2026).

[^4]: *See infra* App. F (Technical Setup) (DEPLOY.md Step 2 designating the Netlify CLI direct-upload path as canonical specifically because it does not consume Netlify build minutes and uses the local PAT so deploys are reproducible from the scheduled task without proxy-token TTL pressure; DEPLOY.md fallback-path entry demoting the Netlify MCP `netlify-deploy-services-updater` call with `operation: deploy-site` and `siteId: f78a098b-9a9e-412a-8d4f-dd8ccda13bfe` because it consumes Netlify build minutes); *see also supra* Section VIII (From Vault to Website) note 78 (cross-reference to the same DEPLOY.md Step 2 cited in Section VIII’s build-pipeline framing of the deploy path).

[^5]: *See infra* App. F (Technical Setup) (vault deployment-lessons record naming the HTTP 403 “Account credit usage exceeded” pattern as an external block rather than a code defect, recording that build still succeeds and upload aborts before any deploy record is created, and specifying the RUNBOOK guard fires after `consecutive_same_type_failures>=3` and `type=deploy-credit-blocked` to skip the fast-deploy POST until credits are restored; same record logging 2026-05-07T18:41Z, T19:11Z, and T19:42Z as the three sequential credit-block events that tripped the three-strike guard against a 281-page corpus build of 131 cases, 53 topics, and 97 lectures).

[^6]: *See infra* App. E (Cost and Time Log) § E.3 (vault-construction tick total of 255 across the eight phases listed in the body, derived from the vault scheduled task’s run-scores log filtered to the snapshot window of April 16 to May 8, 2026, with per-phase sums verified at the cell level: ingest 35, enrich 24, expand 29, synthesize 30, lint 34, verify 34, consolidate 10, deploy 59); *see also infra* Table 9.1 (in-section per-phase aggregate of the same figures).

[^7]: *See supra* Section IV (The Input Corpus) note 33 (198-page snapshot of 92 case briefs, 27 doctrinal topic pages, and 79 lecture summaries as the end-of-window deliverable, used as Section IV’s input-corpus anchor under the article’s snapshot-and-drift convention); *see also infra* App. A (Input Inventory), Vault Output Snapshot subsection (same figures with the page-count breakdown and the approximately ninety-two-percent doctrinal-coverage estimate).

[^8]: *See infra* App. E (Cost and Time Log) § E.5 (Honest Caveats), recording that only six of the 255 vault runs logged a wall-clock field and that none logged token counts or a price, so no dollar figure for model usage and no compute-hours figure can be derived from the run record; *see also infra* Table 9.1. The omission is recorded as a structural property of the logging system rather than as a defect to be repaired by retroactive reconstruction.

[^9]: *See infra* App. D (Karpathy-Loop Per-Phase Rubric) (dispatcher protocol enumerating per-run loads as Tier 1 covering the state file, the rubric for the current phase, and the lessons file, with Tier 2 covering the current phase’s rubric, the lessons file, the current month’s build narrative, and the personas file only for the adversarial review pass, and naming the explicit prohibition against reading other rubrics or archived narratives; same source recording the cross-rubric-reading prohibition that each run loads only its own phase rubric because cross-rubric reading creates conflicting incentives, with the same dispatcher-protocol architecture mirrored in the article-writing scheduled task per its own runbook and tiered-loading guidance); *see also supra* Section VI (Prompting as Pedagogical Design) note 63 (cross-reference to the prompt-design framing of the same tiered-loading architecture as the lessons-as-prompt-iteration-memory contract).

[^10]: *See infra* App. E (Cost and Time Log) § E.5 (recording that the per-tick token-economy mechanism at note [^9] *supra* makes one tick of one phase a predictable unit of loading work, but does not become a token bill without per-tick token instrumentation that neither scheduled task carries; the omission is recorded as a structural property of the logging system rather than as a defect to be repaired).

[^11]: *See supra* note [^1] (enumerating ingest, prompt tuning, review, and debugging as the four labor-category columns the cost-and-labor table must carry). The body-prose mapping from the four labor categories to the vault’s own eight-phase rotation (ingest to vault Ingest; prompt tuning to per-tick rubric-and-lessons work plus the synthesize and consolidate phases; review to per-tick scorecard reads plus the periodic lessons-consolidation sweep plus the vault’s verify phase; debugging to per-tick pending-issue resolution plus the multi-tick pending-issue lifecycle) is this article’s own contribution; the four-column structure comes from the source at note [^1] and this section maps it to the loop architecture Sections III through VIII develop.

[^12]: *See supra* note [^5] (recording the three sequential credit-block events on May 7, 2026 that tripped the dispatcher’s three-strike guard); *see also infra* App. E (Cost and Time Log) § E.3 (recording that of fifty-nine deploy ticks in the snapshot window, a substantial fraction were absorbed by the credit-block pattern, a real cost the run log records and an email estimate would have hidden).

[^13]: *See supra* Section IV (The Input Corpus) note 22 (Section IV ingest-line forward reference closing through this section’s master table); *see also supra* Section VII (Iterative Improvement Under Professorial Control) note 68 (Section VII iteration-line forward reference closing through this section’s master table); *see also supra* Section VIII (From Vault to Website) note 82 (Section VIII deploy-line forward reference closing through this section’s master table). The three forward references flow under the article’s single-owner-section routing convention, which assigns one owning section to any cost or throughput figure that more than one section touches.

[^14]: *See infra* App. E (Cost and Time Log) § E.5 (the vault scheduled task logs only its own runs, so professorial review time and the offline rubric-and-lessons-tuning work the author performs between ticks are not loggable, and a person-hours backfill across the four labor categories is therefore not deliverable from the system’s own records). The honest move is to name the structural limit rather than fabricate a range from sources that do not exist.
