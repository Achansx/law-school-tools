# Rubric: Appendix

Score each criterion 1 to 5. Apply when a Harvest tick is working on an appendix instead of section evidence.

Appendices are **reference material**, not argument prose. The scoring reflects that — different criteria than the main-text section rubrics.

## 1. Source fidelity

- 1: Content contradicts the vault/system reality or invents items.
- 3: Mostly correct but with gaps or unverified items.
- 5: Every entry sourced from a concrete file, config, log, or artifact; entries marked with their provenance.

## 2. Completeness

- 1: Major categories of relevant items missing.
- 3: Coverage uneven; some categories thorough, others sketchy.
- 5: All known items in scope are listed; explicit "intentionally excluded" note for anything left out.

## 3. Replicability

- 1: A reader could not use this appendix to reproduce the method.
- 3: Reader could partially reproduce; some steps require guessing.
- 5: A faculty member at another institution could follow this appendix and reproduce the method end-to-end.

## 4. Reference usability

- 1: Long unstructured prose; reader cannot scan for the item they need.
- 3: Some structure (headings, tables) but inconsistent.
- 5: Consistent structure (tables, code blocks, named subsections); scannable; cross-references to main-text footnotes resolve.

## 5. Word discipline

- 1: Padded with explanatory prose that belongs in the main text.
- 3: Mostly tight; a few discursive paragraphs.
- 5: Lists, tables, and code blocks dominate; prose is captions and 1-2 sentence introductions only. No argument; no thesis-restating.

## Exit conditions

- `status: drafted` when all five criteria score >= 4 and word count is within the appendix's target range.
- `status: polished` after a Polish pass converts straight quotes/em dashes and tightens captions.
- Appendices do NOT participate in the main-text word count gate. They count as separate online supplements per JLE submission practice.

## Appendix targets (approximate word ranges)

| ID | Title | Target words | Source |
|----|-------|--------------|--------|
| A  | Input Inventory | 400-700 | Vault Source Materials counts, MISSING_SOURCE_MATERIALS.md |
| B  | AI Tooling — Prompts, Skills, and Plugins | 1200-1800 | Vault rubrics/LESSONS, scheduled-task configs, plugin manifests, MCP connectors |
| C  | Obsidian Note Templates | 500-900 | Vault Templates/ folder, frontmatter schemas |
| D  | Karpathy-Loop Per-Phase Rubric | 600-1000 | rubric/*.md (compiled with intro) |
| E  | Cost and Time Log | 400-800 | manuscript/cost-log.jsonl (aggregated with prose wrapper) |
| F  | Technical Setup | 500-800 | .site/build.py, DEPLOY.md, Netlify config |

Total appendix words: ~3,600-6,000. Not counted against main-text 10k-12k ceiling.
