---
id: appendix-E
title: "Cost and Time Log"
status: none
words: 0
target_min: 400
target_max: 800
last_phase: none
source_files:
  - "<vault>/Article/manuscript/cost-log.jsonl (this paper's per-tick log)"
  - "<vault>/.run-scores.jsonl (vault's per-tick scores)"
  - "Git history of the vault repo (proxy for human time on commits)"
  - "Claude usage dashboard exports (if available)"
---

# Appendix E: Cost and Time Log

<!-- TODO (Harvest appendix tick): Aggregate the cost-log.jsonl into reader-friendly tables. The cost-log already contains the raw data; this appendix wraps it in prose and totals.

Structure:

## E.1 Method note (1 paragraph)

Explain that the system logged every tick (run, phase, files read/written, words generated, model used) into manuscript/cost-log.jsonl. The data shown here is aggregated from that machine-generated log.

## E.2 Article writing cost (this paper)

Table from cost-log.jsonl aggregations:

| Metric | Value |
|--------|------:|
| Total ticks (runs) | (computed) |
| Calendar days | (computed) |
| Total words generated (new + edited) | (sum of words_generated) |
| Total files read | (sum) |
| Total files written | (sum) |
| Models used | claude-opus-4-7 (and any others) |
| Hand-fired vs cron-fired | (split) |
| Push-race conflicts (lost ticks) | (count from build narrative) |

## E.3 Vault construction cost (the case study)

For the Constitutional Law vault:
- Roughly 60% of weekly Claude usage over the build period (per email-to-chandler-progress.md)
- Hand-categorized by build phase (Ingest, Enrich, Verify, Deploy) from git log and run-scores.jsonl
- Hours of human review by category (best estimate from email trail + LESSONS dates)

## E.4 Hosting and infrastructure

- Netlify free tier (zero hosting cost to date)
- Domain (or netlify.app subdomain): N/A or cost
- Storage: vault size in MB

## E.5 Honest caveats

What the cost log does NOT capture:
- Token-level API spend (we have run counts, not per-tick token counts)
- Cognitive time spent thinking about prompts (the system can only log its own runs)
- Stranded work on session branches (early-period before the push-to-master fix)

Footnote anchors: Section IX (Cost and Labor) is the primary consumer of this appendix.
-->
