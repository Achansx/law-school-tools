---
id: appendix-E
title: "Cost and Time Log"
status: drafted
words: 470
target_min: 400
target_max: 800
last_phase: harvest-appendix
methodology_change: "Appendix costs the VAULT (the deliverable), not the writing of this paper. Vault cost is derived from the vault's own machine-generated logs (.run-scores.jsonl: 255 scored ticks; .ingested-files.jsonl: 469 ingestion records; CHANGELOG.md: milestone timeline) rather than the unmetered '~60% of weekly Claude usage' email estimate, which is omitted. The cost of the autonomous loop that produced the paper itself is incidental to the method the article evaluates and is not costed here."
source_files:
  - "<vault>/.run-scores.jsonl (vault's per-tick scorecard, 255 ticks)"
  - "<vault>/.ingested-files.jsonl (vault ingestion log, 469 records)"
  - "<vault>/CHANGELOG.md (vault milestone timeline)"
  - "<vault>/.vault-maintenance-state.json (current run_count and phase)"
---

# Appendix E: Cost and Time Log

## E.1 Method note

This appendix reports the cost of building the **vault** — the course-knowledge system that is the article's deliverable — not the cost of writing this paper. The vault was produced by a scheduled task that logs one machine-generated line per run to its own scorecard (`.run-scores.jsonl`), recording the run's phase, score, and the files it touched. The figures below aggregate those logs. They count automated runs and the files they processed; they are not a metered token bill and not a human-hour ledger (see E.4). An earlier draft restated an "about 60% of weekly Claude usage" figure from an email trail; that number was unmetered and is omitted here in favor of counted runs.

## E.2 Vault-construction cost

| Metric | Value | Source |
|--------|------:|--------|
| Build window | April 16 to May 8, 2026 (~3 weeks) | `.run-scores.jsonl` (first to last scored tick) |
| Scored maintenance ticks | 255 | `.run-scores.jsonl` |
| Average weighted run score | 4.3 (across the 155 ticks carrying a weighted score) | `.run-scores.jsonl` |
| Ingestion-log records | 469 (1 metadata, 468 operations) | `.ingested-files.jsonl` |
| Distinct source files processed | 456 | `.ingested-files.jsonl` |
| Deployed pages (deliverable size, not cost) | 198 | Appendix A |

Ticks by phase (the vault runs an eight-phase rotation, distinct from this paper's seven-phase loop):

| Phase | Ticks |
|-------|------:|
| ingest | 35 |
| lint | 34 |
| enrich | 24 |
| expand | 29 |
| synthesize | 30 |
| verify | 34 |
| consolidate | 10 |
| deploy | 59 |
| **Total** | **255** |

The deploy row is the honest outlier. Of 59 deploy ticks, 43 were blocked by a Netlify "Account credit usage exceeded" response and published nothing. The construction cost therefore includes dozens of runs that advanced no deliverable — a real expense the run log records and an email estimate would have hidden.

## E.3 Hosting and infrastructure

| Item | Value |
|------|------|
| Host | Netlify free tier (zero hosting cost to date) |
| Domain | `constitutionallaw.netlify.app` subdomain (no custom-domain cost) |
| Vault size on disk | Not captured in this repository snapshot |

## E.4 Honest caveats

What the logs do not capture:

- Token-level API spend. The vault's run-scores do not record per-tick token counts, so no dollar figure for model usage can be derived from them.
- Human review hours. The scheduled task logs only its own runs; professorial review time is not loggable.
- The 198-page figure is deliverable size from Appendix A, not an effort measurement.
- Cognitive time spent designing prompts and rubrics is not loggable by a system that can only record its own runs.
- The autonomous loop that produced this paper is not costed here; it is incidental to the method the article evaluates, and the per-run token cost of either loop was never metered.

Cross-reference: Section IX (Cost and Labor) is the primary consumer of this appendix.
