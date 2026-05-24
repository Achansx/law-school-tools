# Con Law Wiki Runbook

Per-phase procedures, frontmatter rules, and update checklists. The scheduled-task prompt links here instead of repeating this material.

---

## Frontmatter (canonical)

Schema and per-field population rules live inline in each `Templates/*.md` file as an HTML comment block directly below the YAML. Copy the template, follow the inline guide, delete the comment block. Populate during Ingest, update during Enrich and Verify, normalize during Lint. `case_name` / `topic_name` / `lecture_title` must equal the H1 and the filename stem.

**Enum realignment policy.** When a page's `area` or other enum-typed field does not fit any existing enum value (example: Judicial Review initially assigned `area: "Federal Judicial Power"`, which is not one of Federalism | Separation of Powers | Individual Rights | Justiciability), REALIGN the page to the nearest canonical value; do NOT widen the enum inline. Widening the enum is a vault-wide change that requires editing the template's inline guide, updating this RUNBOOK if the enum is mentioned here, and a one-paragraph BUILD_NARRATIVE note explaining the reason. Only widen when the realigned value would be misleading to a reader, and even then prefer renaming the page before adding a new enum value.

---

## Phase: Ingest (skeleton pass, gated)

Goal: turn unprocessed source files into **skeleton** wiki pages, AND backfill file-on-disk source attributions onto already-ingested briefs as new Source Materials arrive. Depth is deferred to Enrich.

**Cadence gate.** Ingest runs roughly once per full rotation through the other phases. Before doing anything else, count distinct non-ingest phases since the most recent `ingest` entry by tailing the current month's phase-history JSONL: `tail -n 40 archive/phase-history-$(date -u +%Y-%m).jsonl | jq -r .phase` (read both the current month and prior month's file when the rotation crosses a month boundary). If fewer than 6 non-ingest runs have occurred (one full cycle of Lint, Enrich, Expand, Synthesize, Verify, Deploy), do NOT ingest this run: append a one-line `CHANGELOG.md` entry explaining the skip, set `next_phase` to whichever rotation phase comes next, and end. A time-based fallback (2 hours since the most recent `.ingested-files.jsonl` timestamp) handles cases where the JSONL tail is inconclusive. This keeps Enrich from being starved while still clearing the Source Materials backlog at a reasonable pace. **Burst-mode override:** when `state.force_ingest_remaining > 0`, skip the cadence count entirely, decrement the counter on entry, and proceed to Step 1.

1. Read `.ingested-files.jsonl`. List `Source Materials/` **recursively**, walking every subfolder (`Uploaded Media/`, `resources/`, `unfiled/`, `course_image/`, and any new folders the course publishes into). **Cache-first.** Reuse `/tmp/source_inventory.json` when it exists AND its mtime is newer than the most recent mtime under `Source Materials/` (`find "Source Materials" -type f -newer /tmp/source_inventory.json | head -n 1` returns empty). When the cache is missing or stale, run `python3 .site/scan_sources.py` from the vault root — that script does the recursive `os.walk`, sorts the result, and writes `/tmp/source_inventory.json` with `{scanned_at, root_mtime, files}`. The fallback `find "Source Materials" -type f ! -name '.DS_Store'` still works if the script is unavailable. Either way, store each candidate's vault-relative path including the subfolder (for example `Source Materials/Uploaded Media/01_calder_v_bull.pdf`). Identify unprocessed files by comparing against the `source` field of entries in `processed`, `skipped`, and `failed`. When comparing, match on the full relative path first, then fall back to basename (historical entries logged only the filename).
2. If nothing is unprocessed: skip Steps 3 to 7 and jump directly to Step 8 (backfill). Backfill alone is sufficient work to score this run. Only when both new-file processing AND backfill produce zero touches do you end the run early with a one-line `CHANGELOG.md` entry and `next_phase` set to the next rotation phase.
3. Classify each file by filename and extension:
   - Case reading PDFs (e.g., `Marbury_v__Madison`, `heller-modernized`, `01_calder_v_bull`) create Case Brief pages in `Cases/`.
   - Lecture PPTXs/PDFs (topic-oriented names) create Lecture Summary pages in `Lectures/`.
   - Supplemental (rubrics, quiz answers, teaching guides) go on the skipped list with a reason.
   - `merged-*` packets contain multiple cases. Create one Case Brief per case, or a single Lecture Summary if it reads like a coursebook chapter.
   - **Non-ingestable subfolder content.** `resources/item_*.html` (Canvas LMS page exports), `course_image/*.png`, and other media assets are NOT case or lecture inputs. Add them to the skipped list with reason `"canvas-lms-resource"` or `"course-asset"` on first encounter so they do not re-appear in the candidate pool every run. The numbered PDFs in `Uploaded Media/` (e.g. `01_calder_v_bull.pdf`, `10_griswold_v_connecticut.pdf`) ARE case readings and should be ingested at normal priority. `Uploaded Media/merged-*.pdf` packets follow the merged-packet rule above.
4. Process 8 to 10 files per run in this priority order (the cap is higher because each file is a skeleton, not a finished brief):
   1. Unprocessed PPTXs (they map the syllabus structure).
   2. Modernized PDFs (`-modernized.pdf`) matching cases already mentioned in processed lectures.
   3. Other individual case PDFs.
   4. Merged reading packets.
