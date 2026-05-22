---
section: "06"
fact_type: example
source_path: "Chandler Constitutional Law Vault/rubric/synthesize.md"
verified: true
notes: "The Synthesize phase prompt produces a Topic page in a fixed exam-ready scaffold: Governing Rule blockquote, Doctrinal Development, Key Cases table, Hypothetical Applications, How to Spot on an Exam, Critique, Connections. The Synthesize rubric's exam_readiness criterion enforces that touched Topic pages carry Governing Rule, Hypotheticals, and How to Spot on an Exam sections; missing any drops the score to 2. The synthesize prompt is the pedagogical counterpart to the case-brief prompt: case briefs answer 'what does this opinion hold,' Topic pages answer 'what rule does the doctrine produce and how does a student deploy it.' Section VI should use this card to make the point that the vault's Synthesize prompt is engineered for exam pedagogy specifically, not for generic doctrinal summary. The 'no_synthesis_drift' criterion (Topic pages do not introduce claims absent from underlying case briefs) is the safety rule that keeps the synthesis prompt from inventing doctrine; pedagogy without verification would defeat the article's thesis."
---

The Synthesize phase prompt produces a Topic page in a fixed scaffold designed for exam-preparation work. The Topic Page template specifies a Governing Rule blockquote (the rule stated in exam-ready language), Doctrinal Development (case-by-case progression, foundational case first), a Key Cases pipe table, Hypothetical Applications (the same five-hypo two-same-two-opposite-one-fence distribution Enrich uses for case briefs), a How to Spot on an Exam section (trigger facts and the analytical framework to deploy), Critique, and Connections. The Synthesize rubric's exam_readiness criterion enforces that every touched Topic page carries Governing Rule, Hypotheticals, and How to Spot on an Exam at minimum, weighted at 0.22 of the run score. The Synthesize prompt is the pedagogical mirror of the case-brief prompt: case briefs answer the question "what does this opinion hold," and Topic pages answer the question "what rule does the doctrine produce and how does a student deploy it on an exam." The two prompts together implement the doctrine-first pedagogy that constitutional law instruction depends on, with the rule first and the cases as evidence for the rule.

Exact source quote, `Chandler Constitutional Law Vault/rubric/synthesize.md` exam_readiness criterion (line 8):

> | exam_readiness | 0.22 | 1 | Topic pages touched have Governing Rule, Hypotheticals, and How to Spot on an Exam sections. All -> 5. Any missing -> 2. |

Exact source quote, `Chandler Constitutional Law Vault/RUNBOOK.md` Phase: Synthesize procedure (line 130):

> A topic qualifies when at least two case briefs plus one lecture cover it. Follow `Templates/Topic Page.md` exactly: YAML frontmatter, Governing Rule blockquote, Doctrinal Development (foundational case first, refinements, then limits), Key Cases table, five hypotheticals (2 same-side, 2 opposite-side, 1 fence-sitter), How to Spot on an Exam, Critique, Connections.
