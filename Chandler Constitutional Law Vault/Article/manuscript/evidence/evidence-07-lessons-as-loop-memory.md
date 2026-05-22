---
section: "07"
fact_type: argument
source_path: "Chandler Constitutional Law Vault/LESSONS.md"
verified: true
notes: "Section VII's framing of LESSONS.md is the loop-memory framing, distinct from Section VI's prompt-engineering framing of the same file (see evidence-06-lessons-as-prompt-iteration-memory). For Section VII the relevant facts are: every run that catches an error or learns something nontrivial appends an entry to LESSONS; entries follow a fixed schema (Rule one sentence, Why one sentence, How to apply one sentence, optional dated Seen footer up to three instances); the file is capped at thirty-five entries and an out-of-rotation Consolidate sweep prunes, merges, and promotes new candidates so the cap stays honest; the file is loaded only by content-editing phases (Ingest, Enrich, Expand, Synthesize), not by Lint or Verify, because the corrections that matter for content generation are different from the corrections that matter for structural checks. The Consolidate sweep is itself a piece of the loop's self-management: when three lesson-candidate items accumulate in pending_issues, or when the file passes 30 entries and 7 days have elapsed, the dispatcher runs Consolidate instead of the rotation phase, which keeps the lessons file from drifting into a 200-entry junk drawer. The article's own writing system replicates the same architecture (Article/LESSONS.md, cap 50, drop-lowest-impact-on-add). Per the article's L-007 (per-phase rubric only) and L-009 (Harvest before Draft, not after) the loop-memory framing is what makes the whole system reviewable: the lessons file is the running record of where the loop was wrong and what changed in response, and the audit trail is the article's strongest answer to a JLE reader who asks whether the loop is actually improving or just running."
---

The vault's LESSONS file is the loop's running memory: every error caught and every pattern noticed compounds into a fixed-schema entry that subsequent runs read at the start of every content-editing pass. The file is capped at thirty-five entries and an out-of-rotation Consolidate sweep merges duplicates, prunes superseded entries, and promotes queued lesson-candidate items so the cap stays honest rather than aspirational. Loading is tiered: Ingest, Enrich, Expand, and Synthesize read the file because they generate content; Lint and Verify skip it because the corrections that govern content generation are different from the corrections that govern structural checks. The lessons file is what answers a reader who asks whether the loop is actually improving or just running.

Exact source quote, `Chandler Constitutional Law Vault/LESSONS.md` lines 5 to 9:

> **Entry cap: 35.** When at or above the cap, do NOT append new lessons. Log the candidate to `pending_issues` with `type: lesson-candidate` and let the next Consolidate sweep merge duplicates and prune superseded entries.
>
> **Entry shape (60 words max).** Rule, one sentence. **Why:** consequence or root cause. **How to apply:** the concrete check, command, or trigger. _Seen:_ italic footer with up to three dated instances; drop the oldest when adding a fourth.
>
> **Loaded only for content-editing phases.** The scheduled task reads this file during Ingest, Enrich, Expand, and Synthesize. Lint and Verify skip it unless a phase-verify persona specifically needs it.
