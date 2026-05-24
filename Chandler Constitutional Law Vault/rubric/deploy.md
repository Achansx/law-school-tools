# Rubric: Deploy

Scale: 5 exemplary, 4 solid, 3 acceptable, 2 below expectations, 1 serious, 0 failure. Weighted average rounded to one decimal.

Deploy measures whether the published vault advances cleanly each cycle: a fresh build was uploaded, only the changed bytes went over the wire, the live manifest matches what was just built, and `last_deploy` actually moved forward. A deploy that "succeeded" but left the live site stale (cache hit, manifest mismatch, zombie deploy) is a Deploy failure even if the CLI exited zero. The criteria below are scoped to what Deploy can actually affect, so they should hit 5 across the board on a healthy rotation; sustained drops usually mean either Netlify is degraded or the build/upload command drifted.

| Criterion | Weight | Red Flag At | Method |
|-----------|--------|-------------|--------|
| content_hash_incremental_hit_rate | 0.12 | -- | Fraction of files Netlify reported as already uploaded vs. newly transferred. The CLI prints a line like `Uploading X files of Y`. (Y - X) / Y is the hit rate. 1.0 (zero new files) is normal when nothing changed and is fine: score 5. 0.5 to 1.0 -> 5. 0.2 to 0.5 -> 4. Below 0.2 with only a small markdown change in the rotation -> 2 AND a `deploy-low-incremental-hit-rate` red flag (the build is probably re-emitting unchanged JSON with a fresh timestamp). |
| wall_clock_within_cap | 0.08 | 1 | End-to-end wall clock from build start to manifest verification end. Cap is 90 seconds for a steady-state rotation (small content delta). Under 30s -> 5. 30 to 60s -> 4. 60 to 90s -> 3. 90 to 180s -> 2. Over 180s -> 1 AND a `deploy-slow` red flag for investigation (cold npx cache, network, or CDN issue). |
| manifest_verification_matches_dist | 0.18 | 1 | After deploy, fetch `https://constitutionallaw.netlify.app/manifest.json` and compare its `meta.counts` against the local `dist/manifest.json` written by Step 1's build. Equal on every key (`case`, `topic`, `lecture`, `total`) -> 5. Any mismatch -> 0 AND a `deploy-count-mismatch` red flag. This is the canonical "did we actually publish what we built" check. |
| last_deploy_timestamp_advanced | 0.13 | 1 | After Step 4, `last_deploy` in `.vault-maintenance-state.json` is strictly newer than its value at the start of this run AND newer than every `phase_timestamps[<phase>]` value (lint, enrich, expand, synthesize, verify) carried into this rotation. Yes -> 5. Equal/older (state-write skipped or failed) -> 0 AND a `deploy-state-not-advanced` red flag, the deploy itself may have succeeded but the gate will re-fire next cycle and burn the npx cache priming again. |
| zero_zombie_deploys | 0.10 | 0 | A "zombie" is a deploy that started (created a Netlify deploy record) but never reached the `ready` state in this run. Confirm via the deploy URL returned by the CLI: HTTP 200 on the published assets after the CLI prints `Deploy is live`. Zero zombies -> 5. One zombie -> 0 AND a `deploy-zombie` red flag listing the deploy ID for next-cycle cleanup. |
| page_sample_all_200 | 0.12 | 1 | Step 3.5a deterministic sample of 5 case briefs + 3 topics. Each fetched via HTTP GET against `/#/p/<id>` on the live site and verified for HTTP 200 plus title-in-body. All 8 pass -> 5. 1 failure -> 2 AND a `deploy-page-sample-failed` red flag. 2+ failures -> 0 AND the same red flag. The check catches the manifest-says-yes-but-pages-are-broken regression class that pure count comparison misses. |
| search_sanity_marbury_match | 0.07 | 1 | Step 3.5b: fetch live `/search.json`, confirm it has at least one entry whose title contains `Marbury` AND whose text contains `judicial review`. Hit -> 5. Miss -> 0 AND a `deploy-search-sanity-failed` red flag. Marbury is the canonical anchor; if the live search index cannot find it the index is corrupt or truncated. |
| source_sample_all_200 | 0.10 | 1 | Step 3.5c deterministic sample of 5 Source Materials filenames pulled from manifest pages with non-empty `source_files`. HEAD against `/source/<encoded>` and verify HTTP 200 plus a Content-Type matching the file extension (PDF or PPTX). All 5 pass -> 5. 1 failure -> 2 AND a `deploy-source-sample-failed` red flag. 2+ failures -> 0 AND the same red flag. Catches partial Source Materials upload, which manifest-counts cannot. |
| scope_discipline | 0.10 | 0 | Deploy stayed inside its declared scope, build, upload, manifest verify, state-write. No vault content edits, no rubric changes, no opportunistic Lint-style fixes during the build directory. The set of files_edited under the vault root (excluding `.site/dist/`, `.vault-maintenance-state.json`, `CHANGELOG.md`, `BUILD_NARRATIVE_*.md`, `.run-scores.jsonl`) is empty. Strict scope -> 5. One out-of-scope edit (with note) -> 3. Multiple edits to vault content -> 0 AND a `deploy-out-of-scope` red flag. |
| brevity | 0.05 | 0 | This run's CHANGELOG entry stays inside the 120-word cap and uses the fixed shape from SKILL.md Step 2.3 (Did/Found/Files/Score/State bullets, optional fenced JSON extras — no prose paragraphs). The BUILD_NARRATIVE paragraph stays inside the 80-word cap (Deploy may use a single sentence). Compliant on both -> 5. One overflow under 50% over cap -> 3. Either overflow over 50% over OR per-phase JSON extras rendered as prose -> 0 AND a red flag. |

