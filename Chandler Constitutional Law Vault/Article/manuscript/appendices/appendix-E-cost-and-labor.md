---
id: appendix-E
title: "Cost and Time Log"
status: drafted
words: 773
target_min: 400
target_max: 800
last_phase: harvest-appendix
methodology_change: "Vault cost is now derived from the vault's own machine-generated logs (.run-scores.jsonl: 255 ticks; .ingested-files.jsonl: 469 ingestion records; git commit history: 69 commits on the vault path; CHANGELOG.md: milestone timeline) rather than from the 60% weekly-Claude-usage email estimate, which is a hand-wave and not metered. Replace the workplan-restated 60% figure entirely; do not include it. Do not cite email-to-chandler-progress.md as a cost source."
source_files:
  - "<vault>/Article/manuscript/cost-log.jsonl (this paper's per-tick log, 54+ ticks)"
  - "<vault>/.run-scores.jsonl (vault's per-tick scorecard, 255 ticks)"
  - "<vault>/.ingested-files.jsonl (vault ingestion log, 469 records)"
  - "<vault>/CHANGELOG.md (vault milestone timeline)"
  - "Git history: git log --oneline -- 'Chandler Constitutional Law Vault' (~69 vault commits)"
  - "<vault>/.vault-maintenance-state.json (current run_count and phase)"
---

# Appendix E: Cost and Time Log

## E.1 Method note

The scheduled task logs one machine-generated line per run to `manuscript/cost-log.jsonl`, recording the run number, phase, model, files read, files written, and an approximate count of words generated in new or changed prose. The tables below aggregate that log. They count the system’s own runs only; they are not a metered token bill (see E.5).

## E.2 Article-writing cost (this paper)

The log instruments runs 66 through 119. The 65 earlier runs predate the cost-log and are not captured here.

| Metric | Value |
|--------|------:|
| Logged ticks (runs 66 to 119) | 54 |
| Calendar window | May 23 to May 28, 2026 (6 days) |
| Words generated (new and edited) | 49,994 |
| Files read (cumulative) | 635 |
| Files written (cumulative) | 240 |
| Model | `claude-opus-4-7` (all 54 ticks) |
| Noop ticks (no prose produced) | 8 |
| Push-race losses in the logged window | 0 (run numbers 66 to 119 are contiguous) |

Per-phase breakdown of the same 54 ticks:

| Phase | Ticks | Words generated |
|-------|------:|----------------:|
| harvest | 7 | 11,969 |
| harvest-appendix | 4 | 4,300 |
| outline | 7 | 10,710 |
| draft | 8 | 4,934 |
| cite | 7 | 4,291 |
| polish | 7 | 2,188 |
| stitch | 7 | 3,264 |
| verify | 7 | 8,338 |
| **Total** | **54** | **49,994** |

The word figure exceeds the manuscript’s 10,000-to-12,000-word target because it counts every draft, evidence card, footnote block, appendix, lesson, and verify-findings run block produced across the window, not the surviving main-text prose.

## E.3 Vault-construction cost (the case study)

The vault was built by a separate scheduled task whose own machine-generated logs are the cost record. There is no token bill and no human-hour ledger; what exists is a count of automated runs and the files they touched. Earlier drafts restated an “about 60% of weekly Claude usage” figure from an email trail. That number was unmetered and is omitted here in favor of counted runs.

| Metric | Value | Source |
|--------|------:|--------|
| Build window | 2026-04-16 to 2026-05-11 (~26 days) | `CHANGELOG.md` (Initial Setup to last deploy) |
| Scored maintenance ticks | 255 | `.run-scores.jsonl` |
| Average weighted run score | 4.3 (across the 155 ticks carrying a weighted score) | `.run-scores.jsonl` |
| Ingestion-log records | 469 (1 metadata, 468 operations) | `.ingested-files.jsonl` |
| Distinct source files processed | 456 | `.ingested-files.jsonl` |
| Deployed pages (deliverable size, not cost) | 198 | Appendix A |

Ticks by phase (the vault runs an eight-phase rotation, distinct from this paper’s seven-phase loop):

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

The deploy row is the honest outlier. Of 59 deploy ticks, 43 were blocked by a Netlify “Account credit usage exceeded” response and published nothing. The construction cost therefore includes dozens of runs that advanced no deliverable, a real expense the run log records and an email estimate would have hidden.

## E.4 Hosting and infrastructure

| Item | Value |
|------|------|
| Host | Netlify free tier (zero hosting cost to date) |
| Domain | `constitutionallaw.netlify.app` subdomain (no custom-domain cost) |
| Vault size on disk | Not captured in this repository snapshot |

## E.5 Honest caveats

What the logs do not capture:

- Token-level API spend. Neither this paper’s cost-log nor the vault’s run-scores records per-tick token counts, so no dollar figure for model usage can be derived from either.
- Human review hours. The scheduled tasks log only their own runs; professorial review time is not loggable.
- Git history is not used as a vault-cost source here. The git log in this repository snapshot is the article-maintenance repository, with commits dated at clone time, not the vault’s construction history, so commit counts would mislead.
- The 198-page figure is deliverable size from Appendix A, not an effort measurement.
- Runs 1 through 65 of this paper’s loop predate its cost-log (see E.2); only runs 66 onward are instrumented.
- Cognitive time spent designing prompts and rubrics is not loggable by a system that can only record its own runs.

Cross-reference: Section IX (Cost and Labor) is the primary consumer of this appendix.
