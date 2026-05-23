---
id: "12"
title: "Risks and Limits"
status: needs_cite
target_words: 800
word_count: 880
last_phase: draft
draft_status: needs_cite
cite_status: none
polish_status: none
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

## 12.A The empirical anchor and the practitioner-side consequence

The risk argument leads with a quantified finding. Magesh and colleagues report that three leading commercial legal retrieval-augmented-generation systems, Lexis+ AI, Westlaw AI-Assisted Research, and Ask Practical Law AI, hallucinate citations between seventeen and thirty-three percent of the time, a rate that persists despite each system being a well-curated product built specifically for legal research against proprietary case-law and treatise corpora.[CITE: evidence-12-magesh-hallucination-findings] What generalizes from that finding to the case study is the demonstration that even careful curation does not, by itself, prevent runtime hallucination in a generative-AI pipeline; what does not transfer is the implementation surface, because the case study is a reviewed static website rather than a commercial legal-research product. Mata v. Avianca is the one-sentence practitioner-side reminder that hallucination is not hypothetical: Judge Castel imposed Rule 11 sanctions on counsel for filing six fabricated AI-generated citations, and the pedagogical concern is that students who internalize a no-verify habit in school will repeat the error in practice.[CITE: evidence-12-mata-v-avianca-rule-11-sanctions]

## 12.B The architectural contrast and the discipline that organizes the prose

The architectural argument that follows the Magesh anchor turns on a contrast between two production pipelines. A chatbot-tutor generates responses at runtime against a corpus, and the student sees that text without prior review; a reviewed static website publishes pages at build time after professorial inspection, and the student sees only content that passed review before reaching the browser.[CITE: evidence-12-static-vs-chatbot-risk-architecture] The contrast holds at four points: review timing (build-time inspection versus runtime generation), error surface (a published artifact that can be audited and corrected versus a response that is ephemeral and re-rolled on each session), update mechanism (a versioned redeploy versus a regeneration under the same uninspected pipeline), and accountability (a named professor and author own each published page versus a system whose responses no one signed).

The static architecture is not risk-free; it concentrates risk in different parts of the pipeline, and the article names those parts honestly. Review scales linearly with vault size, so a careful professorial pass on every page bounds the system’s growth rate. The static artifact cannot adapt to a student question the professor did not anticipate, an interactivity affordance the chatbot pipeline offers in principle. The doctrinal map the system encodes is the professor’s commitment, and a student who internalizes the map without contest loses the live Socratic challenge. Errors that pass review and ship to the public site are harder to retract than ephemeral chatbot responses are to revise.[CITE: evidence-12-static-vs-chatbot-risk-architecture] The prose discipline this subsection enforces is that the chatbot vocabulary (answers, responds, generates, retrieves) describes the contrast object and does not migrate to the case study, whose architecture publishes, surfaces, indexes, and exposes.[CITE: evidence-12-static-not-chatbot-operational-card]

## 12.C Casebook material and the corpus completeness question

The first workplan open decision concerns copyrighted casebook material. The forward-looking rule is that no public-facing page includes verbatim casebook text; the case study works only from professor-prepared slides and notes, public judicial opinions, public constitutional text, statutes, and original hypotheticals. The backward-looking audit, whether any of the existing pages currently includes casebook quotation that would need to be removed before the site is held up as a model, is open pending professorial review.[CITE: evidence-12-copyrighted-casebook-material-risk; see PI-073] The architectural implication that the Section IV hedge defers to lands here: the curriculum-grounded retrieval claim Section V and Section VIII develop applies to the course-issued layer of slides, lectures, indexed opinions, and professor-authored hypotheticals rather than to the full reading load that also includes the assigned casebook, and the static-website architecture has no runtime retrieval surface that would need to ingest the casebook to do its work; a future replication of the method on a different course may ingest casebook excerpts under a license that permits it.[CITE: evidence-12-curriculum-grounding-corpus-incompleteness; see PI-063]

## 12.D Privacy and the snapshot commitment

The second workplan open decision concerns student work as input. If no student exam answers, office-hours notes, or LMS posts were used as training input, the article says so explicitly; if any were used, the article carries a separate privacy paragraph naming FERPA-compliant handling, IRB review when appropriate, consent and anonymization protocols, and separate retention rules.[CITE: evidence-12-student-work-as-input-privacy; see PI-002] The deployed site’s analytics surface is the parallel use-side row of the privacy catalogue, with PostHog configured to respect Do Not Track and to disable session recording per Section VIII’s deployment record. The fourth workplan open decision concerns the public site as evidence rather than continuing experiment: the article names four snapshot commitments so the manuscript and the artifact remain synchronized, namely a Git tag at the snapshot date, an archive.org capture of the deployed pages at that date, a canonical-reference commitment to the tagged version rather than the live HEAD, and an explicit posture that continued evolution after the snapshot is intended.[CITE: evidence-12-public-site-continuing-experiment-snapshot]

## 12.E Equity, accessibility, and the field-level frame

Four prior sections defer their equity-and-accessibility acknowledgment here, and the substantive treatment is disclosure of what the case study assumes rather than a claim to have solved the access problem.[CITE: evidence-12-equity-accessibility-cross-section-convergence] The deployed single-page application presupposes broadband and a modern browser; hash-route navigation and the command-K search palette carry open screen-reader questions; 300-dpi modernized PDFs assume rendering capacity; Canvas enrollment gates the input corpus; and the analytics configuration is privacy-disciplined by design. Bond and colleagues’ field-level call for greater ethics and rigor in AI-in-higher-education research is the frame the section closes on, placing the article inside that field’s self-critique and naming that the risk surface a reviewed-static-website intervention raises is partially shared with and partially distinct from the chatbot-tutor and LMS-integration corpus the Bond review predominantly covers.[CITE: evidence-12-bond-aihed-rigor-frame-risks]
