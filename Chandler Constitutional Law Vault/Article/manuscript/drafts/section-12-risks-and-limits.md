---
id: "12"
title: "Risks and Limits"
status: needs_cite
target_words: 800
word_count: 914
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

The empirical anchor for this section's risk argument is Magesh and colleagues' 2025 study of three leading commercial legal retrieval-augmented-generation systems, Lexis+ AI, Westlaw AI-Assisted Research, and Ask Practical Law AI, which hallucinate legal citations between seventeen and thirty-three percent of the time despite being well-curated commercial products grounded against proprietary case-law and treatise corpora.[CITE: evidence-12-magesh-hallucination-findings] What transfers to the case study described in this article is the abstract risk that well-curated legal retrieval-augmented generation can still hallucinate at rates incompatible with professionally responsible practice; what does not is the instrumentation, because the three-system evaluation method has no purchase on a reviewed static website that performs no runtime generation. The practitioner-side consequence is Mata v. Avianca, in which the Southern District of New York imposed Rule 11 sanctions for filing a brief containing six fabricated AI-generated cases.[CITE: evidence-12-mata-v-avianca-rule-11-sanctions] Students who internalize a no-verify habit through generative-AI tools will repeat the Schwartz error once they reach practice; a course knowledge system that habituates verification at the case-brief level matters for that reason.

## 12.B The architectural contrast and the discipline that organizes its prose

The architectural contrast organizes the rest of the section. A chatbot-tutor generates text against a corpus at runtime and the user sees the output without prior professorial review; a reviewed static website produces content at build time by professorial authoring and review, and the user sees only content that was inspected before publication.[CITE: evidence-12-static-vs-chatbot-risk-architecture] The contrast holds along four axes: review timing (publication-time professorial pass versus runtime generation), error surface (errors stable and addressable to a page versus errors ephemeral and re-rolled each session), update mechanism (versioned commits to a repository versus opaque retrieval-and-generation), and accountability surface (a named professor versus a system whose outputs no one signed). The Magesh hallucination rate describes the chatbot pipeline's runtime risk surface; the reviewed-static-website architecture has no equivalent generation surface.

The contrast is not that the case study is risk-free. Review scales linearly with vault size, which caps the rate at which the system can grow without compromising the discipline. A static artifact cannot adapt to a particular student's confusion the way a conversational tutor could in principle, a real pedagogical loss. The structural prose tells the reader what to think is doctrinally important, and the structure carries pedagogical commitments the professor must own. Publication bakes errors into a public artifact, which raises the cost of correction relative to a chatbot whose answer is ephemeral.

The prose discipline that organizes the section follows from the contrast. Chatbot-tutor evaluation vocabulary (response quality, conversational coherence, tutor accuracy, engagement turns) appears here as named features of the contrast architecture rather than as vocabulary for the case study's own risk surface; verbs the section uses for the chatbot architecture (answers, responds, generates, retrieves, adapts) do not transfer to the case study's static artifact, which publishes, surfaces, indexes, links, and exposes.[CITE: evidence-12-static-not-chatbot-operational-card]

## 12.C Casebook material and the corpus completeness question

Two open decisions from the case study's project workplan land here as named risks. The first is copyrighted casebook material. The case study works only from the professor's own slides and notes, public judicial opinions, public constitutional text, statutes, and original hypotheticals; whether any existing pages on the current corpus snapshot include casebook quotation that would need to be removed before the site is held up as a model in this Journal is a backward audit pending the professor's review.[CITE: evidence-12-copyrighted-casebook-material-risk] The architectural implication is that the article asserts curriculum-grounded retrieval as a load-bearing transfer-of-inference, so the case study's curriculum-grounding claim applies to the course-issued layer (lecture decks, professor-prepared opinion PDFs, merged reading packets, practice exams, teaching guides) rather than to the full reading load. The reviewed-static-website architecture does not need to retrieve casebook text in response to a runtime query, because the work happens at build time against the corpus the professor has authored or curated; a future replication of the method on a different course may ingest casebook excerpts under license.[CITE: evidence-12-curriculum-grounding-corpus-incompleteness]

## 12.D Privacy and the snapshot commitment

Privacy lives at two surfaces. On the input side, no past student exam answers, office-hours notes, or LMS posts were used as training input to the vault, pending the professor's written confirmation; a future replication that ingests student work would require FERPA-compliant data handling, Institutional Review Board review where appropriate, and consent and anonymization protocols the case study did not need to build.[CITE: evidence-12-student-work-as-input-privacy] On the use side, the deployed site uses PostHog with Do Not Track respected and session recording disabled. The publication-side snapshot answers the public-site-as-evidence-versus-continuing-experiment question with four commitments: a Git tag at the manuscript's snapshot date, an archive.org Wayback Machine capture of the deployed site at that date, a canonical-reference commitment that the article cites the tagged version rather than the live HEAD, and an explicit continued-evolution-as-intended posture distinguishing the snapshot the article relies on from the site's growth after submission.[CITE: evidence-12-public-site-continuing-experiment-snapshot]

## 12.E Equity, accessibility, and the field-level frame

The deployed single-page application presupposes broadband-quality access and a modern browser; the hash-route URL structure, the command-K search palette, and the holding-bar banner block leave open screen-reader and keyboard-navigation testing questions; the modernized PDFs assume a device that can render high-resolution image content; Canvas enrollment gates the input corpus to currently enrolled students.[CITE: evidence-12-equity-accessibility-cross-section-convergence] Bond and colleagues' 2024 meta-systematic review of sixty-six artificial-intelligence-in-higher-education publications calls for greater ethics and rigor across the field; the risk catalogue assembled above is built to that bar by disclosing access assumptions, refusing the rhetoric that names any system risk-free, and placing the case study inside the field's own self-critique. What transfers from Bond is the ethics-and-rigor commitment; what does not is the implementation surface, because Bond's corpus is predominantly chatbot-tutor and learning-management-system interventions and the case study studies a reviewed static website.[CITE: evidence-12-bond-aihed-rigor-frame-risks]
