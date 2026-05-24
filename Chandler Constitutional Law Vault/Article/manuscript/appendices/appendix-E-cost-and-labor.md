---
id: appendix-E
title: "Cost and Time Log"
status: needs_work
words: 624
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

The case-study figures come from `email-to-chandler-progress.md` as restated in `Article-Workplan.md`; that file is not present in this repository snapshot, so the numbers below are reproduced from the workplan rather than recomputed.

| Item | Value | Provenance |
|------|------|-----------|
| Claude usage to reach 198 pages | ~60% of weekly usage over the build period | Workplan §3.1 (self-described as a hand-wave estimate, not metered) |
| Deployed pages | 198 (92 case briefs, 27 topic pages, 79 lecture summaries) | Workplan §1 |
| Input corpus | 61 PowerPoint decks, 66 reading PDFs (388 files counting all subfolders) | Appendix A |
| Build phases | Ingest, Enrich, Verify, Deploy | Workplan §3.1 |
| Human review hours by phase | Not captured in any in-repo log | email trail (absent) |

## E.4 Hosting and infrastructure

| Item | Value |
|------|------|
| Host | Netlify free tier (zero hosting cost to date) |
| Domain | `constitutionallaw.netlify.app` subdomain (no custom-domain cost) |
| Vault size on disk | Not captured in this repository snapshot |

## E.5 Honest caveats

What the cost log does not capture:

- Token-level API spend. The log records run counts and word counts, not per-tick token counts, so no dollar figure for model usage can be derived from it.
- The 60% case-study figure is an estimate from the email trail, not a metered measurement, and the workplan flags it as such.
- Runs 1 through 65 predate the cost-log; only runs 66 through 119 are instrumented.
- The vault-construction source files (`email-to-chandler-progress.md`, `.run-scores.jsonl`) are absent from this repository snapshot; E.3 reproduces the workplan’s restatement rather than the primary log.
- Cognitive time spent designing prompts is not loggable by a system that can only record its own runs.
- Stranded work on early session branches, before the push-to-master fix, is not represented in the contiguous run sequence.

Cross-reference: Section IX (Cost and Labor) is the primary consumer of this appendix.
