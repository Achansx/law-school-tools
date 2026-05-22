---
section: "08"
fact_type: example
source_path: "Chandler Constitutional Law Vault/.site/dist/index.html"
verified: true
notes: "The hand-written SPA shell. Section VIII needs to be explicit that the shell is three files (index.html, app.js, style.css) plus the regenerated JSON, with hash-route navigation (#/cases, #/topics, #/p/<id>), a ⌘K search palette, light and dark themes, and PostHog analytics for usage tracking. The shell is small enough to fit on one screen of HTML. The PostHog write key is public-safe and filtered by property (app: 'con-law-wiki'), so Section VIII can name analytics without conceding any privacy-by-default surface area. The Netlify Forms stub (hidden page-feedback form) is what registers the form at build time so the Step 0 feedback intake described in evidence-08-feedback-form-loopback has something to read from."
---

The hand-written shell is three files: `index.html`, `app.js`, `style.css`. The shell defines a hash-route navigation (`#/cases`, `#/topics`, `#/lectures`, `#/recent`, `#/about`, `#/p/<id>`) so every page in the corpus is reachable through a stable URL, a ⌘K search palette wired to `search.json`, a theme toggle that respects the user's `prefers-color-scheme` and persists the choice in `localStorage`, and a hidden `page-feedback` Netlify form stub that registers the form at build time so the Step 0 feedback intake has something to read from. PostHog analytics are embedded with a public-safe write key, configured to ignore session recording (`disable_session_recording: true`), to respect Do Not Track (`respect_dnt: true`), and to register `app: 'con-law-wiki'` and `site: 'constitutionallaw.netlify.app'` on every event so the data is filterable to this vault and not aggregated with the author's other Netlify properties. The footer reads "Built from an Obsidian vault · rebuilt nightly by a rotating LLM cycle." Section VIII can quote that line as the deployed site's own self-description, and can name the shell's small surface area as the operational basis for the static-versus-chatbot risk argument that lands in Section XII.

Exact source quote, `Chandler Constitutional Law Vault/.site/dist/index.html` lines 84 to 100 (the body shell):

> <main id="app">
>   <div class="loader">Loading wiki&hellip;</div>
> </main>
>
> <footer class="sitefoot">
>   <span>Built from an Obsidian vault · rebuilt nightly by a rotating LLM cycle</span>
>   <span class="spacer"></span>
>   <span id="footer-stats"></span>
>   <a href="#/about">About this site</a>
>   <a href="mailto:achansx@gmail.com?subject=Con%20Law%20Wiki">Email Alan</a>
> </footer>
>
> <div id="palette-mount"></div>
>
> <script src="app.js?v=2026042202" defer></script>
