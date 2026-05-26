---
id: "04"
title: "The Input Corpus"
status: needs_polish
target_words: 900
word_count: 899
last_phase: cite
draft_status: needs_polish
cite_status: needs_polish
---

# IV. The Input Corpus

## A. What the LMS handed us

The corpus comes from a single course taught by a single professor in a single semester: Professor Chandler's Constitutional Law I, Spring 2026.[^1] The doctrinal scope is the structural constitution rather than the full year of constitutional law, covering judicial review, federalism, separation of powers, the Commerce Clause, executive power, justiciability, preemption, state sovereign immunity, the Reconstruction Amendments, substantive due process, equal protection, the First Amendment, and the Second Amendment.[^2] The export arrived as a flat folder of three hundred eighty-eight files, its top level holding sixty-one PowerPoint lecture decks and sixty-six PDFs of case readings and slide handouts, the one hundred twenty-seven slide-and-reading files the flat structure exposed first, alongside three DOCX files.[^3] This is the raw surface that the schema layer described in Section V is built to translate from, and the concrete answer to the question Section II raises about why an LMS folder by itself is not yet a course knowledge system. The corpus is course-issued materials only: lecture decks, professor-prepared opinion PDFs, merged reading packets, and a small set of assessment artifacts. The published wiki on Netlify is a static, reviewed website rather than a chatbot or conversational tutor, a distinction Section XII's risk argument returns to.[^4]

## B. Anatomy of the export

The Source Materials folder is shallow at the top, but the Uploaded Media subfolder holds the bulk of the case reading. One hundred thirty-five individual case-opinion PDFs sit in that subfolder, one decision per file, with filenames such as 02_lochner_v_new_york-1.pdf and Fulton_v_City_of_Philadelphia_Modernized.pdf.[^5] Twelve merged reading packets, whose filenames begin with the merged- prefix, bundle several decisions per topic, including merged-incorporation.pdf and merged-equal-protection-limitations.pdf.[^6] A separate resources subfolder contains eighty-one HTML files exported from Canvas, and an unfiled subfolder holds a single Midterm rubric.[^7] The shape of the export is the shape of a course shell, and that recognition matters for Section V, which contrasts filename-level organization against a structured note layer.

Thirty-seven files in the export carry the modernized tag in their filenames, including mcculloch_modernized.pdf, youngstown-modernized.pdf, dobbs_modernized.pdf, bruen-modernized.pdf, and Fulton_v_City_of_Philadelphia_Modernized.pdf.[^8] These are not slip opinions; they are professor-edited versions of older opinions, updated to ease the archaic phrasing for student readers.[^9] Modernized PDFs are among the most pedagogically useful inputs the export contained, and among the most epistemically dangerous to ingest without verification against an indexed opinion. Section VII develops the consequence; Section IV introduces the input type.

The export also includes three prior exam artifacts and one published grading rubric: Final Exam Constitutional Law Fall 2023.pdf, Constitutional Law Final Exam Spring 2025 (Reduced).pdf, TEFA_Exam_Question.docx.pdf, and Midterm_Rubric.pdf.[^10] These files encode professorial judgment about what counts as a complete answer and which doctrinal issues the course centers. They are what later allow the vault to generate hypotheticals and exam-tip blocks within its Topic pages, and they are what keeps Section IV from being a reading-list inventory.

## C. What the LMS did not hand us

The corpus is bounded by what was uploaded to Canvas, not by what the syllabus assigned. Ten foundational opinions the syllabus references have wiki briefs but no corresponding source file on disk: Cohens v. Virginia, United States v. Cruikshank, Wickard v. Filburn, Adamson v. California, Baker v. Carr, USDA v. Moreno, South Dakota v. Dole, United States v. Lopez, United States v. Morrison, and Hamdi v. Rumsfeld.[^11] Students presumably read these decisions in the assigned casebook rather than from a course-issued PDF. The wiki briefs themselves exist, generated against an indexed-opinion source, but the deployed site cannot offer readers a course-issued reading for these cases because no such file is on disk.[^12] Section II uses this gap to motivate why ordinary LMS infrastructure is incomplete by itself.

This article does not claim that casebook excerpts were ingested as input to the vault; that question remains open at the time of writing, and Section IV hedges any positive claim until the professor resolves it. [TODO: evidence needed for casebook-input status; see PI-001] For the same reason, this article does not claim that student work, including prior exam answers, office-hours notes, or LMS posts, was used as training input. [TODO: evidence needed for student-work-input status; see PI-002] The privacy framing in Section XII depends on whichever way each question lands.

## D. Filename hygiene as a signal

