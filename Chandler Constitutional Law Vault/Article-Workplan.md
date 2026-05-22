# From Casebook to Course Knowledge System

## A course of action and annotated bibliography for the JLE article

Last updated: May 15, 2026

This is a working plan. It absorbs Professor Chandler’s detailed feedback, grounds the case study in what actually exists in this vault, and lays out a path from where the project sits today to a publishable Journal of Legal Education article. Everything below is editable; nothing is locked in.

---

## 1. What we are actually claiming

The article makes one argument, in the professor’s shape:

> Law professors already possess vast course‑specific knowledge: syllabi, class notes, hypotheticals, case annotations, doctrinal explanations, diagrams, classroom questions, exam rubrics, and accumulated judgment about student confusion. Generative AI, combined with structured source materials, Obsidian‑style markdown notes, retrieval from verified legal sources, and iterative expert review, can convert that dispersed archive into a navigable course knowledge system. The constitutional‑law website is the case study; the broader contribution is a replicable method for other law‑school courses.

Working title (the professor’s preferred): **From Casebook to Course Knowledge System: AI‑Assisted Synthesis, Obsidian, and the Future of Legal Pedagogy**

What the article is *not*:

- Not “I built an AI teaching assistant.”
- Not “chatbot in the classroom.”
- Not a product announcement.
- Not a claim that students learned more (unless we run the study in Section XI).

What the article *is*:

- A method paper, in the voice of an experienced legal educator describing a workshop process.
- Centered on the professor‑in‑the‑loop, with the system as scaffold rather than substitute.
- Replicable by faculty in other doctrinal courses with similar archives.

---

## 2. What this vault already proves

A scan of the vault confirms there is real evidence to draw on. Highlights worth lifting straight into the article:

- **A live, deployed knowledge system** at `https://constitutionallaw.netlify.app` with 198 pages: 92 case briefs, 27 doctrinal topic pages, 79 lecture summaries (per `email-to-chandler-progress.md`).
- **A real pipeline**: Source Materials (61 PowerPoints, 66 PDFs, merged reading packets, practice exams) → Obsidian markdown vault (`Cases/`, `Topics/`, `Lectures/`, `Templates/`) → static site → Netlify.
- **Structured schemas**: per‑page YAML frontmatter, canonical templates in `Templates/`, 9‑section case‑brief standard, wiki‑link conventions documented in `PROJECT_PRIMER.md`.
- **A documented six‑phase rotation**: Ingest → Lint → Enrich → Expand → Synthesize → Verify, with one phase per scheduled run and per‑phase rubrics in `rubric/`.
- **A self‑improvement record**: `LESSONS.md` (and prior `LESSONS_*.md` archives) capturing 30+ codified mistakes; run‑by‑run scorecards in `.run-scores.jsonl`; rolling build narratives in `BUILD_NARRATIVE_YYYY‑MM.md`. This is the Karpathy loop, domesticated.
- **A verified‑source discipline**: Midpage `analyzeOpinion` / `findInOpinion` for quotation verification; CourtListener for citation chains. Cases are read against indexed opinions, not paraphrased PDFs.
- **A concrete failure story we can lead with**: The Prize Cases / Justice Grier quotation. The professor’s modernized PDF silently updated archaic phrasing; Ingest, Lint, two Enrich passes, and Expand all reproduced “never formally declared…by its character” faithfully. Only an adversarial Verify pass, switching from keyword search to AI analysis of the indexed opinion, returned Grier’s actual language: “never solemnly declared…by its accidents.” The article should open Section VII or XII with that story. It does more work than a paragraph of theory.
- **An honest cost note**: roughly 60% of the weekly Claude usage to reach 198 pages, plus the human time. We can quantify this.
- **A “professor in the loop” email trail**: `email-to-chandler-progress.md` and `email-to-chandler-stages.md` are real artifacts of the human handoff. We should reproduce relevant fragments in an appendix.

Treat the existing `archive/vault-blog-post-draft.md` as raw material. It already has the Prize Cases story and the token‑problem story in usable prose. We mine; we do not paste.

---

## 3. What is still missing

The most important gaps to close before the article can land:

