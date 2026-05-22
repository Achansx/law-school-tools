---
section: "06"
fact_type: example
source_path: "Chandler Constitutional Law Vault/RUNBOOK.md"
verified: true
notes: "The Hypothetical Applications prompt is the clearest pedagogy-as-prompt example in the vault. Five hypos in a fixed structural distribution (two same-side, two opposite-side, one fence-sitter), each with a fact pattern AND reasoning, is not a generic LLM-prompt convention; it mirrors the law-school exam pedagogy of testing a rule against varying fact patterns to expose where the rule bends and where it breaks. The RUNBOOK Step 3 procedure and the Enrich rubric hypos_with_reasoning criterion together specify the requirement. Section VI should use this card to make the point that pedagogical knowledge is encoded directly in the prompt's distributional requirements; a hypothetical-set of any other shape would produce different student work. The lesson-candidate failure mode the rubric watches for (fact-pattern-only hypos count as 0 for that slot) is the mechanical enforcement of the reasoning requirement."
---

The Enrich phase prompt for Hypothetical Applications requires five hypos per brief in a fixed structural distribution: two same-side hypos that would come out the same way under the rule, two opposite-side hypos that would come out differently, and one fence-sitter hypo that is genuinely unclear. Each hypo must include both a fact pattern and the reasoning that applies the rule to those facts; a hypo written as fact pattern alone counts as zero for that slot under the Enrich rubric. The distributional commitment is pedagogical, not stylistic. The same-side hypos confirm the rule's core; the opposite-side hypos test where the rule's coverage ends; the fence-sitter forces the student to do the analytical work of identifying which features of the fact pattern push the case in each direction. A prompt that asked for five hypotheticals without specifying the distribution would produce a different pedagogical artifact, most likely five same-side variations.

Exact source quote, `Chandler Constitutional Law Vault/RUNBOOK.md` Phase: Enrich Step 3 (line 100):

>    - **Hypothetical Applications**: five hypos total (2 same-side, 2 opposite-side, 1 fence-sitter). Each hypo needs fact pattern + reasoning, not just the fact pattern.

Exact source quote, `Chandler Constitutional Law Vault/rubric/enrich.md` hypos_with_reasoning criterion (line 11):

> | hypos_with_reasoning | 0.14 | 0 | Five hypos per brief (2 same-side, 2 opposite-side, 1 fence-sitter), each with fact pattern AND reasoning. All five on each enriched brief -> 5. Four on any brief -> 3. Three or fewer -> 1. Fact-pattern-only hypos count as 0 for that slot. |
