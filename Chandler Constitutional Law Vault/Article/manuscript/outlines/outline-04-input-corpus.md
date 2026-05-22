---
id: "04"
title: "The Input Corpus"
status: ready_for_draft
target_words: 900
last_phase: outline
evidence_cards:
  - evidence-04-top-level-counts
  - evidence-04-uploaded-media-and-packets
  - evidence-04-modernized-pdfs
  - evidence-04-assessment-materials
  - evidence-04-vault-output-snapshot
  - evidence-04-missing-from-export
  - evidence-04-filename-heterogeneity
  - evidence-04-course-scope
---

# Section IV. The Input Corpus

Spine for the draft phase. Each H2 has a word budget; subtotal is 900. Each bullet states the claim, names the evidence, and signals the inferential move it carries for the rest of the article. The section is descriptive, not argumentative; the argumentative weight lives in Sections II, V, VII, and XII, which all depend on Section IV having said clearly what came in.

## 4.1 What the LMS handed us (180 words)

- Claim: the corpus is a single LMS export from a single course taught by a single professor in a single semester. Evidence: course-scope card naming Chandler, Con Law I, Spring 2026, and the doctrinal subject list. Inferential move: bounds the case study so Section X (Generalization) can argue from a clearly disclosed base case rather than an unstated one. [evidence: evidence-04-course-scope]
- Claim: the export arrived as a flat folder of 388 files, 127 of them at the top level, with 61 .pptx, 66 .pdf, and 3 .docx among the top-level files. Evidence: filesystem audit on 2026-05-15 confirms the figures the blog draft cites. Inferential move: this is the raw surface the system was asked to read, and it is the surface Section V's schema layer is built on top of. [evidence: evidence-04-top-level-counts]
- Claim: the corpus is course-issued materials only, not casebook text, public judicial opinions are referenced through their professor-issued PDFs, and the published wiki on Netlify is what the article calls a static site rather than a chatbot. Evidence: workplan §6.1 open question, lesson L-003. Inferential move: locks Section IV's framing to what Section XII's risk argument needs (static reviewed site, not conversational AI). [evidence: pending issue PI-001 hedge]

## 4.2 Anatomy of the export (250 words)

- Claim: the bulk of the case reading lives in a single Uploaded Media subfolder containing 135 individual case opinion PDFs, 12 merged reading packets named with the merged- prefix, plus a resources/ subfolder with 81 HTML files exported from Canvas. Evidence: filesystem audit, 2026-05-15. Inferential move: gives the reader a concrete picture of what the LMS calls a course shell, so the Section V comparison between filename-level organization and YAML-frontmatter pages has something to push against. [evidence: evidence-04-uploaded-media-and-packets]
- Claim: 37 files in the export carry the modernized tag, meaning the professor edited the underlying archaic text so students could read it (examples: mcculloch_modernized.pdf, youngstown-modernized.pdf, dobbs_modernized.pdf, Fulton_v_City_of_Philadelphia_Modernized.pdf). Evidence: filesystem audit; vault-blog-post-draft.md "The quote problem" paragraph. Inferential move: this is the upstream cause of the Prize Cases quotation error that Section VII anchors; Section IV introduces the input type, Section VII pays it off. [evidence: evidence-04-modernized-pdfs]
- Claim: the corpus contained three prior exam artifacts (two finals, one TEFA question packet) and one published Midterm rubric, which encode professorial judgment about what counts as a complete answer. Evidence: filesystem paths cited in evidence card. Inferential move: this is what lets the vault generate hypotheticals and exam-tip blocks in Topic pages later, and it is what makes Section IV more than a reading-list inventory. [evidence: evidence-04-assessment-materials]

## 4.3 What the LMS did not hand us (200 words)