1. **Cost and time log.** We have a hand‑wave at 60% of weekly Claude usage. The article needs a real table: hours spent by category (ingest, prompt tuning, review, debugging), token spend by phase, hosting cost, total dollars, total person‑hours. Start logging retroactively now (memory plus git history) and prospectively going forward.
2. **Screenshots.** Section III (case study) needs four to six images: a case page, a topic page, the graph view, a wiki‑link cluster, the Recent tab, and the search UI. Capture these from `constitutionallaw.netlify.app` in a single session.
3. **A clean prompt library.** Professor flagged prompts as a core appendix. The prompts we used live across scheduled‑task configs, rubrics, and the `LESSONS.md` rules. They need to be extracted, deduplicated, and arranged by function (extraction, case note, doctrine, hypothetical, linking, review).
4. **Iteration before/after pair.** A side‑by‑side that shows the same vault page at skeleton, post‑Enrich, and post‑Verify, with the diff annotated. Use Trump v. United States (skeleton), Rehnquist Court Commerce Clause (mid‑cycle), Gonzales v. Raich (full). Those three are explicitly the staging examples in `email‑to‑chandler‑stages.md`.
5. **The Karpathy reference, done carefully.** The professor is right to be cautious. The actual primary source is Karpathy’s `autoresearch` repo and X/Twitter announcement on March 7, 2026: a 630‑line Python script that ran *50* experiments overnight (not 700) and discovered a learning‑rate improvement. The “11% efficiency gain” figure does not appear in primary sources I can verify and should be dropped. The “vibe coding” framing from his February 2, 2025 tweet is older and well‑documented. We cite the loop as a *concept*, not as a benchmark, and we describe what we adapted: the per‑phase rubric, the LESSONS file as memory, the rolling scorecard, the forced‑finding Verify pass.

---

## 4. Phased plan

Given the “flexible, quality over speed” timeline, I’d run six phases. Each phase has a single output. None bleeds into the next.

### Phase A. Evidence harvest (2 to 3 weeks)

Goal: get every artifact into a form the writing phase can pull from without rummaging.

- Extract the live prompt library from configs, rubrics, and `LESSONS.md` into `Appendix-Prompts.md`.
- Reconstruct the cost and time log from email trail, git log, and best‑memory entries; commit `Appendix-Cost-Log.md`.
- Capture the screenshots (six to eight images, 300 dpi, labeled by figure).
- Pull the Prize Cases / Grier story, the rubric‑split story, and the wiki‑link asymmetry story into a single `Iteration-Stories.md` that the writing phase can quote from.
- Build the side‑by‑side before/after pair (Trump skeleton → Rehnquist mid‑cycle → Raich full enrich). Save the markdown sources, not just renders, so the diff is inspectable.

Output: a `manuscript/` folder with raw materials and a one‑page memo on what evidence supports which section.

### Phase B. Outline lock and abstract (1 week)

Goal: lock the article’s shape before drafting prose.

- Adopt the professor’s 14‑section outline as the skeleton.
- Write a 250‑word abstract that states the thesis, the case study, the contribution, and the disclaimer about evaluation. Get the professor’s sign‑off on the abstract before writing further. If we can’t state the thesis in 250 words, we shouldn’t be writing 12,000.
- Draft the introduction (Section I) and Section X (generalization) first. Those are the load‑bearing rhetorical sections. If they land, the rest is mostly description.
- Decide footnote architecture (Bluebook 21st, per JLE’s submission guidelines).

Output: `abstract.md`, `section-01-intro.md`, `section-10-generalization.md`, all approved by the professor.

### Phase C. Body draft (4 to 6 weeks)

Goal: complete the full draft at 10,000 to 12,000 words.

Order of drafting (not order of appearance):

