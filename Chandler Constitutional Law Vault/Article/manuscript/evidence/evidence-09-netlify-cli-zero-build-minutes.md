---
section: "09"
fact_type: argument
source_path: "Chandler Constitutional Law Vault/DEPLOY.md"
verified: true
notes: "The hosting-cost architectural property that lets the deploy phase land at zero marginal hosting cost on Netlify's free tier under normal operation. DEPLOY.md Step 2 names the Netlify CLI direct-upload path as canonical specifically because it does not consume Netlify build minutes, and explicitly demotes the Netlify MCP fallback because it does consume build minutes. The cost-table line for Section VIII's deploy phase (PI-018) inherits this property: the preferred path is free-tier-bounded by file count and bandwidth, not by build-minute throughput, and the per-tick deploy cost reduces to the CLI invocation's local wall-clock plus the bytes-on-the-wire upload. The honest hedge is the credit-block pattern: when account credits run out (see evidence-09-credit-block-as-external-cost-signal), the free-tier ceiling reasserts itself and deploys are blocked until human action restores credits or upgrades the tier. Section IX's deploy-phase line should carry the qualitative architectural property (zero Netlify build minutes on the preferred path) plus the credit-block hedge, not a fabricated dollar figure pretending Netlify is free under all conditions."
---

The DEPLOY.md procedure names the Netlify CLI direct-upload path as canonical specifically because it does not consume Netlify build minutes. The Netlify MCP fallback path is demoted because it does. This is the architectural property that lets Section IX's deploy-phase cost line land at zero marginal hosting cost on Netlify's free tier under normal operation; the per-tick deploy cost reduces to the CLI invocation's local wall-clock and the bytes-on-the-wire upload, with no build-minute meter accruing on Netlify's side. The hedge is the credit-block pattern documented in vault `LESSONS.md` and CHANGELOG entries from 2026-05-07: when account credits exhaust, the free-tier ceiling reasserts itself and deploys are blocked with HTTP 403 until human action restores credits or upgrades the tier. Section IX's deploy-phase line should carry the qualitative architectural property plus the credit-block hedge, not a fabricated dollar figure that pretends Netlify is free under all conditions. PI-018 (Section VIII deploy-phase cost line) closes through this card plus the credit-block card plus a snapshot-date specific Netlify-pricing-page WebSearch in the Cite tick.

Exact source quote, `Chandler Constitutional Law Vault/DEPLOY.md` Step 2 (lines 48 to 50):

> ### Step 2 — Deploy
>
> **Preferred path: Netlify CLI direct upload.** This is the canonical path because it does not consume Netlify build minutes and uses the local PAT, so deploys are reproducible from the scheduled task without proxy-token TTL pressure.

And `DEPLOY.md` line 70 (MCP fallback demotion):

> **Fallback path: Netlify MCP.** Call `netlify-deploy-services-updater` with `operation: deploy-site` and `siteId: f78a098b-9a9e-412a-8d4f-dd8ccda13bfe`. [...] This consumes Netlify build minutes; restore the PAT as soon as possible to drop back to the preferred path.
