---
id: "12"
title: "Risks and Limits"
status: needs_cite
target_words: 800
word_count: 0
last_phase: draft
draft_status: needs_cite
draft_completed_at: 2026-05-23T07:00:00Z
evidence_cards:
  - evidence-12-magesh-hallucination-findings
  - evidence-12-mata-v-avianca-rule-11-sanctions
  - evidence-12-static-vs-chatbot-risk-architecture
  - evidence-12-static-not-chatbot-operational-card
  - evidence-12-copyrighted-casebook-material-risk
  - evidence-12-curriculum-grounding-corpus-incompleteness
  - evidence-12-student-work-as-input-privacy
  - evidence-12-public-site-continuing-experiment-snapshot
  - evidence-12-equity-accessibility-cross-section-convergence
  - evidence-12-bond-aihed-rigor-frame-risks
  - evidence-12-recurring-sentence-not-here
---

# Section XII. Risks and Limits

## 12.A The lead anchor: hallucination findings and the practitioner-side consequence

The article’s risk argument begins with what the published literature has measured. Magesh and colleagues report that three leading commercial legal retrieval-augmented-generation systems (Lexis+ AI, Westlaw AI-Assisted Research, and Ask Practical Law AI) hallucinate citations at rates between seventeen and thirty-three percent, drawn from products whose proprietary corpora and curation budgets exceed anything available to a course knowledge system.[CITE: evidence-12-magesh-hallucination-findings] What transfers from that finding to this article’s setting is the empirical foundation that hallucination in well-curated legal AI is a measured fact rather than a hypothetical concern; what does not transfer is the runtime-generation pipeline on which the evaluation depends, because the architecture this article describes has no runtime generation surface for hallucination to occur on. The practitioner-side consequence is documented in Mata v. Avianca, Inc., where Judge Castel imposed Rule 11 sanctions on counsel who filed a brief containing six fabricated AI-generated cases; students who internalize a no-verify habit through their AI tools will repeat that error once they reach practice.[CITE: evidence-12-mata-v-avianca-rule-11-sanctions]

## 12.B The architectural contrast and the discipline that organizes its prose

The architectural contrast organizes the rest of the catalogue. The case study is a reviewed static website on which every page was professorially inspected before publication; the chatbot-tutor alternative generates responses at runtime against a corpus and surfaces the generated text without prior review.[CITE: evidence-12-static-vs-chatbot-risk-architecture] The contrast holds along four axes: review timing (build-time inspection versus runtime generation), error surface (a stable, citeable, URL-addressable page versus an ephemeral response that re-rolls each session), update mechanism (a versioned commit with an audit trail versus an opaque retrieval-and-generation pipeline), and accountability surface (a named professor who owns each published page versus a system whose outputs no one signed).

The contrast does not claim the case study is risk-free; the risk surface differs in kind and lives elsewhere in the pipeline. Per-page professorial inspection scales linearly with vault size and caps the rate at which the system can grow; a static page cannot adapt to a question the professor did not anticipate, an affordance the chatbot architecture would address differently; the doctrinal map the system encodes is the professor’s commitment, and a student who internalizes that map without contesting it loses the live Socratic contest; and an error that ships to the public site is harder to retract than an ephemeral response.[CITE: evidence-12-static-vs-chatbot-risk-architecture]

The chatbot-tutor evaluation vocabulary (response quality, conversational coherence, tutor accuracy, engagement turns, dialogue-state tracking) appears here only as named features of the contrast architecture, not as silent vocabulary for the case study’s surface; the case study publishes, surfaces, indexes, and links pages a professor reviewed.[CITE: evidence-12-static-not-chatbot-operational-card]

## 12.C Casebook material and the corpus completeness question

The workplan flags two open decisions on the corpus side. The first is copyrighted casebook material: no public-facing page should include verbatim casebook text, and the case study works only from professor-prepared slides and notes, public judicial opinions, public constitutional text, statutes, and original hypotheticals.[CITE: evidence-12-copyrighted-casebook-material-risk] Whether any of the existing one hundred ninety-eight deployed pages currently include casebook quotation that would need to be removed is an audit pending professorial review; the article reports the forward rule and the backward audit together as a single catalogue entry.

The architectural implication is that the curriculum-grounding claim the article develops elsewhere applies to the course-issued layer (lecture decks, professor-prepared opinion PDFs, merged reading packets, practice exams, teaching guides) rather than to the full reading load the casebook also supplies.[CITE: evidence-12-curriculum-grounding-corpus-incompleteness] The contrast is sharpest precisely because the reviewed static website does not retrieve casebook text in response to a runtime query; the work happens at build time against the corpus the professor authored or curated. A future replication on a different course may ingest casebook excerpts under a license that permits it.

## 12.D Privacy and the snapshot commitment

The second corpus-side open decision is whether the professor’s past exam answers, office-hours notes, or LMS posts served as training input. If they did, the article reports a separate privacy discipline covering FERPA-compliant data handling, Institutional Review Board review when appropriate, and consent, anonymization, and retention protocols; if they did not, the article says so explicitly. A parallel use-side surface lives independently of the input decision: PostHog analytics on the deployed site respects Do Not Track and disables session recording, as Section VIII discloses.[CITE: evidence-12-student-work-as-input-privacy]

The publication-side snapshot rests on four commitments: a tagged release of the source repository at the manuscript’s snapshot date, an archive.org capture of the deployed pages at the same date, a canonical-reference commitment that the article cites the tagged version rather than the live HEAD, and an explicit posture that continued evolution after the snapshot is the intended state rather than a drift to be repaired.[CITE: evidence-12-public-site-continuing-experiment-snapshot]

## 12.E Equity, accessibility, and the field-level frame

Four upstream sections previously deferred to Section XII for the equity-and-accessibility argument. Five commitments anchor the treatment: the deployed single-page application presupposes broadband and a modern browser; the hash-route navigation, search palette, and holding-bar banner leave screen-reader behavior as an open testing question; the three-hundred-dpi modernized PDFs assume sufficient device rendering; the Canvas enrollment gate restricts input-side access to currently enrolled students; and the PostHog analytics surface respects Do Not Track with session recording disabled. The contribution here is disclosure rather than solution, with WCAG conformance testing, alt-text discipline, and screen-reader auditing named as investments a replication would add and this case study did not make.[CITE: evidence-12-equity-accessibility-cross-section-convergence]

Bond and colleagues’ meta-systematic review of sixty-six AI-in-higher-education publications calls for greater ethics and rigor in the field; the risk catalogue here anticipates that call.[CITE: evidence-12-bond-aihed-rigor-frame-risks] What transfers is the ethics-and-rigor critique that applies to any AI-in-higher-education system; what does not is the implementation surface, because the cited corpus is predominantly chatbot-tutor and learning-management-system interventions while this article addresses a reviewed static website with no runtime generation surface.