The Canvas export does not enforce a filename convention. Within the same top-level folder, the same kind of artifact, a lecture slide deck, appears under many shapes: 11th Amendment.pptx, Architecture_of_Exclusion.pptx, Biden_v_Nebraska_Standing.pptx, Enumerated Powers- Warren Court and Beyond (2026).pptx, Federalist Papers 2025.pptx, and Gibbons v. Ogden.pptx.[^13] Hyphens, underscores, spaces, parenthetical years, and dotted abbreviations appear in arbitrary combinations within one folder. Some filenames encode topic, some encode case name, some encode year, and no rule predicts which. The point is not that filename hygiene is poor; the point is that filename-level organization carries pedagogical intent unevenly, which is the small bridge to Section V's case for a structured note layer rather than further filename cleanup.

## E. Snapshot and disclosure

The article snapshots the input-to-output state at the date of the professor-facing progress report, which records one hundred ninety-eight wiki pages comprising ninety-two case briefs, twenty-seven doctrinal topic pages, and seventy-nine lecture summaries.[^14] Anchoring Sections III and IV to that single disclosed date means peer reviewers will not catch the article citing different numbers from different audits. The corpus and the wiki keep growing; a filesystem audit on May 15, 2026, records two hundred eighty-one wiki pages against the progress report's one hundred ninety-eight, and Stitch will footnote the drift if the article publishes after further ingestion.[^15] Applying the vault's own snapshot discipline to the article that describes it is the kind of self-consistency the thesis is selling. [TODO: evidence needed for ingest-phase cost line item; see PI-003] [TODO: evidence needed for snapshot-date sign-off; see PI-004]

## Footnotes

[^1]: *See infra* App. A (Input Corpus Inventory) (cataloguing course-issued materials for Constitutional Law I (Spring 2026) taught by Professor Chandler).

[^2]: *Id.*

[^3]: *See infra* App. A (Input Corpus Inventory) (filesystem audit of the Source Materials/ folder, Constitutional Law Vault (May 15, 2026)).

[^4]: *See infra* Section III (describing the deployed static website and its review pipeline); *see also infra* Section XII (distinguishing the static, reviewed website from chatbot architectures).

[^5]: *See infra* App. A (Input Corpus Inventory) (Source Materials/Uploaded Media/ subfolder: one hundred thirty-five individual case-opinion PDFs as of filesystem audit (May 15, 2026)).

[^6]: *Id.* (twelve merged-prefixed reading packets, including merged-incorporation.pdf and merged-equal-protection-limitations.pdf).

[^7]: *Id.* (resources/ subfolder of eighty-one HTML files exported from the Canvas LMS; unfiled/Midterm_Rubric.pdf).

[^8]: *See infra* App. A (Input Corpus Inventory) (filesystem audit of files containing the modernized tag in filenames across Source Materials/ and Source Materials/Uploaded Media/ (May 15, 2026)).

[^9]: *Id.*

[^10]: *See infra* App. A (Input Corpus Inventory) (Source Materials/Uploaded Media/Final Exam Constitutional Law Fall 2023.pdf; Constitutional Law Final Exam Spring 2025 (Reduced).pdf; TEFA_Exam_Question.docx.pdf; and Source Materials/unfiled/Midterm_Rubric.pdf).

[^11]: *See infra* App. A (Input Corpus Inventory) (Missing-from-Export subsection). The ten opinions referenced are: *Cohens v. Virginia*, 19 U.S. (6 Wheat.) 264 (1821); *United States v. Cruikshank*, 92 U.S. 542 (1876); *Wickard v. Filburn*, 317 U.S. 111 (1942); *Adamson v. California*, 332 U.S. 46 (1947); *Baker v. Carr*, 369 U.S. 186 (1962); *USDA v. Moreno*, 413 U.S. 528 (1973); *South Dakota v. Dole*, 483 U.S. 203 (1987); *United States v. Lopez*, 514 U.S. 549 (1995); *United States v. Morrison*, 529 U.S. 598 (2000); and *Hamdi v. Rumsfeld*, 542 U.S. 507 (2004).

[^12]: *See infra* App. A (Input Corpus Inventory) (Missing-from-Export subsection); *see also* Constitutional Law Wiki, https://constitutionallaw.netlify.app (last visited May 16, 2026) (URL liveness verification deferred to next Cite or Verify pass; see PI-005). The wiki briefs were generated against an indexed-opinion source described *infra* Section V.

[^13]: *See infra* App. A (Input Corpus Inventory) (filename sample drawn from a directory listing of Source Materials/ on May 15, 2026).

[^14]: *See infra* App. A (Input Corpus Inventory) (Vault Output Snapshot subsection: one hundred ninety-eight wiki pages as of the progress-report date, comprising ninety-two case briefs, twenty-seven doctrinal topic pages, and seventy-nine lecture summaries; underlying progress report excerpted *infra* App. D (Correspondence Excerpts)).

[^15]: *See infra* App. A (Input Corpus Inventory) (filesystem audit of May 15, 2026: one hundred thirty-one case briefs, fifty-three doctrinal topic pages, and ninety-seven lecture summaries, totaling two hundred eighty-one pages).
