---
id: "01"
title: "Introduction: The Hidden Archive of the Law Professor"
status: ready_for_stitch
target_words: 900
word_count: 842
last_phase: polish
draft_status: needs_polish
cite_status: needs_polish
polish_status: ready_for_stitch
footnotes_count: 8
---

# I. Introduction: The Hidden Archive of the Law Professor

## A. The archive no one can open

Every experienced doctrinal teacher carries a course in two places: inside their head and across a hard drive. The drive holds syllabi, lecture decks, annotated cases, hypotheticals tried and discarded, and exam rubrics. The head holds the rest, including the accumulated judgment about exactly where a class loses the thread of a doctrine and what question pulls it back. This is real intellectual capital, and almost none of it sits in a form a second person can use. The files arrive in a learning-management folder as a flat list organized only by name.[^1] The judgment lives in the professor and in the live classroom, where it is performed once and then gone. Over years the professor also learns which sequence of cases builds an argument and which detours cost a week, yet that ordering rationale rarely survives outside the syllabus’s bare list of assignments. A successor instructor inherits the syllabus but not the reasoning that built it. A student receives the assigned reading but not the map that joins one week’s case to the next. The archive exists, yet no one, the professor included, can open it as a whole.

## B. The claim

This article describes a method for opening that archive. Generative AI, working on structured source materials, Obsidian-style markdown notes, retrieval from verified legal sources, and iterative expert review, can convert a professor’s scattered course materials into a navigable, cross-linked, student-facing course knowledge system. The constitutional-law case study below is the demonstration; the transferable contribution is the method, which other doctrinal courses with similar archives can follow. The essential feature is not automation. The essential feature is iteration under the control of a human expert, who reviews, corrects, and signs off on every layer the system produces. Review here is not a gloss applied at the end. It is built into the process at defined checkpoints, where the professor inspects what the system has drafted, corrects what is wrong, and decides whether the work advances or returns for another pass.[^2]

The article is not the announcement of an AI teaching assistant, and it is not a chatbot placed in front of students. The case study is a reviewed static website, not a conversational agent, and that architectural choice carries the article’s later argument about risk.[^3] The article also makes no claim that students learned more, because it has not run the study that would license such a claim.[^4] The system did not replace professorial judgment; it made that judgment reusable, inspectable, and publishable.

## C. The case study, in one breath

The case study is concrete and public. A single professor’s Constitutional Law I course, taught in a single semester, became a live knowledge system of 198 pages, comprising 92 case briefs, 27 doctrinal topic pages, and 79 lecture summaries, published at https://constitutionallaw.netlify.app and readable by anyone.[^5] Each case page is written against the indexed judicial opinion rather than a paraphrase of it, so a quotation a student relies on can be traced to the source that controls it.[^6] The doctrinal scope is the structural constitution: judicial review, federalism, separation of powers, the commerce power, executive authority, justiciability, and the Reconstruction amendments, among the subjects a first constitutional-law course covers.[^7] The article’s later claim that the method generalizes beyond constitutional law rests on a clearly bounded base case, so the scope is fixed before that argument is made.

## D. The conversation this enters

The article enters a conversation the Journal of Legal Education has already begun. Recent empirical work in these pages reports that AI assistance can help weaker students more than stronger ones on law-school examinations, with a potential equalizing effect.[^8] That study sets both the stakes and the standard. It shows that serious inquiry into AI and legal learning is possible at proportional rigor, without overclaiming and without waiting for a controlled trial that a single course cannot run. This article’s contribution sits upstream of any classroom intervention. It concerns the infrastructure a professor assembles before a student arrives, and it insists that a human expert remain in command of each step that builds it. The question it takes up is therefore not whether a model can answer a student’s query, but whether a professor can turn a career’s worth of dispersed materials into a resource that others can read, check, and build on.

## E. The shape of the argument

The argument proceeds in the order a reader needs it. It begins with why ordinary course infrastructure, the casebook, the syllabus, the slide deck, and the learning-management folder, cannot produce a course knowledge system on its own. It then presents the case study and the corpus and schemas that constitute it, the prompting practice that shaped its pages, and the iterative loop, run under professorial review, that improved them. It accounts honestly for publication and for cost in dollars and hours, and it closes with generalization to other courses, an evaluation plan proportional to the claims, the risks the approach carries, and the institutional questions it raises. Throughout, the constitutional-law content is the example. The method is the result the article asks other faculty to reuse.

## Footnotes

[^1]: *See infra* Section IV (The Input Corpus) (describing the Canvas learning-management export as a flat folder whose only organization is the filename string); *see also infra* App. A (Input Corpus Inventory) (filename sample drawn from a directory listing of the Source Materials folder on May 15, 2026).

[^2]: *See infra* Section VII (Iterative Improvement Under Professorial Control) (describing the professorial-review checkpoints built into each phase of the maintenance rotation, under which the professor inspects the drafted work, corrects what is wrong, and gates whether the work advances or returns for another pass).

[^3]: *See infra* Section XII (Risks and Limits) (developing the architectural contrast between the reviewed static-website case study and chatbot architectures, and locating the case study’s risk surface at build-time professorial review rather than at runtime generation).

[^4]: *See infra* Section XI (Evaluation: What Would Count as Success) (stating that the article advances a method claim rather than a learning-outcomes claim, and describing the method-plus-light-data evaluation posture adopted in lieu of a controlled trial the single course cannot run).

[^5]: Constitutional Law I Wiki, https://constitutionallaw.netlify.app (last visited May 23, 2026) (URL verified live this run via WebFetch; the deployed static site presents Dashboard, Cases, Topics, Lectures, Recent, and About navigation and identifies the course as Professor Chandler’s Constitutional Law I, Spring 2026); *see also infra* App. A (Input Corpus Inventory) (198-page corpus snapshot of 92 case briefs, 27 doctrinal topic pages, and 79 lecture summaries as of the progress-report date; underlying progress report excerpted *infra* App. D (Correspondence Excerpts)).

[^6]: *See infra* Section III (Case Study: A Constitutional-Law Knowledge System) (describing the discipline under which every key quotation on a case page links to the cited line of the indexed judicial opinion, so a reader can trace each pull-quote to the source that controls it).

[^7]: *See infra* Section IV (The Input Corpus) (identifying the corpus as a single course, Constitutional Law I (Spring 2026) taught by Professor Chandler, and bounding its doctrinal scope to the structural constitution).

[^8]: Jonathan H. Choi & Daniel Schwarcz, *AI Assistance in Legal Analysis: An Empirical Study*, 73 J. Legal Educ. 384 (2025), https://jle.aals.org/home/vol73/iss2/5/ (last visited May 23, 2026) (URL verified live this run via WebFetch, returning the verbatim article title and the authors’ names and institutions); *see also infra* Section XI (Evaluation: What Would Count as Success) (deploying the same study as precedent that publishable empirical work on artificial intelligence in this Journal’s pages does not require a randomized controlled trial).
