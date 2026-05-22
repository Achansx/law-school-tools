---
section: "07"
fact_type: example
source_path: "Chandler Constitutional Law Vault/RUNBOOK.md"
verified: true
notes: "The professor-in-the-loop control mechanism is the page-feedback intake. Every scheduled-task run, before the phase dispatcher selects the active phase, Step 0 pulls inbound feedback from the deployed-site page-feedback form via the Netlify MCP, triages each submission into one of six buckets (trivial fix, structural, analytical depth, cross-reference, topic-level/doctrinal gap, verification), logs a `professor-feedback` pending issue carrying the submitter's name and email plus the verbatim comment, routes the issue to the phase that owns the fix (`route: lint | enrich | expand | synthesize | verify`), and deletes the Netlify submission after triage so the queue stays clean. Trivial inline fixes happen on the current run regardless of which phase is dispatched; structural and substantive feedback waits for the phase that owns the fix to rotate around. When a phase's scope-selection step runs, it MUST prefer pages with open `professor-feedback` issues routed to that phase. Resolved feedback gets a short BUILD_NARRATIVE acknowledgement naming the submitter (first name only) so the progress log shows the feedback loop closing. This is the architectural feature that distinguishes the article's loop from an autonomous Karpathy-style loop: the professor remains the gating actor at every phase, the rotation runs continuously but professorial input is the input the rotation prefers, and the system never reaches a state where it generates content without a path for the professor to send it back. Per L-031 the article must not personify the deployed site or the rotation; the page-feedback form is a form, the reader submits a comment, the maintenance phase processes the submission. The form is a real artifact on the deployed site (Section VIII evidence card evidence-08-feedback-form-loopback documents the deployment-side; this card documents the loop-side)."
---

The vault's answer to professorial control is the page-feedback intake. Every scheduled-task run, before the phase dispatcher selects the active phase, Step 0 pulls inbound comments from the deployed site's page-feedback form, triages each submission into one of six routes (trivial fix, structural, analytical, cross-reference, topic-level, verification), and logs a typed `professor-feedback` pending issue routed to the phase that owns the fix. Trivial fixes land on the same run; structural and substantive feedback waits for the phase that owns the fix to rotate around. When a phase's scope-selection step runs, it must prefer pages with open `professor-feedback` issues routed to that phase, so reviewer comments shape what the rotation works on next. The mechanism is the architectural feature that distinguishes the loop from a Karpathy-style autonomous loop: the professor is the gating actor at every phase, and the rotation prefers professorial input over its own next-in-queue work.

Exact source quote, `Chandler Constitutional Law Vault/RUNBOOK.md` lines 222 to 234 (Step 0: Feedback intake):

> Call the Netlify MCP `manage-form-submissions` with `action: "get-submissions"`...
>
> Triage each comment into one of five buckets and act accordingly:
> - **Trivial fix** (typo, wrong date, broken wikilink target, obvious factual slip that can be resolved with a quick source check): fix it inline in THIS run, before dispatching to the phase. Note the fix in BUILD_NARRATIVE and bump the page's `verified` date. Do not queue as a pending issue.
> - **Structural** (schema field missing, enum mismatch, sources out of sync, heading order): log `pending_issues` entry with `type: "professor-feedback"`, `route: "lint"`.
> - **Analytical depth** (asks for more reasoning, missing concurrence, weak hypo, critique gap): log with `route: "enrich"`.
> - **Cross-reference** (wants a link to another case, backlink missing, comparison table request): log with `route: "expand"`.
> - **Topic-level / doctrinal gap** (Chandler wants a new Topic page or meaningful rework of one): log with `route: "synthesize"`.
> - **Verification** (disputed fact, quote accuracy challenge, citation wrong): log with `route: "verify"`.
>
> When a phase's scope-selection step runs, it MUST prefer pages that have open `professor-feedback` `pending_issues` routed to that phase. Sort those pages to the front of the scope list before applying the usual priority rules.
