---
id: "04"
title: "The Input Corpus"
status: ready_for_stitch
target_words: 900
word_count: 944
last_phase: polish
draft_status: needs_polish
cite_status: needs_polish
polish_status: ready_for_stitch
---

# IV. The Input Corpus

## A. What the LMS handed us

The corpus comes from a single course taught by a single professor in a single semester: Professor Chandler’s Constitutional Law I, Spring 2026.[^1] The doctrinal scope is the structural-plus-rights subset typical of a one-semester Con Law I sequence rather than the full constitutional law curriculum, covering judicial review, federalism, separation of powers, the Commerce Clause, executive power, justiciability, preemption, state sovereign immunity, the Reconstruction Amendments, substantive due process, equal protection, the First Amendment, and the Second Amendment; Section X takes up the generalization question beyond this one-course scope.[^2] The export arrived as a flat folder of three hundred eighty-eight files, one hundred twenty-seven of them at the top level, with sixty-one PowerPoint lecture decks, sixty-six PDFs of case readings and slide handouts, and three DOCX files among the top-level set.[^3] This is the raw surface that the schema layer described in Section V is built to translate from, and the concrete answer to the question Section II raises about why an LMS folder by itself is not yet a course knowledge system. The corpus is course-issued materials only: lecture decks, professor-prepared opinion PDFs, merged reading packets, and a small set of assessment artifacts; students also work from an assigned casebook alongside this course-issued layer, and whether the casebook itself was ingested as input to the vault is an open question this article hedges throughout.[^4] The published wiki on Netlify is a static, reviewed website rather than a chatbot or conversational tutor, a distinction Section XII’s risk argument returns to.[^5]

## B. Anatomy of the export

The Source Materials folder is shallow at the top, but the Uploaded Media subfolder holds the bulk of the case reading. One hundred thirty-five individual case-opinion PDFs sit in that subfolder, one decision per file, with filenames such as 02_lochner_v_new_york-1.pdf and Fulton_v_City_of_Philadelphia_Modernized.pdf.[^6] Twelve merged reading packets, whose filenames begin with the merged- prefix, bundle several decisions per topic, including merged-incorporation.pdf and merged-equal-protection-limitations.pdf.[^7] A separate resources subfolder contains eighty-one HTML files exported from Canvas, and an unfiled subfolder holds a single Midterm rubric.[^8] The shape of the export is the shape of a course shell, and that recognition matters for Section V, which contrasts filename-level organization against a structured note layer.

Thirty-seven files in the export carry the modernized tag in their filenames, including mcculloch_modernized.pdf, youngstown-modernized.pdf, dobbs_modernized.pdf, bruen-modernized.pdf, and Fulton_v_City_of_Philadelphia_Modernized.pdf.[^9] These are not slip opinions; they are professor-edited versions of older opinions, updated to ease the archaic phrasing for student readers.[^10] Modernized PDFs are among the most pedagogically useful inputs the export contained, and among the most epistemically dangerous to ingest without verification against an indexed opinion. Section VII develops the consequence; Section IV introduces the input type.

The export also includes three prior exam artifacts and one published grading rubric: Final Exam Constitutional Law Fall 2023.pdf, Constitutional Law Final Exam Spring 2025 (Reduced).pdf, TEFA_Exam_Question.docx.pdf, and Midterm_Rubric.pdf.[^11] These files encode professorial judgment about what counts as a complete answer and which doctrinal issues the course centers. They are what later allow the vault to generate hypotheticals and exam-tip blocks within its Topic pages, and they are what keeps Section IV from being a reading-list inventory.

## C. What the LMS did not hand us

