---
section: "08"
fact_type: example
source_path: "Chandler Constitutional Law Vault/DEPLOY.md"
verified: true
notes: "The deploy mechanic. Section VIII needs to be concrete about how a vault edit reaches the live site. Three-tier fallback chain: Netlify CLI direct upload with a local PAT (preferred, zero build minutes); Netlify MCP fallback (consumes build minutes); deploy.sh shell wrapper as last resort. The cardinal rule that the token is gitignored and never committed is the substantive piece — the deploy is reproducible from a scheduled task without leaking credentials and without a build-minutes meter. Section VIII can cite the specific site ID and the netlify.toml that disables Netlify's post-processing because the build is fully owned by the Python script."
---

The deploy is a direct CLI upload to Netlify using a local personal access token (PAT) that is gitignored. The `DEPLOY.md` procedure documents a three-tier fallback chain: the Netlify CLI direct upload is the preferred path because it does not consume Netlify build minutes; the Netlify MCP is the fallback when the PAT is missing (consumes build minutes); a shell wrapper, `.site/deploy.sh`, is the last resort when the CLI itself fails for an environment-specific reason. The Netlify site itself disables all post-processing (`skip_processing = true`) and registers a single SPA-style redirect (`/* /index.html 200`) so the build artifact uploaded is exactly the artifact served. Section VIII can name the deploy as scriptable, credentialed by a local file, and free of any hidden remote build step. Section IX's cost-and-labor table inherits the build-minutes-zero claim from this card.

Exact source quote, `Chandler Constitutional Law Vault/DEPLOY.md` lines 50 to 64 (preferred CLI direct-upload path):

> **Preferred path: Netlify CLI direct upload.** This is the canonical path because it does not consume Netlify build minutes and uses the local PAT, so deploys are reproducible from the scheduled task without proxy-token TTL pressure.
>
> ```bash
> # Prime npx cache once per cold environment so the second invocation is instant.
> npx -y netlify-cli@latest --version >/dev/null 2>&1 || true
>
> cd "$VAULT_DIR/.site/dist"
> NETLIFY_AUTH_TOKEN="$(cat "$VAULT_DIR/.site/.netlify-token")" \
>   npx -y netlify-cli@latest deploy \
>     --no-build \
>     --prod \
>     --dir . \
>     --site f78a098b-9a9e-412a-8d4f-dd8ccda13bfe \
>     --auth "$NETLIFY_AUTH_TOKEN"
> ```

And `Chandler Constitutional Law Vault/.site/dist/netlify.toml` lines 1 to 12 (the deployed Netlify configuration):

> [build]
>   publish = "."
>   command = ""
>
> [[redirects]]
>   from = "/*"
>   to = "/index.html"
>   status = 200
>
> [build.processing]
>   skip_processing = true
