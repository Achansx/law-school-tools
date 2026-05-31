---
id: appendix-A
title: "Input Inventory"
status: drafted
words: 545
target_min: 400
target_max: 700
last_phase: harvest-appendix
source_files:
  - "<vault>/Source Materials/"
  - "<vault>/MISSING_SOURCE_MATERIALS.md"
  - "<vault>/Templates/"
---

# Appendix A: Input Inventory

This appendix inventories the corpus the system ingested. All counts come from a filesystem audit of the Canvas LMS export taken on 2026-05-15 and recorded in the Section IV and V evidence cards; the headline 61/66 figure is corroborated by `Article-Workplan.md`. The course is Professor Chandler’s Constitutional Law I (Spring 2026), whose syllabus covers the structural constitution.

## A.1 Source Materials Provided

The export arrived as a flat folder. At the top level it held 61 PowerPoint decks (.pptx) and 66 reading PDFs, the 127 slide-and-reading files the flat structure exposed first, plus 3 .docx, one .txt, and one .potx template. Counting every subfolder, the export totals 388 files, with no organization beyond filenames.

| Location | Category | Count |
|----------|----------|------:|
| Top level | PowerPoint decks (.pptx) | 61 |
| Top level | Reading PDFs (.pdf) | 66 |
| Top level | Word documents (.docx) | 3 |
| Top level | Other (.txt, .potx) | 2 |
| Uploaded Media/ | Individual case-opinion PDFs | 135 |
| Uploaded Media/ | Merged reading packets (`merged-*.pdf`) | 12 |
| resources/ | Exported LMS HTML files | 81 |
| unfiled/ | Stray files (`Midterm_Rubric.pdf`) | 1 |
| All subfolders | Total | 388 |

Assessment artifacts. Four files encode professorial judgment about what counts as a complete answer: `Final Exam Constitutional Law Fall 2023.pdf`, `Constitutional Law Final Exam Spring 2025 (Reduced).pdf`, `TEFA_Exam_Question.docx.pdf`, and `Midterm_Rubric.pdf`.

Modernized opinions. Thirty-seven files carry a `modernized` tag (for example, `mcculloch_modernized.pdf` and `youngstown-modernized.pdf`): professor-edited versions that update archaic phrasing for student readers. These are the most pedagogically useful and the most error-prone intake type, because a silent edit can drift from the indexed opinion (see Section VII and Appendix D).

## A.2 Categories Intentionally Excluded

- Copyrighted casebook excerpts. The corpus is drawn from Professor Chandler’s own course materials; casebook text was not a source (the author’s understanding, pending the professor’s confirmation). Ten assigned opinions accordingly have vault briefs but no source PDF on disk (see below).
- Student work product — graded submissions and exam answers (privacy/IRB). One boundary case: review-session materials prepared by teaching assistants *are* part of the ingested corpus, but they are TA-authored teaching aids, not student submissions, so they raise an authorship-attribution note rather than a student-privacy concern.
- Office-hours notes (privacy).
- Anything that would require a separate IRB review.

Absent by inheritance, not by choice. Ten foundational Supreme Court opinions have vault briefs but no source file on disk, because students read them in the assigned casebook rather than from a course-issued PDF: Cohens v Virginia (1821), United States v Cruikshank (1876), Wickard v Filburn (1942), Adamson v California (1947), Baker v Carr (1962), USDA v Moreno (1973), South Dakota v Dole (1987), United States v Lopez (1995), United States v Morrison (2000), and Hamdi v Rumsfeld (2004). The corpus is bounded by what the LMS captured, not by what the syllabus assigned.

## A.3 Source Material Conventions

Intake naming. The export enforced no filename convention; hyphens, underscores, spaces, parenthetical years, and mixed case appear in arbitrary combinations within one folder. The vault imposes a three-way invariant on intake: the filename stem, the H1, and the frontmatter name field must agree, with no periods (“v Madison,” not “v. Madison”) and “and” rather than the ampersand.

Categorization. Each ingested file is typed into one of three content folders (`Cases/`, `Topics/`, `Lectures/`), each backed by a `Templates/*.md` schema. The Case Brief template carries roughly 30 frontmatter fields; its `source_files` field records provenance back to the originating Source Materials filename or the Midpage `analyzeOpinion` opinion ID.

Cross-reference: this appendix is referenced by Sections IV (input corpus) and V (Obsidian vault).
