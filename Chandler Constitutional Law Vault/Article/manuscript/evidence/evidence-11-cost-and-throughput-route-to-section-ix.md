---
section: "11"
fact_type: argument
source_path: "Chandler Constitutional Law Vault/Article/LESSONS.md"
verified: true
notes: "Operational/routing card. Per L-027, load-bearing claims that depend on numeric line items (cost dollars, audit counts, page-view numbers, hours-by-category figures) whose ownership belongs to a different section per PROJECT_PRIMER or per the workplan must route the numeric to its owning section rather than be invented inside the consuming section. For Section XI this means: any cost or throughput figure that bears on the section's evaluation argument is anchored in Section IX (cost and labor), and Section XI's prose makes the qualitative architectural claim without inventing the numbers. The card exists so the Section XI Outline and Draft ticks have a load-bearing reminder against the recurring failure mode L-027 names. The card is operational rather than substantive; it has no external URL anchor."
---

L-027 (`Article/LESSONS.md` impact-score-4 lesson) names the routing rule: load-bearing claims that depend on numeric line items whose ownership belongs to a different section route the numeric to its owning section rather than be invented inside the consuming section. For Section XI the rule has three operational consequences.

First, any cost-or-time figure that bears on the section's evaluation argument (build hours, token spend, deploy time, hosting cost) is anchored in Section IX, and Section XI's prose makes the qualitative architectural claim without quoting numbers. Section XI may say that the artifact under evaluation was produced at proportional cost and labor; Section XI may not say that it cost X dollars or took Y hours unless Section IX's master cost table has already landed those numbers and Section XI cross-references the table.

Second, any Netlify analytics figure (page views by page type, time on page, search-term frequency) is the evaluation data Section XI itself owns, not a Section IX cost-and-throughput figure. Per L-027 the distinction is that analytics-as-use-pattern-data belongs to the section whose claims rest on it; cost-and-throughput data belongs to Section IX regardless of which section needs them.

Third, any think-aloud-session figure (number of participants, session length, common click paths) is Section XI's own evaluation data and follows the same rule as analytics: Section XI owns it.

Source-record excerpt, `Chandler Constitutional Law Vault/Article/LESSONS.md` L-027 (lines 239 through 246, summarized rule):

> When the Outline phase encounters a load-bearing claim that needs a specific numeric line item (a cost dollar figure, an audit count, a Netlify analytics number, a Bluebook URL-liveness date) whose ownership belongs to a different section per PROJECT_PRIMER or per the workplan's section-by-section commentary, the bullet must (a) name the qualitative architectural property the line item supports without quoting a fabricated number, and (b) route the numeric line item to its owning section by opening a pending_issue with the owner-section field set and an explicit closing condition.

Cross-reference: PI-053 (Route A multi-section pattern that the 2026-05-22 Polish tick on Section IV operationalized for the ingest-phase cost line) is the canonical implementation of the rule for cost figures. Section XI's first reference to the cost-and-labor accounting follows the same Route A pattern: a forward reference to Section IX's master cost table for any cost-or-throughput figure, with the qualitative architectural claim carried in Section XI's own prose. Section XI's Outline tick should bind any cost-or-throughput bullet to a forward-reference pointer rather than to a numeric value; the Cite tick on Section XI resolves the pointer to Section IX's actual note number per L-041 once Section IX's Polish tick has finalized the master cost table.
