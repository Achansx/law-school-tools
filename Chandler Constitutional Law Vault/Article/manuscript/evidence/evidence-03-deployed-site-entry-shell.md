---
section: "03"
fact_type: example
source_path: "Chandler Constitutional Law Vault/.site/dist/index.html"
verified: true
notes: "The visible entry surface of the deployed site as a student first sees it: a top-nav with Dashboard, Cases, Topics, Lectures, Recent, and About, plus a ⌘K search-palette trigger. This is the artifact a student opens at https://constitutionallaw.netlify.app on day one of exam prep. Section III's walkthrough starts here. Different framing from evidence-08-spa-shell-and-routing, which covers the same shell as a build-pipeline output; this card covers the same shell as a student-facing navigation surface and that is the Section III ownership."
---

The deployed site greets a student with a fixed top-nav listing Dashboard, Cases, Topics, Lectures, Recent, and About, a search-palette trigger labeled "Search cases, topics, doctrines" bound to ⌘K, a course brand row reading "Con Law I · Prof. Chandler · Spring 2026," and a light or dark theme toggle. Each top-nav link routes inside the same shell via a hash route (`#/cases`, `#/topics`, `#/lectures`, `#/recent`, `#/about`) rather than a server-rendered page load. There is no login, no chat box, no account, no personalization surface: the shell is the same for every visitor. Section III opens by walking through this entry surface because it is the first thing a Con Law I student encounters and it sets the architectural expectation for everything that follows: this is a site you browse, not a system you query.

Exact source excerpt, `Chandler Constitutional Law Vault/.site/dist/index.html` lines 65 to 77 (top-nav block):

> ```html
>   <div class="cl-navlinks">
>     <a class="cl-navlink" href="#/" data-route="home">Dashboard</a>
>     <a class="cl-navlink" href="#/cases" data-route="cases">Cases</a>
>     <a class="cl-navlink" href="#/topics" data-route="topics">Topics</a>
>     <a class="cl-navlink" href="#/lectures" data-route="lectures">Lectures</a>
>     <a class="cl-navlink" href="#/recent" data-route="recent">Recent</a>
>     <a class="cl-navlink" href="#/about" data-route="about">About</a>
>   </div>
>   <button class="cl-search" id="palette-trigger" type="button" aria-label="Open search palette">
>     <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
>     <span class="cl-search-text">Search cases, topics, doctrines&hellip;</span>
>     <kbd>⌘K</kbd>
>   </button>
> ```

Exact source excerpt, `Chandler Constitutional Law Vault/.site/dist/index.html` lines 60 to 64 (brand block):

> ```html
>     <span>
>       <span class="cl-brand-text">Con Law I</span>
>       <span class="cl-brand-meta">Prof. <b>Chandler</b> · Spring 2026</span>
>     </span>
> ```