- Claim: ten foundational SCOTUS opinions referenced by the syllabus have wiki briefs but no corresponding source file on disk. Evidence: MISSING_SOURCE_MATERIALS.md, ten named cases (Cohens, Cruikshank, Wickard, Adamson, Baker v. Carr, USDA v. Moreno, South Dakota v. Dole, Lopez, Morrison, Hamdi). Inferential move: the corpus is bounded by what was uploaded to Canvas, not by what the syllabus assigns; Section II uses this to motivate the gap that the course knowledge system fills. [evidence: evidence-04-missing-from-export]
- Claim: the article does not claim that casebook excerpts were ingested, and Section IV hedges or omits any such claim until the professor resolves the open question. Evidence: pending issue PI-001; workplan §6.1. Inferential move: protects the JLE submission against copyright surprise and keeps Section XII's risk taxonomy consistent. [evidence: pending issue PI-001]
- Claim: the article does not claim that student work (prior exam answers, office-hours notes, LMS posts) was used as training input, again pending professorial confirmation. Evidence: pending issue PI-002; workplan §6.2. Inferential move: privacy framing in Section IV and the parallel risk in Section XII depend on whichever way the professor resolves this. [evidence: pending issue PI-002]

## 4.4 Filename hygiene as a signal (140 words)

- Claim: the export does not enforce a filename convention; hyphens, underscores, spaces, parenthetical years, and dotted abbreviations appear in arbitrary combinations within one 127-file top-level folder. Evidence: representative sample drawn from ls Source Materials/ on 2026-05-15 (11th Amendment.pptx, Architecture_of_Exclusion.pptx, Biden_v_Nebraska_Standing.pptx, Enumerated Powers- Warren Court and Beyond (2026).pptx, Federalist Papers 2025.pptx, Gibbons v. Ogden.pptx). Inferential move: this is the surface the schema layer in Section V translates from, and it is the concrete answer to Section II's question of why an LMS folder by itself is not yet a course knowledge system. [evidence: evidence-04-filename-heterogeneity]
- Claim: filename-level organization encodes intent unevenly (some filenames carry topic, some carry case name, some carry year). Evidence: same sample. Inferential move: motivates the need for a structured note layer rather than further filename cleanup; this is the small bridge to Section V. [evidence: evidence-04-filename-heterogeneity]

## 4.5 Snapshot and disclosure (130 words)

- Claim: the article snapshots the input-to-output state at the date of the professor-facing progress email, which reports 198 wiki pages comprising 92 case briefs, 27 doctrinal topics, and 79 lecture summaries. Evidence: email-to-chandler-progress.md paragraph 2 (verbatim quoted in evidence card). Inferential move: anchors Sections III and IV to one disclosed date so JLE peer review cannot catch the article citing different numbers from different audits. [evidence: evidence-04-vault-output-snapshot]
- Claim: the corpus and the wiki keep growing; a 2026-05-15 audit shows 281 wiki pages against the email's 198, and Stitch will footnote the drift if the article publishes after further ingestion. Evidence: filesystem audit; lesson L-011. Inferential move: applies the vault's own snapshot discipline to the article that describes it, which is the kind of self-consistency the thesis is selling. [evidence: evidence-04-vault-output-snapshot]

## Open questions

These are claims Section IV currently hedges or omits because the underlying fact has not been resolved. Draft phase must not invent answers; each item names what would close the gap.

- PI-001 (casebook input). Section 4.1 currently treats the corpus as "course-issued materials only" and 4.3 hedges any casebook claim. Closes when the professor confirms whether casebook text appears anywhere in the 198 pages (workplan §6.1).
- PI-002 (student work input). Section 4.3 omits any positive claim. Closes when the professor confirms whether past exam answers, office-hours notes, or LMS posts were used as training input (workplan §6.2). Privacy framing in §12 depends on the answer.
- PI-003 (ingest-phase cost). Section IV does not own the full cost table (Section IX does), but a single ingest-phase line item belongs in 4.5 if available. Closes when the cost log reconstruction in workplan §3.1 produces an ingest-phase number, even an estimate footnoted as such.
- PI-004 (snapshot date). 4.5 currently picks the email's 198-page snapshot. Closes when the professor or author endorses that snapshot in writing; if a tagged release or archive.org capture is preferred, swap in 4.5 and footnote the date.

## Word budget check

180 + 250 + 200 + 140 + 130 = 900. Target is 900. Within 10 percent floor and ceiling.
