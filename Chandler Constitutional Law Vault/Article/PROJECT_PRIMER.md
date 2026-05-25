# JLE Article — Project Primer

Compact runtime index for the article-writing scheduled task. Mirrors the vault-maintenance pattern.

## Absolute Paths

| Resource | File-tool path |
|----------|---------------|
| Vault root | `/Users/alan/Library/Mobile Documents/com~apple~CloudDocs/Projects/claude/Chandler Constitutional Law Vault` |
| Article root | `<vault>/Article/` |
| Workplan (source of truth for thesis and bibliography) | `<vault>/Article-Workplan.md` |
| Runbook | `<vault>/Article/RUNBOOK.md` |
| Rubric (one per phase) | `<vault>/Article/rubric/<phase>.md` |
| Personas (Verify) | `<vault>/Article/PERSONAS.md` |
| Lessons | `<vault>/Article/LESSONS.md` |
| State | `<vault>/Article/.article-state.json` |
| Run scorecard | `<vault>/Article/.article-scores.jsonl` |
| Build narrative (current month) | `<vault>/Article/BUILD_NARRATIVE_YYYY-MM.md` |
| Manuscript | `<vault>/Article/manuscript/` |
| Manuscript subfolders | `evidence/`, `outlines/`, `drafts/`, `footnotes/`, `polished/`, `figures/` |
| Full draft (assembled) | `<vault>/Article/manuscript/full-draft.md` |
| Abstract | `<vault>/Article/manuscript/abstract.md` |

For bash, replace the file-tool vault root with the mount path returned by `find /sessions -maxdepth 3 -name 'Chandler Constitutional Law Vault' -type d | head -1`.

## Article

**Title:** From Casebook to Course Knowledge System: AI-Assisted Synthesis, Obsidian, and the Future of Legal Pedagogy

**Target venue:** Journal of Legal Education (jle.aals.org). Bluebook 21st. Scholastica submission. No published word cap. Target raised from 10,000-12,000 to **10,000 to 14,000** on 2026-05-25 after the provenance audit surfaced under-budgeting in Sections XI (Evaluation) and XII (Risks and Limits): both sections need room to engage substantively with the literature their reviewers will hold the article against (Magesh, Bond meta-review, Mata, chatbot architecture, methodology framing). The extra 2,000 words are earmarked for those two sections; other section budgets unchanged. Plus online appendices.

**Author:** Alan Chan, with Professor Chandler review at human-in-the-loop checkpoints (see RUNBOOK gates).

**Thesis (one sentence):** Generative AI, combined with structured source materials, Obsidian-style markdown notes, retrieval from verified legal sources, and iterative expert review, can convert a law professor's dispersed course archive into a navigable, replicable course knowledge system; the Chandler Con Law I vault is the case study, and the broader contribution is the method.

**House voice:** Practitioner-scholarly. Candid. Methodologically transparent. JLE-idiomatic, not Silicon Valley. Recurring sentence: "The system did not replace professorial judgment; it made that judgment reusable, inspectable, and publishable." Use once in intro, once at the Section VII / VIII seam, once in conclusion.

## Section map

Drives `.article-state.json` per-section status fields. Numbers match `Article-Workplan.md` and Professor Chandler's outline.

| ID | Title | Drafting order | Approx target words |
|----|-------|----------------|-------------------|
| 01 | Introduction: The Hidden Archive of the Law Professor | 11 | 900 |
| 02 | Why Ordinary Course Infrastructure Is Not Enough | 7 | 700 |
| 03 | Case Study: A Constitutional-Law Knowledge System | 2 | 1200 |
| 04 | The Input Corpus | 1 | 900 |
| 05 | Building the Obsidian Vault | 1 | 1100 |
| 06 | Prompting as Pedagogical Design | 4 | 800 |
| 07 | Iterative Improvement Under Professorial Control | 5 | 1100 |
| 08 | From Vault to Website | 1 | 700 |
| 09 | Cost and Labor: The Honest Accounting | 6 | 700 |
| 10 | Generalization Beyond Constitutional Law | 12 | 900 |
| 11 | Evaluation: What Would Count as Success | 8 | 1200 |
| 12 | Risks and Limits | 9 | 1400 |
| 13 | Institutional Implications | 10 | 500 |
| 14 | Conclusion | 13 | 400 |

Total target: ~12,500 words (was 11,600; +900 from Sections XI/XII rebudget). Stitch phase enforces **10,000 to 14,000** range (raised from 12,000 on 2026-05-25). The earmark discipline: the extra 2,000 words of ceiling are reserved for Sections XI and XII's deeper literature engagement; other sections should not expand to absorb the slack. If a non-XI/XII section grows past its original target by more than 10%, the next Polish/Stitch pass trims it back.

## Phase rotation

Harvest -> Outline -> Draft -> Cite -> Polish -> Stitch -> Verify -> repeat

One phase per scheduled run. Phase advancement is automatic in `.article-state.json` unless a gate is set.

## Gates

Only one human-in-the-loop gate is configured: **submission package**. When Stitch reports word count in range and Verify reports zero new findings on a full read-through, the state file flips `gates.submission_ready` to `true` and the dispatcher stops advancing phases until a human clears it. The system never auto-submits.

## Vault sources to mine (Harvest)

- `<vault>/Article-Workplan.md` (thesis, outline, bibliography, recommendations)
- `<vault>/email-to-chandler-progress.md` and `<vault>/email-to-chandler-stages.md` (live update narrative)
- `<vault>/archive/vault-blog-post-draft.md` (Prize Cases story, token problem story; raw, mine quotes)
- `<vault>/PROJECT_PRIMER.md` (vault architecture)
- `<vault>/LESSONS.md` and `<vault>/archive/LESSONS_*.md` (iteration record)
- `<vault>/rubric/*.md` (the vault rubrics inform Section VI/VII)
- `<vault>/Templates/` (Obsidian note schemas, for Appendix C)
- `<vault>/Cases/`, `<vault>/Topics/`, `<vault>/Lectures/` (sample pages for Section III screenshots and quotations)
- `<vault>/Source Materials/` (input corpus inventory for Section IV and Appendix A)

## Citation policy

- Every factual claim, statistic, quotation, or attributed argument requires a footnote.
- Footnotes link to primary sources (court opinions, original papers, original tweets/posts with archive links if possible).
- No "personal communication" or "internal log" cites in published text; convert to appendix excerpts.
- Bluebook 21st form. Cite-checker phase verifies form and URL liveness.
- Karpathy figures: use only the verified 50 experiments overnight per the autoresearch repository (March 7, 2026); never assert "700 experiments" or "11% efficiency gain" without a primary source.

## Conventions

- Every section file opens with YAML frontmatter (id, title, status, word_count, last_phase).
- Filenames: `section-NN-shortslug.md`, `evidence-NN-shortslug.md`, `outline-NN-shortslug.md`.
- No straight ASCII quotes in published prose; convert to curly. Run conversion in Polish.
- No em dashes in published prose; rewrite or use commas, parentheses, or semicolons. Polish enforces this.
- Internal cross-references between sections use `[[section-NN]]` style; resolved to footnote or inline reference in Polish.

## Do Not Touch

- `<vault>/Article-Workplan.md` is the human-edited source of truth for thesis, scope, and bibliography. The scheduled task may read it but may not modify it.
- `<vault>/Article/manuscript/full-draft.md` is assembled in Stitch only; other phases write to `drafts/section-NN-*.md`.
- Never fabricate quotations, citations, or empirical figures. If a needed fact is not in the vault and not on the web, log to `pending_issues` in state.
- The system never submits and never emails the professor. Both are explicit human actions.