1. Section IV (input corpus) → Section V (Obsidian as intermediate layer) → Section VIII (vault to website). These are the most concrete. Drafting them first builds confidence.
2. Section III (case study). Use the live site and screenshots. Walk a reader from doctrine to case to hypothetical to cross‑links the way a student would.
3. Section VI (prompting as pedagogical design). Cite Qian and tie each prompt to a pedagogical move.
4. Section VII (professor‑in‑the‑loop adaptation of the Karpathy loop). Sober. Reproducible. The Prize Cases story anchors it.
5. Section IX (cost and labor). Tied to the cost log.
6. Section II (why ordinary infrastructure isn’t enough). Rubin and Mertz here, with restraint.
7. Section XI (evaluation). See §5 below for the recommended posture.
8. Section XII (risks and limits). Lead with the Magesh et al. Stanford hallucination findings. Then the static‑site‑is‑safer‑than‑chatbot table.
9. Section XIII (institutional implications). Short.
10. Section XIV (conclusion). Last.

Output: full first draft, all sections, every citation present in at least placeholder form.

### Phase D. Polish and unity pass (2 weeks)

Goal: turn 14 drafts into one article.

- Read the whole thing aloud. Cut anything that sounds like a product announcement.
- Insert the recurring sentence (some version of: *the system did not replace professorial judgment; it made that judgment reusable, inspectable, and publishable*) at three calibrated spots.
- Verify every citation against its primary source. Pull anything that fails a primary‑source check.
- Run a Bluebook 21st‑edition pass on footnotes.
- Verify all internal cross‑references.
- Tighten transitions between Sections II and III, VII and VIII, and XI and XII (the seams most likely to read as patched together).

### Phase E. External feedback (3 to 4 weeks, partly overlapping)

Three independent reads, sequentially:

1. The professor. Substantive and structural. Expect a round of revisions.
2. A clinical or legal‑writing faculty colleague who has not seen the project. Will catch the legal‑education‑specific framing that JLE readers will want.
3. A faculty colleague outside law (instructional design or learning sciences). Will catch the AI‑in‑education research framing in Sections VI, VII, XI.

Revise after each. Don’t bundle all three into one revision round.

### Phase F. Submission package (1 week)

- Final manuscript with abstract, body, footnotes.
- Online appendices (A through F) compiled.
- Cover letter to JLE editors framing the contribution.
- Submission via Scholastica.
- Optional: post a working‑paper version to SSRN concurrent with submission so the work is citable while review runs.

**Total realistic timeline if we work steadily but not heroically: about 14 to 19 weeks from start of Phase A.** With the flexible deadline, I’d build in a deliberate four‑week gap between Phases C and D for the draft to settle.

---

## 5. Recommendation on Section XI (evaluation)

You asked me to recommend. Here it is.

**Recommendation: Method plus light usability data.** Not method‑only. Not a full pilot study.

Three reasons:

1. **JLE’s audience expects evidence proportional to claims.** A method paper with no evidence is publishable. A method paper with modest, honest evidence is markedly stronger. The Bond et al. meta‑review explicitly calls for more rigor and ethics in AIHEd research; a paper that anticipates that critique with even a small data slice will weather peer review better.
2. **A structured pilot study is expensive, slow, and risks distorting the article.** Designing a pre/post quiz on one doctrinal cluster, getting IRB approval, recruiting students, controlling for prior preparation, and analyzing the data is a separate paper. If we try to fold it into this one, it either underdelivers as research or overshadows the method contribution.
3. **Light usability data is cheap and credible.** A 15‑question survey to the current Con Law I cohort about how they used the site (or didn’t), navigation traces from Netlify analytics, and three or four think‑aloud sessions with volunteer students. That generates a Section XI with real numbers, real quotations, and a clean disclaimer that learning outcomes were not measured. It tells JLE readers, in effect: *here is what students reported about how the site fit into their studying; the question of whether it improved performance is the subject of a follow‑up study.* That framing is JLE‑idiomatic.

A practical version of the light‑data plan:

- Add a brief, anonymous Qualtrics or Google Forms survey at the end of the semester (or already; depends on Con Law I calendar). Five Likert items on usefulness, navigation, trust, and overreliance, plus two open‑ended items.
- Pull Netlify analytics for page‑view counts by page type (case vs. topic vs. lecture), search terms used, and time on page. Anonymized.
- Conduct three to five 30‑minute think‑aloud sessions with volunteer students preparing for the exam. Ask them to find an answer to a doctrinal question using the site; record what they click and what they say.
- Frame all of it in Section XI as *usability and use pattern* data, never as learning outcomes data.

