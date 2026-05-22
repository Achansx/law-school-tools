---
section: "08"
fact_type: example
source_path: "Chandler Constitutional Law Vault/RUNBOOK.md"
verified: true
notes: "The feedback loop from the deployed site back into the maintenance cycle. The site has a Netlify form (page-feedback) that lets the professor (or any reader) submit page-specific comments. Step 0 of every run, regardless of which phase is queued, pulls the form's submissions, triages each into the right phase (Lint for typos, Enrich for content gaps, Synthesize for new topics, Verify for disputed facts), and either fixes inline or logs to pending_issues. Then it deletes the submission to keep the queue at zero. This is the deployed artifact talking back to the vault — the publication is not write-once. Section VIII can name this as the closed-loop framing that distinguishes a reviewed static site from a published PDF: the professor's feedback gets routed back into the same six-phase cycle that built the page in the first place."
---

The deployed site is not write-once. The shell registers a Netlify form, `page-feedback`, and every run begins with Step 0: pull any feedback submissions, triage each into the maintenance phase that can fix it, and clear the queue. Trivial fixes — typos, wrong dates, broken wiki-links — are made inline and acknowledged in the next CHANGELOG line. Substantive submissions become typed `pending_issues` entries with the page ID, page title, submitter name, submitter email, verbatim comment, and the Netlify submission ID; the routing decision sends a content gap to Enrich, a structural break to Lint, a missing doctrinal page to Synthesize, and a disputed fact or quote to Verify. The scope-selection step of whichever phase the dispatcher next runs is required to prefer pages with open `professor-feedback` issues routed to that phase. The published site, in other words, talks back to the vault, and the vault routes the talk-back through the same rotation that produced the page in the first place. Section VIII can name this as the closed-loop framing that distinguishes a reviewed static site from a published PDF or a one-shot LMS export.

Exact source quote, `Chandler Constitutional Law Vault/RUNBOOK.md` lines 220 to 234 (Step 0 feedback intake, every run):

> At the start of every run, before the phase dispatcher picks the active phase, pull and triage inbound feedback from the deployed site. This runs regardless of which phase is queued, feedback enters the backlog on every cycle, and trivial inline fixes happen on every cycle too.
>
> 1. Call the Netlify MCP `manage-form-submissions` with `action: "get-submissions"`, `siteId: "f78a098b-9a9e-412a-8d4f-dd8ccda13bfe"`, `formId: "69e41503a7e59e0008a03bfa"` (the `page-feedback` form). [...]
>
> 4. [...]
>    - **Topic-level / doctrinal gap** (Chandler wants a new Topic page or meaningful rework of one): log with `route: "synthesize"`.
>    - **Verification** (disputed fact, quote accuracy challenge, citation wrong): log with `route: "verify"`.
> 5. Every `pending_issues` entry must carry `metadata.page_id`, `metadata.page_title`, `metadata.submitter_name`, `metadata.submitter_email`, `metadata.comment` (verbatim), and `metadata.netlify_submission_id` so nothing is lost in translation.
> 6. After logging (or fixing inline), delete the submission via the same MCP: `manage-form-submissions` with `action: "delete-submission"` and the submission `id`. Keep the Netlify queue at zero so the next run starts clean.
> 7. When a phase's scope-selection step runs, it MUST prefer pages that have open `professor-feedback` `pending_issues` routed to that phase. Sort those pages to the front of the scope list before applying the usual priority rules.