## Red flags

- Manifest counts on the live site disagree with the local `dist/manifest.json` (something was built but not published, or the published bundle is stale).
- Wall clock exceeded 180 seconds — usually cold npx cache or network, but worth a one-line note in CHANGELOG so the pattern is visible if it recurs.
- Incremental hit rate fell below 0.2 with no corresponding content change — the build is probably stamping fresh timestamps into otherwise unchanged JSON, defeating Netlify's content-hash dedupe.
- `last_deploy` did not advance after a deploy the rest of the rubric scored as successful (the state file write failed or the path lookup is wrong).
- A Netlify deploy record was created but never reached `ready` (zombie). Surface the deploy ID so the next Deploy cycle can clean it up before re-publishing.
- The PAT at `.site/.netlify-token` was missing AND no Netlify MCP fallback was attempted — Deploy should never silently skip when the token is absent; it should log a `deploy-token-missing` pending issue and abort.

## Regression check

Compare the weighted score to the rolling median of the last five Deploy runs in `.run-scores.jsonl`. Delta greater than 1.0 below median adds `regression-vs-median` to red flags. Deploy is a steady-state phase: the expected score is 5.0 nearly every run on a healthy rotation. A sustained drop usually points at one of three things: a Netlify product change (CLI flag deprecated, API surface moved), a build-script regression that bloats the bundle, or PAT/credential drift. Investigate the actual cause before normalizing the rubric to the new lower number.

## Pending-issue lifecycle

Deploy opens its own issues with `applies_to_phase: deploy` and closes them on the next successful Deploy run. The issues never wait for Lint or Verify to pick them up — they belong to Deploy from open to close.

Standard issue types Deploy emits:
- `deploy-build-failed` — Step 1 (build) returned non-zero. Carries the stderr tail in `metadata.stderr_tail`.
- `deploy-token-missing` — `.site/.netlify-token` not present and Netlify MCP unavailable. Carries the path that was checked.
- `deploy-count-mismatch` — Step 3 manifest verification failed. Carries `metadata.local_counts` and `metadata.live_counts`.
- `deploy-zombie` — A deploy record was created but never reached `ready`. Carries `metadata.deploy_id` for cleanup.
- `deploy-state-not-advanced` — `last_deploy` was not updated despite an apparently successful deploy. Carries the attempted timestamp.
- `deploy-page-sample-failed` — Step 3.5a sample of 5 case briefs + 3 topics returned at least one non-200 or title-missing. Carries `metadata.failed_sample`.
- `deploy-search-sanity-failed` — Step 3.5b "Marbury" sanity probe found no matching entry in the live `search.json`. Carries `metadata.entries_seen` and `metadata.marbury_match`.
- `deploy-source-sample-failed` — Step 3.5c sample of 5 Source Materials downloads returned at least one non-200 or wrong Content-Type. Carries `metadata.failed_sample`.

When Deploy retries on the next cycle and the underlying condition is gone, it closes the prior issue inline and notes the close in the run's CHANGELOG entry. If three consecutive Deploy runs hit the same issue type, escalate by appending a `deploy-recurring-failure` lesson candidate to `pending_issues` for the next Consolidate sweep.
