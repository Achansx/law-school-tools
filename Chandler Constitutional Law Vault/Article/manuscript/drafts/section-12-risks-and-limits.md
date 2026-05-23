---
id: "12"
title: "Risks and Limits"
status: needs_cite
target_words: 800
word_count: 863
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

## 12.A The empirical anchor and its practitioner-side cost

Even well-curated commercial legal research systems fabricate citations at rates that would be disqualifying in practice. A 2025 study in the Journal of Empirical Legal Studies found that three leading commercial legal retrieval-augmented-generation products, Lexis+ AI, Westlaw AI-Assisted Research, and Ask Practical Law AI, hallucinated legal citations between seventeen and thirty-three percent of the time despite being purpose-built for legal research.[CITE: evidence-12-magesh-hallucination-findings] What transfers to this article is the insight that runtime generation against a curated legal corpus still fabricates citations at rates incompatible with responsible work; what does not transfer is the study’s evaluation instrument, because the case study is a reviewed static website with no runtime generation surface on which a hallucination can occur. The consequence is documented and sanctionable: a federal court imposed Rule 11 sanctions on an attorney who filed a brief containing fabricated, AI-generated case citations.[CITE: evidence-12-mata-v-avianca-rule-11-sanctions] A student who internalizes a no-verify habit through classroom AI tools will repeat that error in practice, which is why an architecture that front-loads verification before publication carries a pedagogical claim and not merely a safety one.

## 12.B The architectural contrast and its own risk surface

That hallucination surface belongs to a particular architecture, and the case study does not share it. A chatbot tutor of the kind the artificial-intelligence-in-higher-education literature describes generates a response at runtime against a corpus, and a student reads that generated text without any prior human review; a reviewed static website is authored and inspected at build time, and a student reads only pages a professor has already examined.[CITE: evidence-12-static-vs-chatbot-risk-architecture] The contrast holds along four axes.

| Axis | Chatbot-tutor architecture | Reviewed static website |
|------|----------------------------|-------------------------|
| Review timing | Runtime generation, no human in the loop | Publication-time professorial inspection |
| Error surface | Ephemeral, re-rolled each session | Stable, addressable, and citable to a page |
| Update mechanism | Opaque retrieval and regeneration | Versioned commits to a public repository |
| Accountability | A system no one signed | A named professor and author |

The contrast is structural, not a claim that the case study is risk-free. The reviewed static architecture carries its own risks: a reviewer moving quickly across many pages may miss what a slower pass would catch, so review scales differently than generation; a published page cannot adapt to a question the professor did not anticipate, which forfeits an affordance the chatbot architecture offers; the doctrinal structure the site encodes is itself a pedagogical commitment the professor must own; and an error that survives review and ships to a public page is harder to retract than an ephemeral answer.[CITE: evidence-12-static-vs-chatbot-risk-architecture] The contrast survives only if each architecture is described in its own terms: a chatbot tutor generates, retrieves, and responds at runtime, while a reviewed static site publishes, indexes, and is inspected before release, and collapsing the two vocabularies would erase the distinction the risk argument depends on.[CITE: evidence-12-static-not-chatbot-operational-card]

## 12.C Casebook material and the corpus-completeness question

None of the public-facing pages should carry verbatim casebook text. The case study works only from professor-prepared slides and notes, public judicial opinions, the constitutional text, statutes, and original hypotheticals, and whether any pages already published from the corpus contain casebook quotation that would need removal before the site is offered as a model remains pending the professor’s page-by-page review.[CITE: evidence-12-copyrighted-casebook-material-risk] That exclusion carries an architectural consequence the article owns rather than hides. The article asserts curriculum-grounded retrieval as a load-bearing inheritance from the structure-aware-retrieval literature, but a system that does not ingest the assigned casebook grounds itself in the course-issued layer, the slides, lectures, indexed opinions, and professor-authored hypotheticals, rather than in the full reading load.[CITE: evidence-12-curriculum-grounding-corpus-incompleteness] The static architecture needs no runtime retrieval against the casebook to do its work, because that work happens at build time against the corpus the professor authored or curated; a future replication on a different course could ingest casebook excerpts under a license that permits it.

## 12.D Privacy and the snapshot commitment

Two further open decisions belong to the professor, and the article hedges each pending confirmation while naming the discipline either answer requires. On the input side, if past exam answers, office-hours notes, or learning-management-system posts were used as input to the vault, a privacy regime applies, namely FERPA-compliant handling, consent, anonymization, and appropriate Institutional Review Board review; if none was used, the article says so, and the method should not ingest student work elsewhere without that regime in place.[CITE: evidence-12-student-work-as-input-privacy] On the use side, the deployed site’s analytics are configured to respect Do Not Track and to disable session recording, a posture that still records use-pattern data from current readers. The deployed site is also a continuing experiment, so the article fixes the version it describes with a tagged repository release and an archive.org capture at the snapshot date, cites that tagged version rather than the live site, and treats the site’s continued growth after submission as expected rather than as drift.[CITE: evidence-12-public-site-continuing-experiment-snapshot]

## 12.E Equity, accessibility, and the field-level frame

The architecture makes access assumptions the article discloses rather than solves. The deployed single-page application presupposes a modern browser and a broadband-quality connection; its hash-route navigation and search palette leave open screen-reader questions; the modernized opinion PDFs assume a device that can render high-resolution images; and the Canvas gate restricts the inputs to enrolled students, though the structured prose layer is exposed publicly.[CITE: evidence-12-equity-accessibility-cross-section-convergence] A replication could address each with the WCAG conformance testing, alt-text discipline, and screen-reader auditing the case study did not undertake. Bond and colleagues’ 2024 meta-review of sixty-six artificial-intelligence-in-higher-education studies calls for greater ethics and rigor across the field; that call reaches any such system, a reviewed static website included, even though its corpus is built predominantly on chatbot-tutor and learning-management-system interventions rather than reviewed static artifacts. This catalogue is written to meet that critique rather than to deflect it.[CITE: evidence-12-bond-aihed-rigor-frame-risks]
