---
id: "12"
title: "Risks and Limits"
status: needs_cite
target_words: 800
word_count: 879
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

## 12.A The empirical anchor and the practitioner-side consequence

Magesh and colleagues evaluated three commercial legal retrieval-augmented-generation systems, Lexis+ AI, Westlaw AI-Assisted Research, and Ask Practical Law AI, and reported that each hallucinated citations between seventeen and thirty-three percent of the time despite proprietary case-law and treatise grounding.[CITE: evidence-12-magesh-hallucination-findings] What transfers from that finding is the empirical proposition that runtime generation against a curated legal corpus does not eliminate hallucination at rates compatible with professionally responsible practice; what does not transfer is the implementation surface, because the case study publishes inspected pages from a build-time pipeline rather than answering reader queries at runtime. The practitioner-side cost of a no-verify habit is documented and sanctionable, as Mata v. Avianca, Inc. illustrates in the form of Rule 11 sanctions for filing six fabricated AI-generated citations.[CITE: evidence-12-mata-v-avianca-rule-11-sanctions] A student who internalizes that habit in law school will carry it into practice, which is one reason a course knowledge system that habituates verification at the case-brief level matters pedagogically.

## 12.B The architectural contrast and the discipline that organizes its prose

The risk profile of the case study differs structurally from the chatbot-tutor alternative along four axes.[CITE: evidence-12-static-vs-chatbot-risk-architecture] A reviewed static website is inspected by the professor before any page reaches a reader; a curriculum-grounded chatbot such as Sajja and colleagues’ platform-independent intelligent assistant generates responses at runtime against a corpus with no human in the loop. The contrast holds at review timing (build-time inspection rather than runtime generation), error surface (an inspected artifact citeable to a specific page rather than an ephemeral response re-rolled each session), update mechanism (a versioned commit under the same review pipeline rather than re-generation), and accountability surface (a named professor signs each page rather than a system whose outputs no one signed). What transfers is the structural difference in review timing and error surface; what does not transfer is a claim that the case study is risk-free.

The reviewed-static-website architecture has its own risk surface. Professorial review scales linearly with vault size, which caps growth. The static page cannot adjust to an individual student’s confusion the way a conversational system could in principle. The doctrinal map the artifact encodes is the professor’s commitment, and a student who internalizes it without contesting it loses some of the live Socratic contest. An error that survives review and ships to the public site is harder to retract than an ephemeral response.

The Section keeps each architecture in its own vocabulary. The chatbot-tutor architecture answers, responds, generates, retrieves, and replies; the case study’s architecture publishes, surfaces, indexes, links, and displays.[CITE: evidence-12-static-not-chatbot-operational-card]

## 12.C The casebook discipline and the corpus-completeness implication

The first of the workplan’s open-decision risks is copyrighted casebook material. The case study works only from professor-prepared slides and notes, public judicial opinions, public constitutional text, statutes, and original hypotheticals; none of those input categories includes verbatim casebook text.[CITE: evidence-12-copyrighted-casebook-material-risk] A backward-looking audit of the pages on the snapshot date is pending professorial review, and any page found to contain casebook quotation will be remediated before the site is held up as a model in this Journal’s pages.[CITE: forward reference to the workplan §6.1 backward audit; see PI-073]

The architectural implication is that the curriculum-grounded retrieval claim the article develops elsewhere applies to the course-issued layer rather than to the full reading load.[CITE: evidence-12-curriculum-grounding-corpus-incompleteness] The static-versus-chatbot contrast is sharpest precisely here: a reviewed static website published from a structured corpus does not need to ingest the casebook to do its work, because the work happens at build time against the materials the professor authored or curated. A future replication may ingest casebook excerpts under license; the case study’s object is the course-issued layer at the input side and the inspected publication at the output side.

## 12.D Privacy and the snapshot commitment

The second open-decision risk is student work as input. The article’s current posture, pending professorial confirmation, is that no student work was used as training input to the vault.[CITE: evidence-12-student-work-as-input-privacy; see PI-002] Either resolution produces the same discipline rule for a future replication: any system that ingests student work needs FERPA-compliant handling, Institutional Review Board review where appropriate, and consent and anonymization protocols. The deployed site’s analytics configuration, with Do Not Track respected and session recording disabled, is the parallel use-side commitment.[CITE: forward reference to Section VIII analytics-configuration footnote]

The fourth open-decision risk is the public-site-as-evidence question. The article commits to four anchors: a Git tag at the manuscript’s snapshot date, an archive.org capture of the deployed pages, a canonical-reference commitment that the article cites the tagged version rather than the live deployment, and a continued-evolution-as-intended posture that distinguishes the snapshot from the site’s growth after submission.[CITE: evidence-12-public-site-continuing-experiment-snapshot]

## 12.E Equity, accessibility, and the field-level frame

The Section consolidates the article’s equity-and-accessibility commitments at five points: the deployed single-page application presupposes broadband and a modern browser; the hash-route navigation raises open screen-reader questions the case study did not test against a conformance standard; the three-hundred-dpi modernized opinion PDFs assume a device capable of high-resolution rendering; the input corpus is gated by Canvas enrollment; and the analytics configuration is the disclosed privacy stance.[CITE: evidence-12-equity-accessibility-cross-section-convergence] The contribution at this altitude is disclosure rather than solution. Bond and colleagues’ meta-systematic review of sixty-six artificial-intelligence-in-higher-education publications places the article inside the field’s own ethics-and-rigor call rather than against it; what transfers is the commitment to honest risk disclosure, and what does not transfer is the chatbot-tutor and learning-management-system implementation surface that predominates in the cited corpus.[CITE: cross-section reuse to evidence-12-bond-aihed-rigor-frame-risks and Section XI Bond footnote per L-034]
