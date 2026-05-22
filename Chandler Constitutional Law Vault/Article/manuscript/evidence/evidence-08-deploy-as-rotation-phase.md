---
section: "08"
fact_type: argument
source_path: "Chandler Constitutional Law Vault/RUNBOOK.md"
verified: true
notes: "Deploy is a first-class rotation phase, not a side-effect of a commit. Critical framing for Section VIII: deploy has its own rubric, its own pending issues, and its own cardinal rule (never publish a vault that failed Verify). This is the architectural pivot Section VIII needs to make to set up Section XII: the system treats publication as a phase it can fail, log, and retry — not as an event that happens whenever a human pushes to a branch. The cardinal rule (a stale live site beats a broken one in front of the professor) is the single most quotable sentence for Section VIII's risk discipline."
---

The vault treats Deploy as a first-class rotation phase: it runs in turn after Verify, gets its own per-phase rubric (`rubric/deploy.md`), maintains its own pending-issue lifecycle (`applies_to_phase: deploy`), and refuses to publish a vault that failed the preceding Verify run. This is the architectural pivot Section VIII makes to set up Section XII. Publication is a phase the system can fail, log, and retry on a defined cadence; it is not an event that fires whenever a human pushes to a branch. The cardinal rule — that a stale live site beats a broken one in front of the professor — is the substantive expression of the same risk discipline Section XII later names as the static-site-versus-chatbot architectural advantage.

Exact source quote, `Chandler Constitutional Law Vault/RUNBOOK.md` lines 170 to 184 (Phase: Deploy intro and cardinal rule):

> ## Phase: Deploy
>
> Goal: publish the current vault to https://constitutionallaw.netlify.app so Professor Chandler can read it and leave feedback. Deploy is a first-class rotation phase: it runs after Verify, gets its own scorecard, and owns its own pending issues from open to close. The mechanical procedure (build command, upload, manifest verification, state write) lives in `DEPLOY.md` so it can be edited independently of this rubric-facing description.
>
> [...]
>
> **Pending-issue lifecycle.** Deploy opens issues with `applies_to_phase: deploy` and closes them itself on the next successful Deploy run. The standard issue types (`deploy-build-failed`, `deploy-token-missing`, `deploy-count-mismatch`, `deploy-zombie`, `deploy-state-not-advanced`) are defined in `rubric/deploy.md`. They never wait for Lint or Verify to pick them up.
>
> **Cardinal rule for Deploy.** Never publish a vault that failed Verify (persona-aborted or left an unresolved high-severity finding). A stale live site is recoverable; a broken wiki in front of the professor is not.