The corpus is bounded by what was uploaded to Canvas, not by what the syllabus assigned. Ten foundational opinions the syllabus references have wiki briefs but no corresponding source file on disk: *Cohens v. Virginia*, *United States v. Cruikshank*, *Wickard v. Filburn*, *Adamson v. California*, *Baker v. Carr*, *USDA v. Moreno*, *South Dakota v. Dole*, *United States v. Lopez*, *United States v. Morrison*, and *Hamdi v. Rumsfeld*.[^12] Students presumably read these decisions in the assigned casebook rather than from a course-issued PDF. The wiki briefs themselves exist, generated against an indexed-opinion source, but the deployed site cannot offer readers a course-issued reading for these cases because no such file is on disk.[^13] Section II uses this gap to motivate why ordinary LMS infrastructure is incomplete by itself.

This article does not claim that casebook excerpts were ingested as input to the vault; that question remains open at the time of writing.[^14] For the same reason, this article does not claim that student work, including prior exam answers, office-hours notes, or LMS posts, was used as training input.[^15] The privacy framing in Section XII depends on whichever way each question lands.

## D. Filename hygiene as a signal

The Canvas export does not enforce a filename convention. Within the same one-hundred-twenty-seven-file top-level folder, the same kind of artifact, a lecture slide deck, appears under many shapes: 11th Amendment.pptx, Architecture_of_Exclusion.pptx, Biden_v_Nebraska_Standing.pptx, Enumerated Powers- Warren Court and Beyond (2026).pptx, Federalist Papers 2025.pptx, and Gibbons v. Ogden.pptx.[^16] Hyphens, underscores, spaces, parenthetical years, and dotted abbreviations appear in arbitrary combinations within one folder. Some filenames encode topic, some encode case name, some encode year, and no rule predicts which. The point is not that filename hygiene is poor; the point is that filename-level organization renders the professor’s already-prepared materials inconsistently machine-readable, a gap the structured note layer described in Section V addresses without further filename cleanup.

## E. Snapshot and disclosure

The article snapshots the input-to-output state at the date of the professor-facing progress report, which records one hundred ninety-eight wiki pages comprising ninety-two case briefs, twenty-seven doctrinal topic pages, and seventy-nine lecture summaries.[^17] Anchoring Sections III and IV to that single disclosed date means peer reviewers will not catch the article citing different numbers from different audits. The corpus and the wiki keep growing; a filesystem audit on May 15, 2026, records two hundred eighty-one wiki pages against the progress report’s one hundred ninety-eight, and this article footnotes the drift in case publication follows further ingestion.[^18] The ingest-phase line of the full cost-and-labor accounting lives at the master cost table in Section IX, with this section’s forward reference closing through that table once it lands.[^19] Applying the vault’s own snapshot discipline to the article that describes it is the kind of self-consistency the thesis requires; final sign-off on the snapshot-date selection awaits professorial review.[^20]

## Footnotes

[^1]: *See infra* App. A (Input Corpus Inventory) (cataloguing course-issued materials for Constitutional Law I (Spring 2026) taught by Professor Chandler).

[^2]: *Id.* The fourteen-topic enumeration names the structural-plus-rights subset taught in this one-semester sequence; *see also infra* Section X (taking up whether the method generalizes to other doctrinal areas and to fuller constitutional law sequences).

[^3]: *See infra* App. A (Input Corpus Inventory) (filesystem audit of the Source Materials/ folder, Constitutional Law Vault (May 15, 2026)).

[^4]: Casebook-input status remains an open question at the time of writing pending professorial resolution; the article carries the hedge in body prose throughout Sections IV and XII rather than asserting either inclusion or exclusion.

[^5]: *See infra* Section III (describing the deployed static website and its review pipeline); *see also infra* Section XII (distinguishing the static, reviewed website from chatbot architectures). For representative chatbot-tutor architectures against which the static-website contrast operates, *see also infra* Section V (citing Dong et al. KG-RAG and Peng et al. GraphRAG-survey for the structured-retrieval architectural insight); *see also infra* Section VIII (citing Sajja et al. as a single-platform chatbot-tutor exemplar). The transfer-of-inference framing is the architectural insight that structure-aware retrieval beats flat semantic similarity; the chatbot-tutor implementation surface does not transfer to the case study’s static, reviewed publication form.

