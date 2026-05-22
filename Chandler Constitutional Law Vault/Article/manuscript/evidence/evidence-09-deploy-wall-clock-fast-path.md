---
section: "09"
fact_type: statistic
source_path: "Chandler Constitutional Law Vault/LESSONS.md"
verified: true
notes: "Anchored deploy-phase wall-clock figures the article can cite. Vault LESSONS.md item 1 in the Deployment section records that fast_deploy.py 'completes in ~6s, fits inside the 45s cap'; vault CHANGELOG entries from the same week record a clean CLI-path deploy at ~16 seconds build plus ~8 seconds upload on the 205-page corpus (CHANGELOG 2026-05-01 entry). These are the wall-clock numbers Section IX's deploy-phase line should carry verbatim rather than fabricating. The wall-clock anchor is what the cost-table line uses to back-compute the deploy-phase per-tick local compute cost (six to twenty-four seconds of sandbox time, depending on path), and to anchor Section VIII's PI-018 closing condition on a primary-source vault figure rather than a guess. DEPLOY.md Step 3.5 also caps the post-deploy verification budget at 'roughly 10 to 15 seconds total' so the full deploy-phase wall-clock floor reads as roughly 20 to 40 seconds end-to-end. The 'roughly' qualifier matters: Section IX's prose should hedge by routing through DEPLOY.md and the CHANGELOG rather than asserting a single point estimate."
---

The vault LESSONS.md Deployment section records that `fast_deploy.py` completes in approximately six seconds and fits inside the 45-second sandbox cap, and the vault CHANGELOG entry from 2026-05-01 records a clean CLI-path deploy at approximately sixteen seconds build plus approximately eight seconds upload on the 205-page corpus. The DEPLOY.md Step 3.5 post-deploy verification budget is approximately ten to fifteen seconds for the three sub-checks (page sample, search sanity probe, source-materials sample), so the full deploy-phase wall-clock floor reads as approximately twenty to forty seconds end-to-end depending on which upload path the run takes. Section IX's deploy-phase cost line closes PI-018 by citing these vault-primary figures rather than fabricating a point estimate, and the prose should hedge through DEPLOY.md and the CHANGELOG ranges rather than asserting a single number that future runs will silently drift past.

Exact source quote, `Chandler Constitutional Law Vault/LESSONS.md` lines 115 to 117 (Deployment item 1):

> **Deploy: prefer `fast_deploy.py`; CLI cold-start risks the 45s cap; `--no-build` is required [...].** Five patterns:
> 1. `.site/fast_deploy.py` walks `dist/`, POSTs the manifest, uploads only required bytes, calls finalize. Completes in ~6s, fits inside the 45s cap. First-choice path in `DEPLOY.md` ahead of the CLI.

And `Chandler Constitutional Law Vault/CHANGELOG.md` 2026-05-01 deploy entry (line 1163):

> Build exit 0 in ~16s; counts {case 100, topic 28, lecture 77, total 205}; 387 files / 454 MB to dist/source. Deploy via netlify-cli `--no-build --prod --dir .` from .site/dist; CDN requested 5 files; wall clock 8s. Verification: manifest matches dist on every key.

And `Chandler Constitutional Law Vault/DEPLOY.md` Step 3.5 (line 98):

> All three sub-checks run AFTER the manifest count check passes and BEFORE Step 4 advances `last_deploy`. [...] Capture the wall-clock cost of all three in the run summary; the budget is roughly 10 to 15 seconds total (8 GETs + 1 search.json fetch + 5 HEADs against a CDN).
