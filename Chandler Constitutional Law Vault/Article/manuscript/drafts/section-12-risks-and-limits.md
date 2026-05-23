---
id: "12"
title: "Risks and Limits"
status: needs_cite
target_words: 800
word_count: 879
last_phase: draft
draft_status: needs_cite
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

## 12.A The empirical anchor and its practitioner-side consequence

The article does not claim that the case study is free of the risk that generative systems fabricate. The strongest public evidence that the risk is real and quantified comes from Magesh and colleagues, who report that three leading commercial legal retrieval-augmented-generation systems, Lexis+ AI, Westlaw AI-Assisted Research, and Ask Practical Law AI, hallucinate citations between seventeen and thirty-three percent of the time despite being purpose-built and curated for legal research.[CITE: evidence-12-magesh-hallucination-findings] What transfers is the quantified warning that even well-curated legal systems hallucinate at rates incompatible with responsible practice; what does not transfer is the evaluation method itself, because a reviewed static website has no runtime generation surface on which hallucination can occur. The practitioner-side consequence is documented and sanctionable. In Mata v. Avianca, a federal court imposed Rule 11 sanctions on an attorney who filed a brief containing six fabricated cases that a generative tool produced.[CITE: evidence-12-mata-v-avianca-rule-11-sanctions] The pedagogical reading matters most: a student who internalizes a no-verify habit through an AI tool carries it into practice.

## 12.B The architectural contrast and the discipline that organizes it

The architectural response is the case study’s central design choice, a difference in kind rather than a promise of safety. A chatbot-tutor generates text at runtime against a corpus, and the reader sees that generated text without prior review; the case study publishes a reviewed static website whose every page a professor inspected before it reached a reader.[CITE: evidence-12-static-vs-chatbot-risk-architecture] The contrast holds at four points. Review timing separates build-time professorial inspection from runtime generation with no human in the loop. The error surface separates a stable, citeable page from an ephemeral response re-rolled each session. The update mechanism separates a versioned commit to a repository from opaque retrieval against a corpus. The accountability surface separates a named professor from a system whose outputs no one signed. What transfers is the structural insight that review timing and error surface differ between the architectures; what does not transfer is this case study’s particular risk map, which binds no other static-website implementation.

The contrast does not make the case study risk-free; its own risk surface lives elsewhere. Review at scale caps how fast the system can grow, since every page must pass inspection. A static site cannot address a question the professor did not anticipate, a real loss of the interactivity a conversational system offers. The doctrinal map the structure encodes carries the professor’s commitments, and a student who absorbs it without contest forgoes the live Socratic exchange. An error that survives review and ships to a public page costs more to retract than an ephemeral answer. The verbs stay with their architectures: the chatbot-tutor generates and responds, while the case study publishes, indexes, and structures.

## 12.C Casebook material and the corpus-completeness question

Two of the project’s open decisions route to the corpus. The first is copyrighted casebook material. The forward-looking discipline is settled: the public-facing pages work only from professor-prepared slides and notes, public judicial opinions, public constitutional text, statutes, and original hypotheticals, none of which is casebook text.[CITE: evidence-12-copyrighted-casebook-material-risk] The backward-looking audit, whether any page in the current snapshot reproduces casebook quotation that would need removal before the site is held up as a model, remains pending professorial review, and the article reports it as pending rather than asserting a result. The second decision is what that exclusion means for the curriculum-grounding claim. Because the casebook sits outside the corpus, the curriculum-grounded retrieval the article credits elsewhere applies to the course-issued layer rather than to the full reading load.[CITE: evidence-12-curriculum-grounding-corpus-incompleteness] The architectural implication is that a reviewed static site published from a structured corpus performs no runtime retrieval, so it need not ingest the casebook to do its work; a future replication could license casebook excerpts where its method required them.

## 12.D Privacy and the snapshot commitment

A third decision concerns student work as input. If past exam answers, office-hours notes, or LMS posts were used as training input, the article owes a dedicated privacy treatment; the project’s working understanding, pending the professor’s confirmation, is that no student work was used, and any replication that did use it would need FERPA-compliant handling, IRB review where appropriate, and consent and anonymization protocols.[CITE: evidence-12-student-work-as-input-privacy] The use-side surface is separate: the deployed site’s PostHog analytics respects Do Not Track and disables session recording, the configuration Section VIII discloses. A fourth decision concerns whether the public site is evidence or a continuing experiment. The article commits to a tagged release of the source repository at the manuscript’s snapshot date, an archive.org capture of the deployed pages at that date, citation of the tagged version rather than the live site, and an explicit posture that the site’s continued evolution is expected.[CITE: evidence-12-public-site-continuing-experiment-snapshot]

## 12.E Equity, accessibility, and the field-level frame

The deployed site’s access assumptions are the article’s contribution at the equity altitude, disclosed rather than solved. The single-page application presupposes broadband and a current browser; the hash-route navigation and command-K palette leave screen-reader behavior an open testing question; the modernized PDFs assume a device capable of high-resolution rendering; and the Canvas enrollment gate restricts the input corpus to currently enrolled students.[CITE: evidence-12-equity-accessibility-cross-section-convergence] A replication could add the WCAG conformance testing, alt-text discipline, and screen-reader auditing the case study did not undertake. Bond and colleagues’ meta-review of sixty-six higher-education studies calls the field to greater ethics and rigor, a critique that reaches any AI-in-education system, including a reviewed static one; what does not carry over is the chatbot-tutor and learning-management surface their corpus mostly covers.[CITE: evidence-12-bond-aihed-rigor-frame-risks]
