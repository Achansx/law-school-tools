# Con Law I Wiki — Project Primer

Compact runtime index. The scheduled-task prompt loads this plus `RUNBOOK.md` and the current month's `BUILD_NARRATIVE` only when a phase needs them.

## Absolute Paths

| Resource | File-tool path |
|----------|---------------|
| Vault root | `/Users/alan/Library/Mobile Documents/com~apple~CloudDocs/Projects/claude/Chandler Constitutional Law Vault` |
| Templates | `<vault>/Templates/` |
| Source Materials | `<vault>/Source Materials/` |
| Runbook | `<vault>/RUNBOOK.md` |
| Rubric (one per phase) | `<vault>/rubric/<phase>.md` |
| Personas (Verify) | `<vault>/PERSONAS.md` |
| Lessons | `<vault>/LESSONS.md` |
| State | `<vault>/.vault-maintenance-state.json` |
| Ingestion manifest | `<vault>/.ingested-files.json` |
| Run scorecard | `<vault>/.run-scores.jsonl` |
| Changelog | `<vault>/CHANGELOG.md` |
| Build narrative (current month) | `<vault>/BUILD_NARRATIVE_YYYY-MM.md` |

For bash, replace the file-tool vault root with the mount path returned by `find /sessions -maxdepth 3 -name 'Chandler Constitutional Law Vault' -type d | head -1`.

## Course

Professor Chandler, Constitutional Law I (Spring 2026). Structural constitution: judicial review, federalism, separation of powers, commerce clause, executive power, justiciability, preemption, state sovereign immunity, Reconstruction amendments, substantive due process, equal protection, First Amendment, Second Amendment.

## Vault Structure

- `Cases/` — one file per case, follows `Templates/Case Brief.md` (9-section case-briefer standard)
- `Topics/` — doctrine/concept pages, follows `Templates/Topic Page.md`
- `Lectures/` — lecture and class-recap summaries, follows `Templates/Lecture Summary.md`
- `Templates/` — page templates (schema source of truth)
- `Source Materials/` — read-only corpus (PDFs, PPTXs, `Uploaded Media/`)
- `rubric/` — per-phase scoring rubrics (one file per phase)
- `archive/` — rotated older files (narratives, legacy rubrics)

## File Naming

- Cases: `Cases/Case Name v Party (Year).md` (e.g., `Cases/Marbury v Madison (1803).md`)
- Topics: `Topics/Topic Name.md`
- Lectures: `Lectures/Lecture Title.md`

H1 and `case_name` frontmatter must match the filename convention: no periods, "and" not "&".

## Conventions

- Every page opens with YAML frontmatter delimited by `---`, before the H1.
- One H1 per file (matches filename minus `.md`).
- H2 sections follow template order.
- Wiki-links: `[[folder/filename|Display Text]]`.
- Tags: lowercase-hyphenated, placed at file end before the final `---`.
- Section separators: `---` with blank lines above and below.
- Case briefs scale the 9-section standard by importance.

## Frontmatter Schemas

Canonical definitions live in `Templates/`. Quick reference in `RUNBOOK.md` under "Frontmatter (canonical)".

## Phase Rotation

Ingest -> Lint -> Enrich -> Expand -> Synthesize -> Verify -> repeat

## Legal Research Tools (brief)

- Midpage: `analyzeOpinion`, `findInOpinion`, `search`. Required for Ingest case briefs and Verify spot-checks.
- CourtListener: `find_cited_cases`, `find_citing_cases`, `search_case_law`. Used for Expand and Synthesize citation chains.

Full guidance and fallback patterns live in `RUNBOOK.md` and `LESSONS.md`.

## Do Not Touch

- `Source Materials/` is read-only.
- Never delete wiki content; only add, fix structure, or flag.
- Do not create pages solely to satisfy orphan links; log them instead.
- Do not rename files or change H1s without explicit instruction.
- Never fabricate case details; log to `pending_issues` if sources are insufficient.