If the professor and the law school’s IRB administrator agree this is human subjects work, run it through IRB as exempt or expedited. If they disagree, conduct it as student‑experience feedback, not research, and label it as such in the article.

---

## 6. Open decisions for the professor (and you)

Issues I cannot resolve unilaterally and that affect drafting:

1. **Copyrighted casebook material.** None of the public‑facing pages should include verbatim casebook text. Confirm we are working only from the professor’s own slides and notes, public judicial opinions, public constitutional text, statutes, and original hypotheticals. Confirm whether any of the existing 198 pages currently include casebook quotation that would need to be removed before the site is held up as a model in JLE.
2. **Student work as input.** Confirm whether the professor’s past exam answers, office‑hours notes, or LMS posts were used as training input. If yes, we need a privacy section in Section IV and Section XII; if no, we should say so explicitly.
3. **Attribution and authorship.** Is this a single‑authored article or a co‑authored piece with Professor Chandler? Authorship reshapes the framing (especially Section VII), the “I/we” voice, and the institutional implications section.
4. **Public site as evidence vs. continuing experiment.** If the site keeps changing during peer review, snapshot the version that the article describes (a tagged release, or an archive.org capture) so the article and the artifact stay synchronized.
5. **Karpathy framing in the body text.** Do we call Section VII *“The Professor‑in‑the‑Loop Adaptation of the Karpathy Loop”* (clear, attribution‑honest, slightly tech‑lore‑y) or *“Iterative Improvement Under Professorial Control”* (more JLE‑idiomatic, drops the Karpathy name from the heading and confines it to a footnote)? I’d vote for the second, with Karpathy in the footnote, but it’s a judgment call.
6. **One last decision: do we want any artifact at all on JLE’s online supplement, or do we keep appendices in PDF with the manuscript?** JLE supports online supplements; we could host the prompt library and templates there.

---

## 7. Annotated bibliography

Organized by the article section it most directly serves. Each entry: full citation, what it does for us, and how to deploy it. Sources verified against primary records during this planning pass.

### Core: the Karpathy loop (Section VII)