5. For each case PDF, produce a **skeleton case brief**, not a finished one:
   - Read the PDF (use page ranges for long docs). Call Midpage `analyzeOpinion` with the reporter citation to verify the core holding. Capture `midpage_id`, `midpage_url`, and a single pin-cited quote.
   - Write the page following `Templates/Case Brief.md` with complete frontmatter except `verified`, which stays `"pending-enrich"`. Leave `cited_by` unset (Enrich fetches it from CourtListener).
   - **Populate `source_files` in frontmatter and the `## Sources` footer section.** Both must list every raw Source Materials input that fed the brief. Format each frontmatter entry with the full vault-relative path, preserving the subfolder: `Source Materials/filename.pdf`, `Source Materials/Uploaded Media/01_calder_v_bull.pdf`, `Source Materials/resources/item_14_3.html`, or `Source Materials/Midpage analyzeOpinion (opinionId N)` for Midpage-only sources. In the footer, render each file-on-disk entry as an Obsidian wikilink (`- [[Source Materials/filename.pdf]]`) so the build emits a download link on the deployed site; keep Midpage opinion records as inline code. When multiple inputs contributed (e.g., a case PDF plus a Midpage lookup, or a merged packet), list each entry separately. YAML list and footer must stay in sync; Lint enforces the match.
   - **Drop empty redesign-display keys into frontmatter** so Enrich knows to fill them rather than leaving the deployed site's holding bar showing "— not yet extracted" placeholders. The Case Brief template (`Templates/Case Brief.md`) already lists them in the right order; copy the block verbatim. Required empty keys: `issue: ""`, `holding: ""`, `reasoning: ""`, `doctrine_family: ""`, `argued: ""`, `decided: ""`, `panel: ""`, `author: ""`, `vote: ""`, `disposition: ""`, `relies_on: []`, `distinguishes: []`, `applied_in: []`, `overrules: ""`, `overruled_by: ""`. **Ingest fills only what's directly on the opinion face**: `decided` (always), `argued` (when stated), `author` (majority surname), `vote` (e.g. `6-3`), `disposition` (one of: Affirmed / Reversed / Reversed and remanded / Vacated / S.J. for plaintiffs / etc.), and `doctrine_family` (one of `Federalism | Separation of Powers | Individual Rights | Justiciability` — bucket from the case's primary doctrine). Leave `issue`, `holding`, `reasoning`, `panel`, `relies_on`, `distinguishes`, `applied_in`, `overrules`, `overruled_by` as empty strings or empty lists; Enrich owns those.
   - Fill at full depth ONLY: Memory Jogger, Facts, Procedural History, Judicial Votes, and Holding. These are factual and should not require re-reading during Enrich.
   - Write a majority-only Analysis sketch of roughly 150 words that captures the rule the majority adopted and its chief reasoning. Do not write the concurrence or dissent analysis.
   - Put exactly one Midpage-verified pin-cited quotation in Key Quotations.
   - Stub the remaining sections with single-line `<!-- ENRICH: {one-sentence description of what Enrich should add} -->` markers. Stub at minimum: concurrence reasoning, dissent reasoning, Hypothetical Applications (all five), Critique (both progressive and originalist), additional Key Quotations, and Connections.
   - Name the file `Cases/Case Name v Party (Year).md`.
6. For each lecture PPTX: extract slide text in bash with `pip install python-pptx --break-system-packages -q` then a python-pptx loop. Write a Lecture Summary page following `Templates/Lecture Summary.md`. Expand bullets into prose. Link cases mentioned even if the target page does not exist yet. Populate `cases_discussed` AND `cases_covered` from the slide content (the latter is the canonical name the redesign reads; keep both in sync on new pages). Populate `source_files` frontmatter AND the `## Sources` footer with the full vault-relative path (`Source Materials/<deck filename>` for root decks, `Source Materials/Uploaded Media/<deck filename>` for subfolder decks); render each footer entry as an Obsidian wikilink (`- [[Source Materials/<deck filename>]]`) so the deployed site turns it into a download link; keep the two in sync. **Populate the redesign timeline keys when extractable from the deck or filename**: `theme` (mirror `topic_area`), `week` (integer 1–14, often parsed from a leading number on the deck filename like `12_executive_emergencies.pptx` or from the deck's first slide), `date` (ISO date if the deck cover gives one), and the boolean `is_current` / `is_upcoming` flags. Leave the booleans `false` when uncertain — Verify will flip `is_current` onto the most-recent past lecture during its sweep. Set `verified: "pending-enrich"` unless the summary is already complete on the first pass (lectures are often one-shot because the slide content itself is the source of truth).
7. Append a line per processed file to `.ingested-files.jsonl`:
   `{"source": "filename.pdf", "created": ["Cases/Case Name v Party (Year).md"], "timestamp": "ISO-8601", "type": "case_reading"}`
8. **Backfill source attributions across already-ingested briefs.** Every Ingest run, after Steps 1 to 7 finish processing new files, also runs the source-matcher across the entire `Cases/` directory so that previously-ingested briefs pick up file-on-disk attributions as new Source Materials arrive in subsequent weeks. This step is what keeps the source attribution self-healing instead of frozen at whatever the matcher could see on the day a brief was first written. Procedure:
   1. Run `python3 .site/match_sources.py` from the vault root **only when the matcher output is stale**: reuse `/tmp/case_source_matches.json` if it exists AND its mtime is newer than the most recent mtime under `Source Materials/` (bash: `find "Source Materials" -type f -newer /tmp/case_source_matches.json | head -n 1` — empty output means cache is valid). Reusing a valid cache is the common steady-state path and the matcher only actually runs when the source inventory or case roster changed. When the matcher does run, it writes `/tmp/case_source_matches.json` (case-by-case `auto_apply` and `review_needed` buckets, scored against every file under `Source Materials/` recursively) and a human-readable mirror at `/tmp/case_source_matches.md`.
   2. **Apply the auto bucket.** For each case in the `auto_apply` bucket (score >= 3), compare the candidate paths against the case's current `source_files`. For any candidate path missing from `source_files`, append it to the YAML list AND add a matching wikilink bullet (`- [[Source Materials/<name>]]`) to the `## Sources` footer. The YAML list and the footer must stay in lockstep one-for-one; Lint check 11 enforces this.
   3. **Evict Midpage placeholders that have been superseded.** When a case gains its first file-on-disk source via this backfill, REMOVE every `Source Materials/Midpage analyzeOpinion (opinionId N)` entry from `source_files` and from the `## Sources` footer. The Midpage placeholder was a stand-in until a real file appeared. Preserve `midpage_id` and `midpage_url` in frontmatter — those stay as verification metadata pointing at the Midpage opinion record. Only the Source Materials reference moves.
   4. **Log the review bucket.** For each case in the `review_needed` bucket (score 2) whose `source_files` currently contains only Midpage placeholders, log a `source-attribution-review-needed` pending issue carrying the candidate paths and their reasons (the matcher records why each candidate landed at score 2). Do NOT auto-apply these. A reviewer either promotes one or more candidates to `source_files` by hand or marks the issue resolved.
   5. **Log the empty bucket.** For each case with NO matches at either tier, leave `source_files` alone AND open a one-time `missing-file-on-disk-source` pending issue if one is not already open for that case. This represents a genuine gap in the Source Materials inventory (the case has no PDF or PPTX in the folder), not a matcher failure.
   6. **Backfill scope cap.** Backfill honors the per-run 8-to-10 file cap as a "cases touched" budget, not a candidate-files budget. Count each case whose `source_files` was modified by Step 8.2 as one touch. If Steps 1 to 7 already consumed the cap, skip backfill this run entirely. If new file ingest produced fewer than 5 touches, spend the remainder on backfill, prioritizing cases that currently have zero file-on-disk sources over cases that already have at least one. **Backfill-only ceiling.** When Steps 1 to 7 produced **zero** touches (no new files at all), the backfill ceiling rises to 15 for that run. Backfill is mechanical (no analytical depth), so the ordinary scope-discipline argument that protects Enrich from over-eager Ingest does not apply. The higher ceiling is what drains the first-run backlog at a reasonable pace without forcing a burst-mode flag. Pending-issue logging in 8.4 and 8.5 does NOT consume cap.
   7. **First-run backlog expectation.** The first run of Step 8 after this policy was introduced will encounter a large backlog (most pre-existing briefs were attributed only to Midpage). Working through the backlog one cap-sized batch per Ingest run is intentional; do not raise the cap to clear it faster. Subsequent runs only have work to do when the source inventory actually changed, so backfill cost falls toward zero in steady state.
9. Append a line to `.ingested-files.jsonl` summarizing the backfill pass:
   `{"source": "_backfill", "cases_touched": [...], "auto_applied": N, "review_logged": M, "missing_logged": K, "timestamp": "ISO-8601", "type": "backfill"}`

**Source attribution convention.** Every wiki page carries a provenance trail:
- **Cases and Lectures:** `source_files` in frontmatter and a `## Sources` footer section both list the raw Source Materials entries that fed the page. One-to-one with `.ingested-files.jsonl`.
- **Topics:** `source_files` in frontmatter and `## Sources` footer list the **direct-input** Case and Lecture wiki pages that were actually consulted to draft the Topic, not every case wiki-linked in passing. Paths are vault-relative and end in `.md`. Topics are attributed to the upstream wiki pages rather than raw Source Materials because they are synthesized from briefs, not drafted directly from PDFs. Synthesize populates these during Topic creation; Enrich and Expand extend them when they cite a new upstream page.

**Footer bullet form (Cases and Lectures).** Each entry in the `## Sources` footer is rendered as an Obsidian wikilink when it points at a real file on disk: `- [[Source Materials/<name>]]`. The build script copies `Source Materials/` into `dist/source/` and rewrites that wikilink into `<a class="source-download" href="source/<url-encoded-name>" download>` so visitors can download the raw PDF or slide deck directly from the deployed page. Midpage opinion records stay as inline code (`` `Source Materials/Midpage analyzeOpinion (opinionId N)` ``) because they reference an external opinion ID, not a file on disk. If an Ingest or Enrich run adds a new `source_files` entry, mirror it into the footer using this wikilink-vs-inline-code split.

---

## Phase: Lint

Goal: structural integrity across `Cases/`, `Topics/`, `Lectures/`. Do not add substantive content.

Check every touched file for: (1) valid YAML frontmatter delimited by `---`, (2) required schema fields present, (3) consistent `doctrines` and `concepts` naming across the vault (e.g., not "Commerce Clause" in one file and "Interstate Commerce" in another), (4) `verified` date present, (5) one H1 matching filename, (6) H2 order matching the template, (7) wiki-link targets exist (glob before asserting), (8) pipe tables have the `|---|---|` separator row, (9) `---` section separators have blank lines above and below, (10) tags lowercase-hyphenated at the end, (11) `source_files` frontmatter list is present and its entries match the `## Sources` footer one-for-one (same paths, same order); flag any mismatch for repair, (12) on Cases and Lectures, `## Sources` footer bullets for real files use the wikilink form `- [[Source Materials/<name>]]` and only Midpage opinion records use inline code; an entry in inline code whose path resolves to an actual file under `Source Materials/` is a lint failure (the file is downloadable; the bullet must be a wikilink so the deploy renders it as a download link), (13) on Cases, a `Source Materials/Midpage analyzeOpinion (opinionId N)` placeholder in `source_files` is **stale** if `/tmp/case_source_matches.json` (consumed passively — Lint NEVER runs the matcher) shows that case has any `auto_apply` candidate; stale placeholders should be logged as a `pending-issue: stale-midpage-placeholder` for the next Ingest backfill rather than rewritten by Lint (Lint never invents new file attributions; that is Ingest's job under Step 8). A case that has no `auto_apply` candidate is allowed to keep its Midpage placeholder. **If `/tmp/case_source_matches.json` is missing or older than the most recent Source Materials mtime**, log a single `matcher-output-stale` pending issue routed to the next Ingest run and SKIP check 13 for this tick. This keeps Lint cheap (no heavy walks) and centralizes matcher invocation in Ingest where it belongs.

Fix structural issues in place. Log content gaps to `pending_issues` for Enrich.

**Read `.site/dist/build_errors.json` at Lint entry.** The build script writes this file every Deploy (and any local build) listing pages whose YAML frontmatter failed to parse. Each entry carries `path`, `reason`, and `yaml_excerpt`. For every entry not already represented in `pending_issues`, open a `frontmatter-parse-failed` pending issue routed back to Lint (this run handles its own backlog) carrying `metadata.path`, `metadata.reason`, `metadata.yaml_excerpt`, and `metadata.first_seen` (today's ISO date). Then attempt the in-place fix: re-read the offending page, locate the malformed YAML by the excerpt, and repair it (most common: an unquoted colon inside a string, an unbalanced bracket, or a date written as bare text instead of `YYYY-MM-DD`). When the fix is applied, close the pending issue inline. When the failure is non-trivial (e.g. the YAML is genuinely truncated), leave the issue open and surface it in the run's BUILD_NARRATIVE so it is visible at human-review time. Lint NEVER deletes a page whose frontmatter failed to parse; the body content is still legitimate vault material even when the frontmatter is broken.

---

## Phase: Enrich (analytical depth)


### Scope-selection override (V3 addition)

Before applying the plugin reference's scope-selection rules, **check `ENRICH_QUEUE.md` at the vault root**. If present, the first 3-5 entries in that queue are the run's scope (in list order). The queue is pre-sorted by stub count desc, cited_by desc, year desc.

Regenerate the queue file when its length drops below 5 or when Ingest produces new pending-enrich skeletons. The regeneration query: `verified` starts with `pending` OR empty AND all lineage fields empty; sort by ENRICH-stub count desc, cited_by desc, year desc.

If `ENRICH_QUEUE.md` is missing, fall back to the plugin reference's default scope selection (most stub markers first).


Goal: fill the `<!-- ENRICH: -->` stubs that Ingest left behind, bringing skeleton briefs up to the full 9-section case-briefer standard. This is where substantive legal analysis, not just structural scaffolding, lands.

**Scope selection.** Prioritize briefs with `verified: "pending-enrich"`. Process 3 to 5 briefs per run. Within that set, prefer the ones with the most stub markers and the ones whose doctrines appear in other Ingest-produced skeletons (Expand benefits downstream).

For each brief in scope:

1. Re-read the Source Materials PDF (use page ranges for long opinions). Ingest touched the face of the opinion; Enrich is where you read the concurrences and dissents carefully.
2. Call Midpage `analyzeOpinion` with a targeted question if a stub calls for reasoning that was not in the first pass (e.g., "summarize Justice X's concurrence on point Y"). Use `findInOpinion` for quote pin-cite confirmation; fall back to `analyzeOpinion` with a targeted question if `findInOpinion` returns nothing.
3. Replace each `<!-- ENRICH: -->` marker with substantive prose:
   - **Analysis (concurrence + dissent)**: reasoning, not just votes. Identify the point of divergence from the majority and the interpretive move each opinion makes.
   - **Hypothetical Applications**: five hypos total (2 same-side, 2 opposite-side, 1 fence-sitter). Each hypo needs fact pattern + reasoning, not just the fact pattern.
   - **Critique**: at least one progressive angle and one originalist/textualist angle, each grounded in a published critique or a clearly signposted independent argument. Identify logical weaknesses, competing values, and open questions.
   - **Key Quotations**: add 2 to 3 more Midpage-verified quotations with pin-cite URLs beyond the one Ingest placed. Pick quotes that do analytical work the bare holding does not.
   - **Connections**: wire the brief to related Topics and Cases with one-sentence annotations that explain the direction of the reference (does this case extend, limit, or clarify the connected doctrine?).
   - **Holding-bar frontmatter (redesign-driven)**: replace the Ingest-placed empty strings with the structured short-form fields the deployed site renders above the prose:
     - `issue`: the question presented, ending in `?`. One sentence preferred. Distinct from any longer "## Issue" section that develops alternative framings.
     - `holding`: the Court's answer in 1–2 sentences, distinct from the longer `## Holding` section. The dashboard's "Case of the Day" and the case page's holding bar both render this verbatim — keep it self-contained and readable on its own.
     - `reasoning`: ≤3-sentence synthesis of the majority's reasoning. List the moves (textual / structural / clear-statement / etc.) without re-narrating the analysis section.
     - `doctrine_family`: confirm Ingest's bucket (`Federalism | Separation of Powers | Individual Rights | Justiciability`) is correct for the lead doctrine; correct it if the case is more fairly classified elsewhere.
   - **Citation-meta frontmatter**: any of `argued` / `decided` / `panel` / `author` / `vote` / `disposition` that Ingest left blank, fill from the opinion face during this re-read. `panel` is especially worth the effort on non-SCOTUS opinions where the panel composition matters.
   - **Authority-lineage frontmatter**: populate `relies_on`, `distinguishes`, and `applied_in` from the opinion + CourtListener `find_cited_cases` / `find_citing_cases` (you are already calling these for `cited_by`, so the marginal cost is parsing). Each entry is `"{Case Name} ({Year})"` matching the corresponding `Cases/` filename when one exists. Set `overrules` and `overruled_by` to the single most-relevant case when the opinion expressly does so; leave empty otherwise. The case page's "Connections" panel renders these as cross-linked columns; without them it falls back to backlinks and loses its directionality.
4. Call CourtListener `find_citing_cases` on the Midpage opinion ID to populate `cited_by`. If the count looks implausibly low for a canonical case, log a `low_cited_by` pending issue rather than writing a suspect number.
5. Only after every stub for a brief is resolved, flip `verified` from `"pending-enrich"` to today's date. If any stub remains unresolved because the vault plus Midpage plus web search could not close the gap, leave `verified: "pending-enrich"` in place and log the gap to `pending_issues`.

Cardinal rules for Enrich: never invent details; every filled stub traces to a PDF, a Midpage result, or a web-search citation; Key Quotations are Midpage-verified text with pin-cite URLs or they do not go in. If Enrich finds a brief with zero stub markers and `verified: "pending-enrich"`, something went wrong upstream: treat it as an Ingest regression and log a pending issue instead of hand-waving `verified` forward.

---

## Phase: Expand

Goal: cross-references between Cases, Topics, and Lectures. No new substantive content.

For each in-scope page: list outgoing wiki-links, confirm reciprocity at each target, add the missing backlinks with short annotations that explain the direction of the reference. Use CourtListener `find_cited_cases` and `find_citing_cases` on Midpage opinion IDs (for historical SCOTUS cases the IDs are the same on both systems; do not assume for lower courts or recent opinions) to discover doctrinal connections the vault is missing. Build comparison tables between related cases or doctrines where useful. Enrich-created pages generate a second wave of asymmetric links; Expand must audit those in particular.

---

## Phase: Synthesize

Goal: create or substantively update Topic pages that synthesize across multiple case briefs.

A topic qualifies when at least two case briefs plus one lecture cover it. Follow `Templates/Topic Page.md` exactly: YAML frontmatter, Governing Rule blockquote, Doctrinal Development (foundational case first, refinements, then limits), Key Cases table, five hypotheticals (2 same-side, 2 opposite-side, 1 fence-sitter), How to Spot on an Exam, Critique, Connections. Every claim must trace to a case brief or lecture in the vault. Use CourtListener `search_case_law` to confirm the topic is doctrinally complete before declaring the page done.

**Set `family` explicitly on every new Topic.** The deployed site groups Topics into a four-family grid (Federalism / Separation of Powers / Individual Rights / Justiciability) and uses each family's color for the column's top border. `family` is almost always equal to `area`; setting it explicitly avoids leaving the bucket selection to build.py's keyword fallback. When a Topic genuinely spans two families (e.g. a topic that sits across Justiciability and Separation of Powers), pick the one most central to the doctrine — never list both. **Optionally set `two_part_test` and `open_questions`** when the doctrine actually has a multi-prong test or genuinely open questions; the redesigned site renders them in the spotlight sidebar when this Topic gets featured.

**Populate `source_files` and `## Sources`.** Topic attribution is direct-input only: list every Case or Lecture wiki page that was actually consulted while drafting the Topic, not every page wiki-linked in passing prose. Frontmatter format is a YAML list of vault-relative paths ending in `.md` (e.g., `Cases/McCulloch v Maryland (1819).md`). Footer format is `- [[Cases/Name|Name]]` / `- [[Lectures/Name|Name]]` wiki-links. YAML list and footer must stay in sync; Lint enforces the match. If Expand later adds a new upstream citation that was consulted, append it to both.

---

## Phase: Verify

Goal: adversarial three-persona pass. Each persona MUST return at least one finding; if none, it returns `persona-produced-nothing` as its finding.

**Precondition.** Before running any persona, confirm `PERSONAS.md` exists at the vault root via a quick file check (`Read` it, or bash `test -f`). If it is missing, abort the phase: log a `personas-missing` pending issue, append a one-line CHANGELOG entry noting the abort, and advance `next_phase` to the phase after Verify. Do NOT attempt to run Verify from memory or by reconstructing the personas, the file defines the protocol.

The three personas, their charters, sample sizes, and return formats live in `PERSONAS.md` in the vault root. Load that file for the full protocol. After the three pass, every finding becomes a pending issue (or an inline fix if trivial). Update `verified` dates for any spot-checked files.

**Verify diversity (Levers 1 + 2).** PERSONAS.md defines two rotation tables driven by `state.verify_run_count` (zero-indexed counter, missing means treat as 0). At Verify entry:
1. Read `state.verify_run_count`. Default to 0 if missing.
2. Pick the lead, second, and third persona from the rotation table at `verify_run_count % 3`.
3. For each persona, pick the focus area from its own four-row focus table at `verify_run_count % 4`. Each persona's return block MUST name its lead position and its focus area for this run.
4. Run the personas in lead-then-second-then-third order. Findings are listed in that order in the run summary.
5. Increment `state.verify_run_count` by 1 ONLY after all three personas have produced return blocks. A misrouted Verify, a `personas-missing` abort, or any early exit leaves the counter unchanged so the next attempt re-uses the same lead-and-focus selection.
6. BUILD_NARRATIVE for the run names the lead persona and each persona's focus area, so a reviewer can audit rotation health without re-deriving from the counter.

**Quote-correction discipline.** When a persona flags a Key Quotation that differs from the Midpage-verified text, fix the canonical source (usually the case brief) AND grep the vault for the distinctive phrase to catch every other copy (Topic pages, other lectures, comparison tables). Confirm zero stale copies remain before closing the finding. See LESSONS.md "Key Quotations drift across files" for the pattern that makes this necessary.

**Lecture timeline-flag rotation (cheap inline sweep).** Verify already walks the lecture set when one of the personas hits Lectures. Once per Verify run, regardless of which persona drew Lectures as its sample, walk every page in `Lectures/` and reconcile `is_current` / `is_upcoming` against the calendar:
- The single Lecture whose `date` is the most-recent `<= today` becomes `is_current: true`. All others get `is_current: false`.
- Every Lecture whose `date` is `> today` gets `is_upcoming: true`. All others get `is_upcoming: false`.
- Lectures with no `date` set are left untouched (no flags flipped); flag the missing-date as a `lecture-date-missing` pending issue routed to the next Enrich run.
This sweep is bounded (a single linear pass over `Lectures/`, no Midpage / web calls) and stays inside scope discipline because it only reconciles existing structured fields against the clock — it does not author content. Verify the dashboard's "This week in lecture" surface flips to the new current lecture after this pass.

**Pending-issue aging sweep.** After the three personas return, before scoring, walk every entry in `state.pending_issues` and compute its age from the issue's `opened_at` (or the current run's timestamp if `opened_at` is missing — backfill it on this pass). Apply two rules in order:
- **Auto-close at 14 days stale.** Any issue older than 14 days whose `type` is in the auto-closeable set (`source-attribution-review-needed`, `low_cited_by`, `lesson-candidate`, `consolidation-review`, `persona-produced-nothing`, plus any issue carrying `metadata.auto_close_eligible: true`) and that has had no `last_touched` activity in 7 days is removed from `state.pending_issues` with a one-line CHANGELOG note `pending-aged-out: <type> <id> <opened_at>`. Do NOT auto-close `professor-feedback`, `deploy-misrouted`, `deploy-state-not-advanced`, `deploy-zombie`, `deploy-blocked-by-verify`, `cap-violation`, `personas-missing`, `missing-file-on-disk-source`, or anything tagged `metadata.do_not_auto_close: true` — these stay open until manually resolved no matter the age.
- **Escalate at 30 days aged.** Any issue still open at 30+ days regardless of type is moved (not copied) into a new file `triage.md` at the vault root under a heading `## Aged pending issues — <YYYY-MM-DD>`, then deleted from `state.pending_issues`. The `triage.md` file becomes a quick-glance human todo: each escalation includes the original issue JSON plus a one-line "why this aged" note (e.g. "no `pending_issues_count` decrement in 12 ticks"). If `triage.md` exists at run start, do not overwrite it; append a new dated heading.

The aging sweep is part of Verify, not Consolidate, because Verify is the only phase that already touches every pending issue (each persona finding becomes one) and so it is the cheapest place to enforce hygiene. Log the count of auto-closed and escalated issues in the run's BUILD_NARRATIVE paragraph.

---

## Phase: Deploy

Goal: publish the current vault to https://constitutionallaw.netlify.app so Professor Chandler can read it and leave feedback. Deploy is a first-class rotation phase: it runs after Verify, gets its own scorecard, and owns its own pending issues from open to close. The mechanical procedure (build command, upload, manifest verification, state write) lives in `DEPLOY.md` so it can be edited independently of this rubric-facing description.

**Entry guard.** Deploy is the correct active phase whenever `next_phase` in `.vault-maintenance-state.json` reads `deploy` (the normal case after a Verify run sets it). For belt-and-suspenders, also deploy when `last_deploy` is missing OR when every one of `lint`, `enrich`, `expand`, `synthesize`, `verify` has a `phase_timestamps[<phase>]` entry in state strictly newer than `last_deploy` (cross-check against the current-month JSONL tail if a timestamp is missing). If neither condition holds, the dispatcher should not have routed here; log a `deploy-misrouted` pending issue, hand off to the next rotation phase, and end.

**Procedure.** Follow `DEPLOY.md` end-to-end. The two short forms it documents are: (a) Netlify MCP path via `netlify-deploy-services-updater` returning an `npx @netlify/mcp` command embedded with a short-lived proxy token (run from `$VAULT_DIR/.site/dist`), or (b) the `.site/deploy.sh` fallback when the MCP is unavailable AND the PAT at `$VAULT_DIR/.site/.netlify-token` is present. Either path must end with the manifest-counts cross-check against the local `dist/manifest.json`, and `last_deploy` advances only after that check passes.

**Retry semantics.** A failed Deploy is a failed phase, not a skipped check. On failure, leave `next_phase: deploy` in the state file so the next cycle retries before any content phase fires. Do NOT advance the rotation past a broken publish — a stale live site that re-tries cleanly next cycle is better than a content cycle that pretends the publish step succeeded. If three consecutive Deploy runs fail with the same root cause, escalate via a `deploy-recurring-failure` lesson candidate (see `rubric/deploy.md` "Pending-issue lifecycle").

**Scoring.** Score against `rubric/deploy.md` (5 criteria: `content_hash_incremental_hit_rate`, `wall_clock_within_cap`, `manifest_verification_matches_dist`, `last_deploy_timestamp_advanced`, `zero_zombie_deploys`) and append to `.run-scores.jsonl` like any other phase. On a healthy rotation Deploy is steady-state — 5.0 nearly every run is normal. A sustained drop usually means Netlify product change, build-script regression, or PAT/credential drift; investigate before normalizing the rubric.

**Pending-issue lifecycle.** Deploy opens issues with `applies_to_phase: deploy` and closes them itself on the next successful Deploy run. The standard issue types (`deploy-build-failed`, `deploy-token-missing`, `deploy-count-mismatch`, `deploy-zombie`, `deploy-state-not-advanced`) are defined in `rubric/deploy.md`. They never wait for Lint or Verify to pick them up.

**Cardinal rule for Deploy.** Never publish a vault that failed Verify (persona-aborted or left an unresolved high-severity finding). A stale live site is recoverable; a broken wiki in front of the professor is not.

---

## Step 0: Resumability marker check (every run, before feedback intake)

Before anything else (even before feedback intake), check for a stale `.phase-in-progress` marker file at the vault root. The marker is a one-line JSON file written by every phase at entry and removed by every phase at clean exit. A leftover marker means the previous run died mid-phase (timeout, harness crash, network drop, or any other ungraceful exit) and left state inconsistent.

1. `test -f "$VAULT_DIR/.phase-in-progress"`. If absent, proceed to Step 0 feedback intake. This is the common case.
2. If present, read the file. It contains `{"phase": "<name>", "started_at": "ISO-8601", "pid": "<task-run-id-or-na>"}`. Compute the marker's age: `(now - started_at)` in minutes.
3. **Fresh marker (age < 30 minutes).** Another run may legitimately still be in flight from an overlapping schedule trigger. Do NOT race it: append a one-line `CHANGELOG.md` entry `runbook-skipped: prior <phase> still in flight at <started_at>` and end the run cleanly. Do not advance `next_phase`.
4. **Stale marker (age >= 30 minutes).** The prior run died without cleanup. Log a `phase-died-mid-run` pending issue carrying `metadata.dead_phase`, `metadata.dead_started_at`, and `metadata.recovered_at` (the current run's start). Set `next_phase` to the dead phase so this run retries it from scratch (every content phase is idempotent at the file-edit level: re-running Lint after a partial Lint just re-checks the same files; re-running Verify after a partial Verify re-runs the personas). Remove the marker file. Then proceed to Step 0 feedback intake. Do NOT silently swallow the death; the pending issue is what surfaces it for human review.
5. The marker write/remove pattern lives in every phase's procedure (Lint, Enrich, Expand, Synthesize, Verify, Deploy, Ingest). Each phase writes the marker as its first state-touching action and removes it as its last state-touching action. Consolidate is exempt because it is out-of-rotation and its work is fully captured by the LESSONS.md backup.

The 30-minute threshold matches the cron interval (`*/30`); a marker older than the interval cannot be a live concurrent run, only a corpse. Adjust if the cron cadence ever changes.

**Marker write convention (every phase, first state-touching action):**

```bash
PHASE="lint"  # or enrich, expand, synthesize, verify, deploy, ingest
NOW=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "{\"phase\":\"${PHASE}\",\"started_at\":\"${NOW}\",\"pid\":\"${TASK_RUN_ID:-na}\"}" > "${VAULT_DIR}/.phase-in-progress"
```

**Marker remove convention (every phase, last state-touching action, AFTER the JSONL append and the state-file update succeed):**

```bash
rm -f "${VAULT_DIR}/.phase-in-progress"
```

If a phase exits early on a soft skip (cadence-gate skip, deploy-misrouted, ingest backlog empty), still remove the marker; the run is over even if no real work happened. The marker only persists when the process itself died ungracefully.

---

## Step 0: Feedback intake (every run)

At the start of every run, before the phase dispatcher picks the active phase, pull and triage inbound feedback from the deployed site. This runs regardless of which phase is queued, feedback enters the backlog on every cycle, and trivial inline fixes happen on every cycle too.

1. Call the Netlify MCP `manage-form-submissions` with `action: "get-submissions"`, `siteId: "f78a098b-9a9e-412a-8d4f-dd8ccda13bfe"`, `formId: "69e41503a7e59e0008a03bfa"` (the `page-feedback` form). Also acceptable: pass `siteId` without `formId` and filter client-side for `form_name == "page-feedback"`.
2. If the response is empty, append `"feedback: 0 new"` to today's CHANGELOG line and continue to the phase dispatch. Done.
3. For each submission, read `data.comment`, `data["page-id"]`, `data["page-title"]`, `data.name`, `data.email`, and the submission `id`. Locate the target vault page by matching `page-id` against the slug in `.site/dist/pages.json` (or by title fallback if the slug has drifted). If the page cannot be located, still log the feedback but tag it `orphan-target` so it surfaces for manual review.
4. Triage each comment into one of five buckets and act accordingly:
   - **Trivial fix** (typo, wrong date, broken wikilink target, obvious factual slip that can be resolved with a quick source check): fix it inline in THIS run, before dispatching to the phase. Note the fix in BUILD_NARRATIVE and bump the page's `verified` date. Do not queue as a pending issue.
   - **Structural** (schema field missing, enum mismatch, sources out of sync, heading order): log `pending_issues` entry with `type: "professor-feedback"`, `route: "lint"`.
   - **Analytical depth** (asks for more reasoning, missing concurrence, weak hypo, critique gap): log with `route: "enrich"`.
   - **Cross-reference** (wants a link to another case, backlink missing, comparison table request): log with `route: "expand"`.
   - **Topic-level / doctrinal gap** (Chandler wants a new Topic page or meaningful rework of one): log with `route: "synthesize"`.
   - **Verification** (disputed fact, quote accuracy challenge, citation wrong): log with `route: "verify"`.
5. Every `pending_issues` entry must carry `metadata.page_id`, `metadata.page_title`, `metadata.submitter_name`, `metadata.submitter_email`, `metadata.comment` (verbatim), and `metadata.netlify_submission_id` so nothing is lost in translation.
6. After logging (or fixing inline), delete the submission via the same MCP: `manage-form-submissions` with `action: "delete-submission"` and the submission `id`. Keep the Netlify queue at zero so the next run starts clean.
7. When a phase's scope-selection step runs, it MUST prefer pages that have open `professor-feedback` `pending_issues` routed to that phase. Sort those pages to the front of the scope list before applying the usual priority rules.
8. Resolved `professor-feedback` issues get a short acknowledgement line in BUILD_NARRATIVE naming the submitter (first name only) so the progress log shows the feedback loop is closing.

Do this even on Ingest runs and on Deploy runs. Feedback flows into the backlog regardless of which phase is active, and trivial inline fixes happen regardless of phase.

---

## Phase: Consolidate (out-of-rotation)

Goal: keep `LESSONS.md` below the 35-entry cap by merging duplicates, removing entries superseded by newer lessons, and promoting queued `lesson-candidate` items from `pending_issues`. Does not advance `next_phase` — the rotation resumes on the next cycle.

**Trigger.** In Step 0 of the scheduled-task prompt, check (in order): (a) `pending_issues` contains 3 or more items with `type: lesson-candidate`, (b) `last_consolidation` is missing or more than 21 days old (safety valve), (c) `last_consolidation` is more than 7 days old AND LESSONS.md has 30+ entries. Count entries with bash `sed -n '/^## /,$p' LESSONS.md | grep -c '^\*\*'` which excludes the three bolded header notes. If any hit, run Consolidate instead of the rotation phase.

**Procedure.**

1. Back up the current file to `archive/LESSONS_YYYY-MM-DD.md` via bash `cp` (single Read of LESSONS.md is acceptable — this phase edits it structurally).
2. Read `.vault-maintenance-state.json` and collect every `pending_issues` entry with `type: lesson-candidate`. Also read LESSONS.md.
3. For each candidate:
   - Normalize the lead phrase (lowercase, strip punctuation).
   - Compare against every existing lesson's lead phrase. If the core claim already exists, MERGE: append the candidate's concrete example or citation into the existing entry's body. Do not create a new entry.
   - If genuinely new: classify into an existing H2 section. Only create a new H2 if no existing section fits, and prefer widening an existing section's scope over proliferating headings.
4. Scan existing entries for prune targets:
   - **Supersession.** A newer entry fully subsumes an older one's guidance (e.g., two entries on asymmetric wiki-links where the newer one covers every case the older one does).
   - **Staleness.** References to files or paths that no longer exist. Glob-check every file path or vault-relative link mentioned.
   - **One-offs.** Entries that describe a single-incident gotcha with no reusable pattern (rare — default to keeping).
5. **Pruning cap.** Do not remove more than 5 entries in a single sweep. If more than 5 look removable, keep the 5 clearest and log the rest as `pending_issues` entries of `type: consolidation-review` for human review.
6. If the post-merge count still exceeds 35, log a `cap-violation` pending issue describing which entries resisted consolidation. Do not arbitrarily delete to force compliance.
7. Write the consolidated `LESSONS.md` (this is the one Content phase where Write is preferred over Edit — the file is being restructured). Preserve the cap header and the "loaded only for content-editing phases" note.
8. Remove every processed `lesson-candidate` from `pending_issues` in the state file. Set `last_consolidation` to today's date in the state file root.
9. Append a one-paragraph summary to `BUILD_NARRATIVE_YYYY-MM.md` via bash `>>` listing: candidates processed, entries merged, entries pruned, archive file path, new total count.
10. Score against `rubric/consolidate.md` and append to `.run-scores.jsonl`.

**Cardinal rule.** Never delete a lesson without either a newer entry that supersedes it or an archived copy in `archive/`. Pruning is one-way but archival is cheap.

---

## Scope cap (all phases)

Process no more than 10 to 15 files per run.

---

## Legal research tools

- **Midpage `analyzeOpinion`** — verified holdings and pin-cite quotations. Required for Ingest case briefs and all Verify spot-checks. Also the correct escalation when `findInOpinion` returns nothing.
- **Midpage `findInOpinion`** — keyword search within one opinion. Fails on pre-1900 opinions with OCR artifacts.
- **Midpage `search`** — find cases by topic.
- **CourtListener `find_cited_cases` / `find_citing_cases`** — citation chains for Expand and Synthesize. Pass Midpage opinion IDs directly for historical SCOTUS cases.
- **CourtListener `search_case_law`** — completeness check for Synthesize topic pages.

---

## Scoring (every run)

1. Open `rubric/<phase>.md` for the active phase. Compute raw 0-to-5 scores per criterion.
2. Compute the weighted average. Round to one decimal. Check red flags.
3. Compare to rolling median of the last five runs for this phase from `.run-scores.jsonl`. More than 1.0 below median adds `regression-vs-median` to red flags.
4. Append one JSON line to `.run-scores.jsonl` (bash `>>`, do NOT Read the file first).
5. Red flags become a pending issue for the next phase.

---

## Required end-of-run updates

1. **CHANGELOG.md** — append ONE run entry at the bottom with: phase, timestamp, files_scanned, files_created, files_edited, issues_found, issues_fixed, run score, red flags, one-line summary, list of source files processed (Ingest only), and pending count. Use bash `>>` for the append. If PENDING ISSUES at the top of the file needs a change, read just the top 40 lines and Edit.
2. **`.vault-maintenance-state.json`** — set `last_run`, update `pending_issues` and `next_phase`, refresh `last_phase` and `last_phase_at`, refresh the matching `phase_timestamps[<phase>]` field, set `notes` to a one-paragraph summary of the run. **Phase history is no longer kept inside state.** Append the run record as a single JSONL line to `archive/phase-history-YYYY-MM.jsonl` (month keyed by the run's own UTC timestamp). The append is the system of record for run-by-run history. State now carries only a pointer field `phase_history_log` whose value is `archive/phase-history-{YYYY-MM}.jsonl`; do not re-introduce a `phase_history` array in state. Cardinal rule: every phase MUST write its own record to the JSONL log before exiting, even on partial failures. A convenient bash pattern: `MONTH=$(date -u +%Y-%m); echo "$RUN_RECORD_JSON" >> "archive/phase-history-${MONTH}.jsonl"`. Pending-issue array still lives in state because it is read every run; if it crosses ~30 entries, spin the oldest into `archive/pending-issues-YYYY-MM.jsonl` first and then trim the live array, same archive-before-trim pattern.
3. **`.ingested-files.jsonl`** — only if Ingest ran.
4. **`BUILD_NARRATIVE_YYYY-MM.md`** (current month) — append ONE paragraph (not two to four) using bash `>>`. Do NOT Read the narrative file before appending. Include specific case names and doctrines.
5. **LESSONS.md** — only append if a new gotcha was discovered this run AND the file is under 35 entries. Otherwise log the lesson to `pending_issues` with type `lesson-candidate` for the next consolidation sweep.
6. **PROJECT_PRIMER.md** — skip unless the vault structure changed.

---

## Cardinal rules

- Never delete wiki content. Only add, fix structure, or flag.
- **Archive before trim.** When any bounded-size structure hits its cap (LESSONS.md 35-entry cap, `pending_issues` ~30-entry cap, or any future equivalent), spin the overflow to a file under `archive/` before trimming the live copy. Truncation without a prior archive write is forbidden. Prior archived copies are themselves append-only and are re-merged into the canonical file during reconciliation passes rather than discarded. Phase history is exempt from this rule because it now lives entirely in `archive/phase-history-YYYY-MM.jsonl` (state holds only the `phase_history_log` pointer); the JSONL grows unbounded within a month and rotates automatically by month-keyed filename.
- Never modify `Source Materials/`.
- Always read a file immediately before editing it.
- Prefer Edit with precise `old_string` over Write. Never overwrite a non-empty file.
- Case briefs must meet the 9-section case-briefer standard.
- Key Quotations require Midpage-verified text with pin-cite URLs.
- Frontmatter must match the template schema for every page.
- When unsure about case details, call Midpage `analyzeOpinion` first, web fallback, and never fabricate.
- Finish every run with a one-line summary fit for a notification.