[^6]: *See infra* App. A (Input Corpus Inventory) (Source Materials/Uploaded Media/ subfolder: one hundred thirty-five individual case-opinion PDFs as of filesystem audit (May 15, 2026)).

[^7]: *Id.* (twelve merged-prefixed reading packets, including merged-incorporation.pdf and merged-equal-protection-limitations.pdf).

[^8]: *Id.* (resources/ subfolder of eighty-one HTML files exported from the Canvas LMS; unfiled/Midterm_Rubric.pdf).

[^9]: *See infra* App. A (Input Corpus Inventory) (filesystem audit of files containing the modernized tag in filenames across Source Materials/ and Source Materials/Uploaded Media/ (May 15, 2026)).

[^10]: *Id.*

[^11]: *See infra* App. A (Input Corpus Inventory) (Source Materials/Uploaded Media/Final Exam Constitutional Law Fall 2023.pdf; Constitutional Law Final Exam Spring 2025 (Reduced).pdf; TEFA_Exam_Question.docx.pdf; and Source Materials/unfiled/Midterm_Rubric.pdf).

[^12]: *See infra* App. A (Input Corpus Inventory) (Missing-from-Export subsection). The ten opinions referenced are: *Cohens v. Virginia*, 19 U.S. (6 Wheat.) 264 (1821); *United States v. Cruikshank*, 92 U.S. 542 (1876); *Wickard v. Filburn*, 317 U.S. 111 (1942); *Adamson v. California*, 332 U.S. 46 (1947); *Baker v. Carr*, 369 U.S. 186 (1962); *USDA v. Moreno*, 413 U.S. 528 (1973); *South Dakota v. Dole*, 483 U.S. 203 (1987); *United States v. Lopez*, 514 U.S. 549 (1995); *United States v. Morrison*, 529 U.S. 598 (2000); and *Hamdi v. Rumsfeld*, 542 U.S. 507 (2004).

[^13]: *See infra* App. A (Input Corpus Inventory) (Missing-from-Export subsection: wiki briefs for the ten listed opinions present in the vault’s Cases/ folder as of the May 15, 2026 filesystem audit). The wiki briefs were generated against an indexed-opinion source described *infra* Section V; the deployed-site URL anchoring the published versions is named in body prose at Section VIII.A and footnoted at *infra* Section VIII note 1.

[^14]: Casebook-ingestion status remains an open question at the time of writing pending professorial resolution; the article hedges any positive claim about casebook ingestion throughout until that question lands, and the underlying record lives in this article’s internal pending-issue tracker.

[^15]: Student-work-ingestion status, including prior exam answers, office-hours notes, and LMS posts, remains an open question at the time of writing pending professorial resolution; the privacy framing in Section XII depends on whichever way the question lands, and the underlying record lives in this article’s internal pending-issue tracker.

[^16]: *See infra* App. A (Input Corpus Inventory) (filename sample drawn from a directory listing of Source Materials/ on May 15, 2026).

[^17]: *See infra* App. A (Input Corpus Inventory) (Vault Output Snapshot subsection: one hundred ninety-eight wiki pages as of the progress-report date, comprising ninety-two case briefs, twenty-seven doctrinal topic pages, and seventy-nine lecture summaries; underlying progress report excerpted *infra* App. D (Correspondence Excerpts)).

[^18]: *See infra* App. A (Input Corpus Inventory) (filesystem audit of May 15, 2026: one hundred thirty-one case briefs, fifty-three doctrinal topic pages, and ninety-seven lecture summaries, totaling two hundred eighty-one pages).

[^19]: *See also infra* Section IX (Cost and Labor: The Honest Accounting) (master cost-and-labor table; ingest-phase line item closes through that table per the article’s single-owner cost-routing convention).

[^20]: The recommended snapshot is the professor-facing progress report’s date that records the one hundred ninety-eight-page output state; final sign-off on the snapshot selection awaits professorial review and the underlying record lives in this article’s internal pending-issue tracker.