- **Andrej Karpathy, *autoresearch* (GitHub repository), Mar. 7, 2026.** A 630‑line Python script that delegates the modify‑run‑evaluate‑keep‑or‑discard loop to an LLM agent. The release was accompanied by an X post that surfaced the project to the wider community and produced significant discussion. Deploy as the *concept* citation in Section VII. State plainly: 50 experiments overnight per Karpathy’s announcement; do not assert the “700 experiments” or “11% efficiency gain” numbers, which do not appear in the primary source we located. https://github.com/karpathy/llm-council and the autoresearch repo / announcement are the primary records. See secondary write‑ups for context: MindStudio explainer ([mindstudio.ai](https://www.mindstudio.ai/blog/karpathy-autoresearch-applied-to-claude-code-skills)); The New Stack ([thenewstack.io](https://thenewstack.io/karpathy-autonomous-experiment-loop/)).
- **Andrej Karpathy, “Vibe coding” thread, X / Twitter, Feb. 2, 2025.** Earlier, well‑documented framing for an AI‑guided iterative workflow. Useful as historical context one paragraph before introducing autoresearch. Cite via the secondary write‑up that quotes the original post: Klover.ai ([klover.ai](https://www.klover.ai/andrej-karpathy-vibe-coding/)).

### Knowledge graphs and RAG for education (Sections V, VI, VIII)

- **Chenxi Dong, Yimin Yuan, Kan Chen, Shupei Cheng & Chujie Wen, *How to Build an Adaptive AI Tutor for Any Course Using Knowledge Graph‑Enhanced Retrieval‑Augmented Generation (KG‑RAG)*, arXiv:2311.17696 (v7, Feb. 12, 2025).** Knowledge graphs outperformed pure semantic RAG in a controlled study (76 students; mean scores 6.37 vs. 4.71, p<0.001, Cohen’s d=0.86). Deploy in Section V to support the claim that *schema* (not just prose) is what makes AI‑authored notes pedagogically reusable. https://arxiv.org/abs/2311.17696.
- **Boci Peng, Yun Zhu, Yongchao Liu, Xiaohe Bo, Haizhou Shi, Chuntao Hong, Yan Zhang & Siliang Tang, *Graph Retrieval‑Augmented Generation: A Survey*, arXiv:2408.08921 (Aug. 15, 2024; later in ACM Transactions on Information Systems).** Defines the GraphRAG workflow: graph‑based indexing, graph‑guided retrieval, graph‑enhanced generation. Use to position the Obsidian vault as a manually‑maintained, professor‑supervised cousin of GraphRAG: the structure does retrieval work that pure semantic similarity cannot. https://arxiv.org/abs/2408.08921.

### Prompt engineering as pedagogy (Section VI)

- **Yufeng Qian, *Prompt Engineering in Education: A Systematic Review of Approaches and Educational Applications*, 63 J. Educational Computing Research 1782 (2025).** Distinguishes technique‑based and process‑based prompting strategies. Use to defend the claim that prompts are pedagogical artifacts, not tricks; map each prompt category in our library onto Qian’s typology. https://journals.sagepub.com/doi/abs/10.1177/07356331251365189.

### AI in higher education writ large (Sections XI, XII)

- **Melissa Bond, Hassan Khosravi, Maarten De Laat, Nina Bergdahl, Violeta Negrea, Emily Oxley, Phuong Pham, Sin Wang Chong & George Siemens, *A meta systematic review of artificial intelligence in higher education: a call for increased ethics, collaboration, and rigour*, 21 Int’l J. Educational Tech. Higher Educ., Art. 4 (2024).** Meta‑review of 66 publications; key conclusion is the need for more methodological and ethical rigor in AIHEd research. Deploy as the field‑level frame for Sections XI and XII: this article *anticipates* Bond et al.’s critique by disclaiming learning‑outcomes claims and including the risk catalogue. https://link.springer.com/article/10.1186/s41239-023-00436-z.
- **Ramteja Sajja, Yusuf Sermet, David M. Cwiertny & Ibrahim Demir, *Platform‑independent and curriculum‑oriented intelligent assistant for higher education*, 20 Int’l J. Educational Tech. Higher Educ., Art. 42 (2023).** A working example of a curriculum‑specific AI assistant. Use as a contrast in Section III: their system is a chatbot that answers students’ questions; ours is a reviewed static site that students browse. Different risk profile, different pedagogical commitments. https://link.springer.com/article/10.1186/s41239-023-00412-7.

### Legal AI accuracy and hallucination (Section XII)

- **Varun Magesh, Faiz Surani, Matthew Dahl, Mirac Suzgun, Christopher D. Manning & Daniel E. Ho, *Hallucination‑Free? Assessing the Reliability of Leading AI Legal Research Tools*, J. Empirical Legal Studies (2025), pre‑print arXiv:2405.20362.** Even well‑curated commercial legal RAG systems (Lexis+ AI, Westlaw AI‑Assisted Research, Ask Practical Law AI) hallucinate citations 17% to 33% of the time. This is the strongest cite available for the article’s core risk argument and the static‑site‑is‑safer‑than‑chatbot table. https://onlinelibrary.wiley.com/doi/full/10.1111/jels.12413.
- **Mata v. Avianca, Inc., 678 F. Supp. 3d 443 (S.D.N.Y. 2023) (Castel, J.).** Rule 11 sanctions for filing six fabricated AI‑generated cases. Use in Section XII as a one‑sentence reminder of why hallucination is not a hypothetical concern, and as a teaching‑connection: students who internalize a no‑verify habit through AI tools will repeat the Schwartz error in practice.

### Legal pedagogy: the casebook tradition (Section II)

- **Edward Rubin, *What’s Wrong with Langdell’s Method, and What to Do About It*, 60 Vand. L. Rev. 609 (2007).** Argues that legal education has used essentially the same Langdellian model since the 1870s despite enormous changes in law, practice, theory, and pedagogy. Deploy as the long‑range frame for Section II: course knowledge systems are not a critique of the casebook; they are infrastructure the casebook never had.
- **Elizabeth Mertz, *The Language of Law School: Learning to “Think Like a Lawyer”* (Oxford Univ. Press 2007).** Ethnographic study of 1L Contracts classrooms. Deploy briefly in Section II to support the observation that a great deal of what a professor *teaches* is performed in real time and never captured in the LMS or casebook. The course knowledge system is one way to make that performance reusable.
- **Jamie R. Abrams, *Reframing the Socratic Method*, 64 J. Legal Educ. 562 (2015).** Recent JLE piece on adapting traditional pedagogy. Use as a tone reference and as a citation for the proposition that JLE welcomes structured arguments for pedagogical reform.

### Recent JLE work on AI (multiple sections, especially I and XI)

- **Jonathan H. Choi & Daniel Schwarcz, *AI Assistance in Legal Analysis: An Empirical Study*, 73 J. Legal Educ. 384 (2025).** GPT‑4 helps weak students more than strong students on law‑school exams, with a potential equalizing effect. The strongest recent piece in JLE’s house on AI and law‑school learning. Cite in Section I as part of the current conversation and in Section XI as evidence that meaningful empirical work in JLE on AI is possible without being a full RCT. https://jle.aals.org/home/vol73/iss2/5/.

### Cognitive science of learning (Section X)

- **Saadiq F. Usman, *Making Legal Education Stick: Using Cognitive Science to Help Law Students Learn*, Legal Writing Inst. (2018), https://www.lwionline.org/sites/default/files/2018-06/Usman%20Making%20Legal%20Education%20Stick.pdf.** Applies cognitive‑load theory, worked examples, and spaced retrieval to law‑school teaching. Cite in Section X to support the claim that doctrinal courses share a learnable structure (rule, exception, application) that maps cleanly onto note types in a vault.

### Open educational resources in law (Section XIII)

- **Harvard Library & MIT Press, *H2O Open Casebooks* and **CALI’s eLangdell Press*.** Existing OER infrastructure for legal education. Cite in Section XIII to position the course knowledge system as complementary OER infrastructure: H2O publishes texts, this method publishes the structure around texts. See https://opencasebook.org and https://www.cali.org/the-elangdell-bookstore.

### JLE practice and submissions

- **Journal of Legal Education, Submissions Page.** Bluebook 21st ed. for citation form. Submissions via Scholastica. Editorial decisions typically within two to three weeks of submission; empirical work may go to outside peer review and take longer. No published word cap. https://jle.aals.org/home/submissions.html.

---

## 8. What I recommend we do this week

Three concrete starts, all low effort:

1. **Capture screenshots now.** Six to eight images from `constitutionallaw.netlify.app` at 300 dpi. Once we touch the site again the captures may not match the article.
2. **Start the cost log.** A single markdown file. Backfill what you remember; add a daily one‑line entry going forward.
3. **Write the 250‑word abstract first.** If it lands, the rest is mostly description. If it doesn’t, we know we need to think more about the thesis before drafting 12,000 words.

After those three, the rest of Phase A can run in parallel with Phase B.

---

## 9. Appendices to plan for

Per Professor Chandler’s recommendation, build these as we go rather than at the end:

- **Appendix A.** Input inventory (counts and categories of source materials; sample names).
- **Appendix B.** Prompt library (extraction, case note, doctrine, hypothetical, linking, review, publication).
- **Appendix C.** Obsidian note templates (frontmatter, sections, sample wiki‑link patterns).
- **Appendix D.** Karpathy‑loop rubric (the per‑phase rubric criteria that drive scoring).
- **Appendix E.** Cost and time log.
- **Appendix F.** Technical setup (Obsidian → markdown → static site generator → Git → Netlify).

Online supplements at JLE can carry these; we should not let the print word count balloon to host them.

---

## 10. The one sentence

When the article needs to remind the reader what it is for, I think this is the right sentence. Adjust to taste.

> This article describes a method for turning a law professor’s scattered course archive into a structured, cross‑linked, student‑facing course knowledge system. The method uses generative AI, but its essential feature is not automation. Its essential feature is iteration under professorial control.

Use it once in the introduction. Once at the seam between Section VII (the loop) and Section VIII (publication). Once in the conclusion. No more.
