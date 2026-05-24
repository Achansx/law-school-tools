#!/usr/bin/env python3
"""Build pages.json and search index from the Chandler Con Law Vault.

Produces:
- pages.json: full corpus (frontmatter + rendered HTML + plaintext for search)
- manifest.json: lightweight list of pages for index/nav
- search.json: compact index {id, title, kind, area, doctrines, text}
"""
import json
import os
import re
import shutil
import sys
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import quote as _urlquote

import yaml
from markdown_it import MarkdownIt


def _json_default(o):
    # YAML can return datetime.date for frontmatter like `verified: 2026-04-17`
    try:
        from datetime import date, datetime as _dt
        if isinstance(o, (date, _dt)):
            return o.isoformat()
    except Exception:
        pass
    return str(o)

VAULT = Path(os.environ.get("VAULT_DIR", "/sessions/adoring-dreamy-hypatia/mnt/Chandler Constitutional Law Vault"))
OUT   = Path(os.environ.get("OUT_DIR", "/sessions/adoring-dreamy-hypatia/mnt/outputs/conlaw-site/dist"))
KINDS = [("Cases", "case"), ("Topics", "topic"), ("Lectures", "lecture")]

WIKILINK_RE  = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
CALLOUT_RE   = re.compile(r"^> \[!([a-z]+)\](.*)$", re.IGNORECASE)

md = MarkdownIt("commonmark", {"html": True, "linkify": True, "breaks": False}).enable("table").enable("strikethrough")


def slugify(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def page_id(kind: str, stem: str) -> str:
    return f"{kind}/{slugify(stem)}"


def parse_frontmatter(text: str, source_path: str = "<unknown>"):
    """Parse YAML frontmatter at the head of a markdown file.

    Returns a 3-tuple (frontmatter_dict, body_str, error_or_none). The error
    slot is None on success and a {"path", "reason", "yaml_excerpt"} dict on
    parse failure. Callers that want the legacy 2-tuple shape can ignore the
    third element. The build pipeline collects errors into build_errors.json
    next to the other dist artifacts so a malformed page is visible to Lint
    rather than silently erased into an empty frontmatter dict.
    """
    if not text.startswith("---"):
        return {}, text, None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text, {
            "path": source_path,
            "reason": "frontmatter delimiter not closed (no second `---`)",
            "yaml_excerpt": text[:200].replace("\n", "\\n"),
        }
    raw_yaml = parts[1]
    body = parts[2].lstrip("\n")
    try:
        fm = yaml.safe_load(raw_yaml) or {}
        if not isinstance(fm, dict):
            return {}, body, {
                "path": source_path,
                "reason": f"frontmatter parsed to {type(fm).__name__}, expected mapping",
                "yaml_excerpt": raw_yaml[:200].replace("\n", "\\n"),
            }
        return fm, body, None
    except yaml.YAMLError as exc:
        return {}, body, {
            "path": source_path,
            "reason": f"yaml.YAMLError: {str(exc)[:300]}",
            "yaml_excerpt": raw_yaml[:200].replace("\n", "\\n"),
        }
    except Exception as exc:
        return {}, body, {
            "path": source_path,
            "reason": f"{type(exc).__name__}: {str(exc)[:300]}",
            "yaml_excerpt": raw_yaml[:200].replace("\n", "\\n"),
        }


def normalize_wikilink_target(target: str, pages_by_name):
    """Resolve a wiki-link target (possibly with folder) to a pages-json id."""
    target = target.strip()
    # strip .md extension
    if target.endswith(".md"):
        target = target[:-3]
    # folder-qualified target (e.g. "Cases/McCulloch v Maryland (1819)")
    if "/" in target:
        folder, name = target.split("/", 1)
        folder = folder.strip()
        name = name.strip()
        kind_map = {"Cases": "case", "Topics": "topic", "Lectures": "lecture"}
        if folder in kind_map:
            pid = f"{kind_map[folder]}/{slugify(name)}"
            if pid in pages_by_name["by_id"]:
                return pid
    # bare name — search all kinds
    hit = pages_by_name["by_slug"].get(slugify(target))
    return hit


def render_markdown(body: str, pages_by_name) -> str:
    # Convert wikilinks to markdown links before rendering
    def repl(match):
        target, display = match.group(1), match.group(2)
        target_clean = target.strip()
        label = display if display else target_clean.split("/")[-1]
        # Strip a trailing .md on the visible label so "Foo.md" renders as "Foo".
        if not display and label.endswith(".md"):
            label = label[:-3]
        # Source Materials wikilinks render as direct download links served from
        # /source/<url-encoded-filename>. The build also copies the Source
        # Materials folder into OUT/source so these hrefs actually resolve on
        # the deployed site. We emit the <a> tag directly (mirroring the
        # broken-link span pattern above) so markdown-it does not mangle the
        # URL-encoded filename.
        if target_clean.startswith("Source Materials/"):
            sub = target_clean[len("Source Materials/"):]
            href = "source/" + "/".join(_urlquote(part) for part in sub.split("/"))
            return f'<a class="source-download" href="{href}" download>{label}</a>'
        resolved = normalize_wikilink_target(target_clean, pages_by_name)
        if resolved:
            return f"[{label}](#/p/{resolved})"
        return f'<span class="broken-link" title="No page found for {target_clean}">{label}</span>'

    body = WIKILINK_RE.sub(repl, body)

    # Convert Obsidian callouts to plain blockquotes with a data-attribute
    lines = []
    in_callout = False
    callout_kind = None
    for line in body.split("\n"):
        m = CALLOUT_RE.match(line)
        if m:
            callout_kind = m.group(1).lower()
            heading = (m.group(2) or "").strip()
            lines.append(f'<div class="callout callout-{callout_kind}">')
            if heading:
                lines.append(f'<div class="callout-title">{heading}</div>')
            lines.append('<div class="callout-body">')
            in_callout = True
            continue
        if in_callout:
            if line.startswith("> "):
                lines.append(line[2:])
                continue
            elif line.strip() == ">":
                lines.append("")
                continue
            else:
                lines.append("</div></div>")
                in_callout = False
        lines.append(line)
    if in_callout:
        lines.append("</div></div>")

    body = "\n".join(lines)
    return md.render(body)


def extract_headings(body_md: str):
    headings = []
    for line in body_md.split("\n"):
        m = re.match(r"^(#{1,4})\s+(.+?)\s*$", line)
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            if level >= 2:  # TOC starts at H2
                headings.append({"level": level, "text": text, "slug": slugify(text)})
    return headings


# ---------- Smart extractors for the editorial redesign ----------

# Map free-form area / topic strings into one of the four families used by
# the topics page's four-family grid. The redesign collapses every doctrine
# into Federalism / Separation of Powers / Individual Rights / Justiciability.
_FAMILY_MAP = {
    "federalism": "Federalism",
    "commerce": "Federalism",
    "commerce clause": "Federalism",
    "dormant commerce": "Federalism",
    "necessary and proper": "Federalism",
    "necessary & proper": "Federalism",
    "enumerated powers": "Federalism",
    "anti-commandeering": "Federalism",
    "tenth amendment": "Federalism",
    "spending clause": "Federalism",
    "tax immunity": "Federalism",

    "separation of powers": "Separation of Powers",
    "executive power": "Separation of Powers",
    "commander in chief": "Separation of Powers",
    "presidential immunity": "Separation of Powers",
    "major questions": "Separation of Powers",
    "major questions doctrine": "Separation of Powers",
    "nondelegation": "Separation of Powers",
    "appointments": "Separation of Powers",
    "removal": "Separation of Powers",
    "appointments and removal": "Separation of Powers",
    "judicial review": "Separation of Powers",
    "administrative law": "Separation of Powers",
    "chevron": "Separation of Powers",
    "loper bright": "Separation of Powers",

    "individual rights": "Individual Rights",
    "equal protection": "Individual Rights",
    "substantive due process": "Individual Rights",
    "free speech": "Individual Rights",
    "first amendment": "Individual Rights",
    "free exercise": "Individual Rights",
    "establishment clause": "Individual Rights",
    "second amendment": "Individual Rights",
    "incorporation": "Individual Rights",
    "fourteenth amendment": "Individual Rights",
    "thirteenth amendment": "Individual Rights",
    "affirmative action": "Individual Rights",
    "compelled speech": "Individual Rights",
    "public accommodations": "Individual Rights",
    "originalism": "Individual Rights",

    "justiciability": "Justiciability",
    "standing": "Justiciability",
    "ripeness": "Justiciability",
    "mootness": "Justiciability",
    "political question": "Justiciability",
    "political question doctrine": "Justiciability",
    "sovereign immunity": "Justiciability",
    "case or controversy": "Justiciability",
}


def bucket_family(*candidates) -> str | None:
    """Map any of the candidate strings to one of the four topic families."""
    for c in candidates:
        if not c:
            continue
        if isinstance(c, list):
            for sub in c:
                got = bucket_family(sub)
                if got:
                    return got
            continue
        key = str(c).strip().lower()
        if key in _FAMILY_MAP:
            return _FAMILY_MAP[key]
        # partial match against keys
        for needle, fam in _FAMILY_MAP.items():
            if needle in key:
                return fam
    return None


def _truncate_at_sentence(text: str, max_chars: int) -> str:
    """Cut text at the last sentence boundary at or before max_chars. Falls
    back to a word boundary so we never end mid-word like 'staggering pol'."""
    if len(text) <= max_chars:
        return text
    window = text[:max_chars]
    # Prefer the last sentence-ending punctuation followed by a space.
    for end in (". ", "? ", "! "):
        i = window.rfind(end)
        if i >= max_chars * 0.5:  # don't cut absurdly short
            return text[:i + 1]
    # Fall back to last whitespace.
    i = window.rfind(" ")
    if i >= max_chars * 0.5:
        return text[:i] + "…"
    return window + "…"


def _section_text(body_md: str, heading: str, max_chars: int = 600) -> str:
    """Return the first prose paragraph under an H2/H3 heading. Strips
    blockquote markers, leading list markers, and bold so the snippet reads
    cleanly in a holding bar / lineage row. Returns "" if heading not found.
    """
    pattern = re.compile(rf"^#{{2,3}}\s+{re.escape(heading)}\s*$", re.IGNORECASE | re.MULTILINE)
    m = pattern.search(body_md)
    if not m:
        return ""
    rest = body_md[m.end():]
    para_lines = []
    for line in rest.split("\n"):
        s = line.rstrip()
        if not s.strip():
            if para_lines:
                break
            continue
        if s.startswith("#"):
            break
        if s.startswith("---"):
            break
        # Strip a leading "> " from blockquotes (Memory Jogger uses these)
        if s.startswith("> "):
            s = s[2:]
        elif s.lstrip().startswith("- ") or s.lstrip().startswith("* "):
            # only swallow the first bullet for the snippet
            s = s.lstrip()[2:]
        para_lines.append(s)
    text = " ".join(para_lines).strip()
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"\s+", " ", text)
    return _truncate_at_sentence(text.strip(), max_chars)


def extract_holding_bar(body_md: str, fm: dict, doctrines: list) -> dict:
    """Promote four fields into a structured holding bar. Frontmatter wins
    over body extraction. Body fallbacks: Memory Jogger → holding, Holding
    section → reasoning if no separate field, Facts/Procedural → issue.
    """
    # Holding never gets truncated — it's the most important field on the
    # page; cutting it produces dishonest "...staggering economic and pol"
    # endings. Reasoning/issue tolerate a soft cap because they're flavor.
    holding = fm.get("holding") or _section_text(body_md, "Memory Jogger", 100_000)
    if not holding:
        holding = _section_text(body_md, "Holding", 100_000)

    reasoning = fm.get("reasoning") or ""
    if not reasoning:
        # Take the second paragraph after Holding if it exists, else the
        # whole Holding section if Memory Jogger already supplied the holding.
        h_section = _section_text(body_md, "Holding", 100_000)
        if h_section and h_section != holding:
            reasoning = h_section
        else:
            reasoning = _section_text(body_md, "Reasoning", 100_000) or _section_text(body_md, "Analysis", 100_000)

    issue = fm.get("issue") or ""
    if not issue:
        # Find the first sentence containing a "?" anywhere in Facts/Procedural.
        candidate = _section_text(body_md, "Issue", 400)
        if candidate:
            issue = candidate
        else:
            facts = _section_text(body_md, "Facts", 1200) or _section_text(body_md, "Procedural History", 1200)
            for sent in re.split(r"(?<=[.?!])\s+", facts):
                if "?" in sent:
                    issue = sent.strip()
                    break

    family = fm.get("doctrine_family") or fm.get("family")
    if not family:
        family = bucket_family(fm.get("area"), *(doctrines or []))

    return {
        "issue": issue or "",
        "holding": holding or "",
        "reasoning": reasoning or "",
        "family": family or "",
    }


_VOTE_RE = re.compile(r"\b(\d{1,2}\s*[-–—]\s*\d{1,2})\b")


def extract_citation_meta(body_md: str, fm: dict) -> dict:
    """Surface the courtroom metadata the case page header / meta card need.
    Frontmatter wins; falls back to the # Judicial Votes block which
    consistently lists Majority/Author/Vote in the existing vault format.
    """
    out = {
        "argued":      fm.get("argued") or fm.get("argued_at") or "",
        "decided":     fm.get("decided") or fm.get("decided_at") or "",
        "panel":       fm.get("panel") or "",
        "author":      fm.get("author") or "",
        "vote":        fm.get("vote") or "",
        "disposition": fm.get("disposition") or "",
    }
    if out["author"] and out["vote"]:
        return out

    votes = _section_text(body_md, "Judicial Votes", 800)
    if not votes:
        return out
    # "Majority: Gorsuch (joined by Roberts, C.J., …) — 6-3" — capture
    # surname only, then optional joined-by parenthetical, then vote.
    m = re.search(r"Majority\s*[:\-–]\s*([A-Z][A-Za-z\.\-']+(?:[ ,]+(?:C\.J\.|J\.))?)\s*(?:\(joined by[^)]*\))?\s*[—–\-]?\s*(\d{1,2}\s*[-–]\s*\d{1,2})?", votes)
    if m:
        if not out["author"]:
            out["author"] = m.group(1).strip().rstrip(",.")
        if not out["vote"] and m.group(2):
            out["vote"] = m.group(2).replace("–", "-").replace(" ", "")
    if not out["vote"]:
        v = _VOTE_RE.search(votes)
        if v:
            out["vote"] = v.group(1).replace("–", "-").replace(" ", "")
    return out


def extract_lineage(fm: dict) -> dict:
    """Pass through authority lineage from frontmatter. Normalize each list
    to a list of strings (frontmatter authors sometimes write a single
    string). Empty lists are fine — the case page falls back to backlinks.
    """
    def _aslist(v):
        if v is None:
            return []
        if isinstance(v, str):
            return [v]
        if isinstance(v, list):
            return [str(x) for x in v if x]
        return [str(v)]

    return {
        "relies_on":     _aslist(fm.get("relies_on")),
        "distinguishes": _aslist(fm.get("distinguishes")),
        "applied_in":    _aslist(fm.get("applied_in")),
        "overrules":     fm.get("overrules") or "",
        "overruled_by":  fm.get("overruled_by") or "",
    }


def plaintext(md_text: str) -> str:
    t = re.sub(r"```[\s\S]*?```", " ", md_text)
    t = WIKILINK_RE.sub(lambda m: m.group(2) or m.group(1), t)
    t = re.sub(r"[#>*_`~\-]+", " ", t)
    t = re.sub(r"\s+", " ", t)
    return t.strip()


def load_pages():
    raw = []
    by_slug = {}
    by_id = set()

    # First pass: list all files so wikilinks can resolve cross-folder
    for folder, kind in KINDS:
        folder_path = VAULT / folder
        if not folder_path.is_dir():
            continue
        for f in sorted(folder_path.glob("*.md")):
            stem = f.stem
            pid = page_id(kind, stem)
            by_id.add(pid)
            by_slug[slugify(stem)] = pid
            raw.append((kind, stem, f))

    resolver = {"by_id": by_id, "by_slug": by_slug}

    # Errors are collected here and surfaced via build_errors.json in main().
    # We attach the running list to load_pages itself so main() can read it
    # without a global; nothing else in the module needs it.
    load_pages.errors = []

    pages = []
    for kind, stem, f in raw:
        text = f.read_text(encoding="utf-8", errors="replace")
        rel_for_log = str(f.relative_to(VAULT))
        fm, body, fm_err = parse_frontmatter(text, source_path=rel_for_log)
        if fm_err is not None:
            load_pages.errors.append(fm_err)
        title = stem
        html = render_markdown(body, resolver)
        headings = extract_headings(body)

        # extract a lead paragraph (first non-blockquote, non-heading paragraph after any Memory Jogger)
        lead = ""
        if kind == "case":
            mj = re.search(r"##\s+Memory Jogger\s*\n+>\s*(.+?)\n", body)
            if mj:
                lead = mj.group(1).strip()
        if not lead:
            m2 = re.search(r"##\s+Overview\s*\n+([^\n#][^\n]+)", body)
            if m2:
                lead = m2.group(1).strip()
        if not lead:
            # first paragraph after H1
            m3 = re.search(r"\n\n([A-Z][^\n]{40,})", body)
            if m3:
                lead = m3.group(1).strip()
        lead = lead[:320]

        pid = page_id(kind, stem)

        # Normalize frontmatter fields
        area = fm.get("area") or fm.get("doctrines", [None])[0] if isinstance(fm.get("doctrines"), list) else fm.get("area")
        if isinstance(area, list):
            area = area[0] if area else None

        doctrines = fm.get("doctrines", []) or []
        concepts  = fm.get("concepts", []) or []
        citation  = fm.get("citation")
        year      = fm.get("year")
        court     = fm.get("court")
        status    = fm.get("status")

        page = {
            "id": pid,
            "kind": kind,
            "title": title,
            "slug": slugify(stem),
            "filename": str(f.relative_to(VAULT)),
            "frontmatter": fm,
            "html": html,
            "headings": headings,
            "lead": lead,
            "area": area,
            "doctrines": doctrines,
            "concepts": concepts,
            "citation": citation,
            "year": year,
            "court": court,
            "status": status,
        }

        # ---- Editorial-redesign enrichments ----
        # All additive; downstream consumers may ignore them. The redesign
        # gracefully degrades when any of these come back empty.
        if kind == "case":
            page["holding_bar"] = extract_holding_bar(body, fm, doctrines)
            page["citation_meta"] = extract_citation_meta(body, fm)
            page["lineage"] = extract_lineage(fm)
            # Display name for the case header — split on " v " / " v. "
            display = re.sub(r"\s*\(\d{4}\)\s*$", "", title)
            page["display_name"] = display
        elif kind == "topic":
            page["family"] = (
                fm.get("family") or fm.get("doctrinal_family")
                or bucket_family(area, title, *(doctrines or []))
                or ""
            )
            page["leading_cases"] = fm.get("key_cases") or fm.get("leading_cases") or []
            page["two_part_test"] = fm.get("two_part_test") or ""
            page["open_questions"] = fm.get("open_questions") or []
        elif kind == "lecture":
            # Carry through whatever the vault has set; renderers fall back
            # when fields are missing.
            page["week"] = fm.get("week")
            page["date"] = str(fm.get("date") or "")
            page["theme"] = fm.get("theme") or fm.get("topic_area") or ""
            page["cases_covered"] = fm.get("cases_covered") or fm.get("cases_discussed") or []
            page["is_current"] = bool(fm.get("is_current"))
            page["is_upcoming"] = bool(fm.get("is_upcoming"))

        pages.append(page)

    return pages


def build_manifest(pages):
    out = []
    for p in pages:
        row = {
            "id": p["id"],
            "kind": p["kind"],
            "title": p["title"],
            "lead": p["lead"],
            "area": p["area"],
            "year": p["year"],
            "doctrines": p["doctrines"][:5],
            "citation": p["citation"],
            "status": p["status"],
        }
        if p["kind"] == "case":
            hb = p.get("holding_bar") or {}
            row["holding"] = hb.get("holding") or ""
            row["family"] = hb.get("family") or ""
            row["court"] = p.get("court") or ""
            row["display_name"] = p.get("display_name") or p["title"]
        elif p["kind"] == "topic":
            row["family"] = p.get("family") or ""
            row["leading_cases"] = p.get("leading_cases") or []
        elif p["kind"] == "lecture":
            row["week"] = p.get("week")
            row["date"] = p.get("date") or ""
            row["theme"] = p.get("theme") or ""
            row["cases_covered"] = p.get("cases_covered") or []
            row["is_current"] = p.get("is_current") or False
            row["is_upcoming"] = p.get("is_upcoming") or False
        out.append(row)
    return out


def _case_sort_key(p):
    """Year desc, then title asc — used for both Prev/Next and dashboard
    'recent cases'. Cases without a year sink to the end."""
    y = p.get("year")
    try:
        y = -int(y) if y else 999_999
    except (TypeError, ValueError):
        y = 999_999
    return (y, p.get("title", ""))


def pick_featured_case(pages):
    """Heuristic: pick the case with the most-recent ISO `verified` date.
    Tiebreak by year desc, then by `cited_by` (if present), then by id.
    Cases with non-ISO `verified` (e.g. 'pending-enrich') are eligible only
    if no ISO-verified case exists.
    """
    cases = [p for p in pages if p["kind"] == "case"]
    if not cases:
        return None

    def key(p):
        fm = p.get("frontmatter") or {}
        v = str(fm.get("verified") or "")
        iso = bool(re.match(r"\d{4}-\d{2}-\d{2}", v))
        try:
            y = int(p.get("year") or 0)
        except (TypeError, ValueError):
            y = 0
        try:
            cb = int(fm.get("cited_by") or 0)
        except (TypeError, ValueError):
            cb = 0
        return (
            1 if iso else 0,
            v if iso else "",
            y,
            cb,
            -ord(p["id"][0]) if p["id"] else 0,  # last-resort tiebreak
        )

    return sorted(cases, key=key, reverse=True)[0]["id"]


def build_search(pages):
    out = []
    for p in pages:
        # strip HTML tags
        text = re.sub(r"<[^>]+>", " ", p["html"])
        text = re.sub(r"\s+", " ", text).strip()
        out.append({
            "id": p["id"],
            "kind": p["kind"],
            "title": p["title"],
            "area": p["area"],
            "doctrines": p["doctrines"],
            "text": text[:6000],
        })
    return out


def backlinks(pages):
    """Scan each page's HTML for hash links to other pages to build a backlink map."""
    links_to = {p["id"]: set() for p in pages}
    for p in pages:
        for m in re.finditer(r'href="#/p/([^"]+)"', p["html"]):
            target = m.group(1)
            if target != p["id"] and target in links_to:
                links_to[target].add(p["id"])
    return {pid: sorted(v) for pid, v in links_to.items()}


# ---------- Recent / ingestion status ----------

CHANGELOG_HEAD_RE = re.compile(
    r"^##\s+(.+?)\s*$",
    re.MULTILINE,
)
# Match a date / datetime token anywhere in a heading line.
CHANGELOG_DATE_RE = re.compile(
    r"(\d{4}-\d{2}-\d{2}(?:[ T]\d{2}:\d{2}(?::\d{2})?(?:Z|\s*UTC)?)?)"
)
PHASE_TOKENS = [
    "Ingest", "Lint", "Enrich", "Expand", "Synthesize", "Verify",
    "Consolidate", "Deploy", "Initial Setup", "Post-Setup Enhancements",
]


def parse_changelog(text: str, limit: int = 20):
    """Return a list of dicts {phase, timestamp, summary, bullets} newest first.

    The changelog headings have been written in many shapes over time. We try
    to extract a phase name and an ISO timestamp for each block, then capture
    a short summary line and up to six leading bullets.
    """
    # Split into sections by H2 headings, keep the heading with its body.
    parts = re.split(r"(?m)^(##\s+[^\n]+)\n", text)
    # parts[0] is the preamble, then alternating (heading, body)
    entries = []
    for i in range(1, len(parts), 2):
        heading_line = parts[i].strip()
        body = parts[i + 1] if i + 1 < len(parts) else ""
        heading = heading_line.lstrip("#").strip()
        if heading.upper().startswith("PENDING"):
            continue

        # Identify phase
        phase = None
        for tok in PHASE_TOKENS:
            if re.search(rf"\b{re.escape(tok)}\b", heading, re.IGNORECASE):
                phase = tok
                break
        if not phase:
            # fallback: first word
            phase = heading.split()[0]

        # Identify timestamp
        ts = None
        m = CHANGELOG_DATE_RE.search(heading)
        if m:
            raw = m.group(1)
            # Normalize " UTC" -> "Z", and space-between-date-and-time -> "T"
            norm = raw.replace(" UTC", "Z").replace(" ", "T", 1)
            if "T" in norm and not norm.endswith("Z") and len(norm) <= 16:
                norm = norm + ":00Z"
            elif "T" in norm and not norm.endswith("Z") and len(norm) <= 19:
                norm = norm + "Z"
            elif "T" not in norm:
                norm = norm + "T00:00:00Z"
            ts = norm

        # First non-empty, non-bullet line becomes summary. Collect a few bullets.
        summary = ""
        bullets = []
        for line in body.split("\n"):
            s = line.strip()
            if not s:
                continue
            if s.startswith("---"):
                break
            if s.startswith(("-", "*", "•")):
                b = re.sub(r"^[-*•]\s+", "", s)
                b = re.sub(r"\*\*([^*]+)\*\*", r"\1", b)
                bullets.append(b[:240])
                if len(bullets) >= 8:
                    break
            elif not summary:
                summary = re.sub(r"\*\*([^*]+)\*\*", r"\1", s)[:300]

        entries.append({
            "phase": phase,
            "title": heading,
            "timestamp": ts,
            "summary": summary,
            "bullets": bullets,
        })

    # Sort newest first on timestamp; entries without timestamps keep source order.
    entries_with_ts = [e for e in entries if e.get("timestamp")]
    entries_with_ts.sort(key=lambda e: e["timestamp"], reverse=True)
    # Merge: ts-sorted entries first, then untimed tail
    untimed = [e for e in entries if not e.get("timestamp")]
    combined = entries_with_ts + untimed
    return combined[:limit]


def build_recent(pages):
    """Build recent.json from vault state files and source folder."""
    out = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "changelog": [],
        "ingestion": {"processed": [], "skipped": [], "unprocessed": [], "broken_refs": [], "shared_sources": []},
        "pending_issues": [],
        "phase_history": [],
        "last_run": None,
        "last_deploy": None,
    }

    # --- Changelog ---
    cl = VAULT / "CHANGELOG.md"
    if cl.exists():
        out["changelog"] = parse_changelog(cl.read_text(encoding="utf-8", errors="replace"), limit=20)

    # --- Ingested files state ---
    # Source of truth is .ingested-files.jsonl (JSON Lines).
    # Each line is one record: a metadata record (`_record: "metadata"`) or a
    # bucketed record (`_bucket: "processed"|"skipped"|"failed"`).
    # Legacy .ingested-files.json (whole-file JSON with top-level processed/skipped
    # arrays) is read as a fallback so older snapshots still work.
    processed = []
    skipped = []
    ing_jsonl = VAULT / ".ingested-files.jsonl"
    ing_json  = VAULT / ".ingested-files.json"
    if ing_jsonl.exists():
        try:
            with ing_jsonl.open("r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        rec = json.loads(line)
                    except Exception:
                        continue
                    if rec.get("_record") == "metadata":
                        continue
                    bucket = rec.get("_bucket")
                    if bucket == "processed":
                        processed.append(rec)
                    elif bucket == "skipped":
                        skipped.append(rec)
                    # "failed" bucket exists but isn't surfaced on the public widget
        except Exception:
            processed, skipped = [], []
    elif ing_json.exists():
        try:
            ingested = json.loads(ing_json.read_text(encoding="utf-8"))
            processed = ingested.get("processed", []) or []
            skipped = ingested.get("skipped", []) or []
        except Exception:
            processed, skipped = [], []
    def _as_list(v):
        if v is None:
            return []
        if isinstance(v, list):
            return v
        return [v]

    out["ingestion"]["processed"] = [
        {
            "source": p.get("source", ""),
            "created": _as_list(p.get("created")),
            "timestamp": p.get("timestamp"),
            "type": p.get("type"),
        }
        for p in processed
    ]
    out["ingestion"]["skipped"] = [
        {
            "source": s.get("source", ""),
            "reason": s.get("reason", ""),
            "note": s.get("note", ""),
            "timestamp": s.get("timestamp"),
        }
        for s in skipped
    ]

    # --- Unprocessed source files ---
    known_sources = set()
    for p in processed:
        src = p.get("source")
        if src:
            known_sources.add(src)
            known_sources.add(Path(src).name)
    for s in skipped:
        src = s.get("source")
        if src:
            known_sources.add(src)
            known_sources.add(Path(src).name)

    source_dir = VAULT / "Source Materials"
    unprocessed = []
    ingestable_files = set()  # unique filenames of ingestable files in Source Materials/
    if source_dir.is_dir():
        exts = {".pdf", ".pptx", ".docx", ".potx"}
        for f in sorted(source_dir.rglob("*")):
            if not f.is_file():
                continue
            if f.suffix.lower() not in exts:
                continue
            ingestable_files.add(f.name)
            rel = f.relative_to(VAULT).as_posix()
            if rel in known_sources or f.name in known_sources:
                continue
            unprocessed.append({"path": rel, "size": f.stat().st_size})
    out["ingestion"]["unprocessed"] = unprocessed

    # --- Source coverage (file-based, not record-based) ---
    # The widget should report file coverage of files currently on disk, not
    # historical ingestion-event ratios. We intersect both the processed set
    # and the skipped set with the current ingestable_files inventory so that
    # historical entries for files that have since been moved or deleted
    # don't inflate the totals. Processed wins ties: a file that was processed
    # once and later re-skipped (e.g., after a metadata fix) counts as
    # "made a page."
    processed_names_all = set()
    for p in processed:
        src = p.get("source") or ""
        if src:
            processed_names_all.add(Path(src).name)
    skipped_names_all = set()
    for s in skipped:
        src = s.get("source") or ""
        if src:
            skipped_names_all.add(Path(src).name)

    processed_on_disk = processed_names_all & ingestable_files
    skipped_only_on_disk = (skipped_names_all - processed_names_all) & ingestable_files

    pages_created = len(processed_on_disk)
    intentionally_skipped = len(skipped_only_on_disk)
    unprocessed_count = len(unprocessed)
    ingestable_total = len(ingestable_files) or (pages_created + intentionally_skipped + unprocessed_count)
    coverage_denom = max(ingestable_total, 1)
    out["source_coverage"] = {
        "pages_created": pages_created,
        "intentionally_skipped": intentionally_skipped,
        "unprocessed": unprocessed_count,
        "ingestable_total": ingestable_total,
        "coverage_pct": round(100.0 * pages_created / coverage_denom, 1),
    }

    # --- Broken source_files refs (lecture frontmatter pointing at nonexistent files) ---
    broken = []
    shared = {}
    source_stem_index = {}
    if source_dir.is_dir():
        for f in source_dir.rglob("*"):
            if f.is_file():
                source_stem_index[f.name.lower()] = str(f.relative_to(VAULT).as_posix())

    for p in pages:
        if p["kind"] != "lecture":
            continue
        fm = p.get("frontmatter") or {}
        refs = fm.get("source_files") or fm.get("sources") or []
        if isinstance(refs, str):
            refs = [refs]
        for ref in refs:
            if not ref:
                continue
            ref_name = Path(str(ref)).name
            if ref_name.lower() not in source_stem_index:
                broken.append({
                    "page_id": p["id"],
                    "page_title": p["title"],
                    "missing": ref_name,
                })
            else:
                shared.setdefault(ref_name, []).append({"id": p["id"], "title": p["title"]})

    out["ingestion"]["broken_refs"] = broken
    out["ingestion"]["shared_sources"] = [
        {"source": k, "lectures": v}
        for k, v in sorted(shared.items())
        if len(v) > 1
    ]

    # --- Maintenance state ---
    state_file = VAULT / ".vault-maintenance-state.json"
    if state_file.exists():
        try:
            st = json.loads(state_file.read_text(encoding="utf-8"))
        except Exception:
            st = {}

        # Pending issues — only surface actively open ones on the public widget.
        # Issues with status "deferred-manual-verification", "verified-confirmed",
        # "partially-resolved", "ready", "wontfix", or "closed" are still in the
        # state file for audit history but should not display as live work.
        OPEN_STATUSES = {"open", ""}  # blank status treated as open
        issues = st.get("pending_issues", []) or []
        pid_by_slug = {p["slug"]: p["id"] for p in pages}
        pid_by_title = {p["title"]: p["id"] for p in pages}
        out_issues = []
        for iss in issues:
            status = (iss.get("status") or "").strip().lower()
            if status not in OPEN_STATUSES:
                continue
            target = iss.get("target") or iss.get("page") or iss.get("file") or ""
            page_id = iss.get("page_id")
            page_title = iss.get("page_title")
            if not page_id and target:
                stem = Path(str(target)).stem
                page_id = pid_by_slug.get(slugify(stem)) or pid_by_title.get(stem)
                page_title = stem
            out_issues.append({
                "type": iss.get("type") or iss.get("kind") or "issue",
                "status": status or "open",
                "target": target,
                "page_id": page_id,
                "page_title": page_title,
                "note": iss.get("note") or iss.get("description") or "",
                "detected": iss.get("detected") or iss.get("timestamp") or iss.get("flagged_at"),
            })
        out["pending_issues"] = out_issues

        # Phase history
        ph = st.get("phase_history", []) or []
        norm_ph = []
        for entry in ph:
            if isinstance(entry, dict):
                norm_ph.append({
                    "phase": entry.get("phase") or entry.get("name") or "",
                    "timestamp": entry.get("timestamp") or entry.get("when") or entry.get("at"),
                })
        norm_ph.sort(key=lambda e: e.get("timestamp") or "", reverse=True)
        out["phase_history"] = norm_ph

        last_run = st.get("last_run")
        if isinstance(last_run, dict):
            out["last_run"] = last_run
        elif isinstance(last_run, str):
            out["last_run"] = {"timestamp": last_run}

        last_deploy = st.get("last_deploy")
        if isinstance(last_deploy, dict):
            out["last_deploy"] = last_deploy
        elif isinstance(last_deploy, str):
            out["last_deploy"] = {"timestamp": last_deploy}

    return out


def copy_source_materials() -> dict:
    """Mirror VAULT/Source Materials into OUT/source so the deployed site can
    serve raw casebook PDFs, slide decks, and ancillary handouts as direct
    downloads. Wikilinks of the form `[[Source Materials/<name>]]` rendered by
    render_markdown point at /source/<urlencoded-name>; this function makes
    those URLs resolve. Hidden files and macOS metadata are skipped.
    """
    src_dir = VAULT / "Source Materials"
    dst_dir = OUT / "source"
    if not src_dir.is_dir():
        return {"copied": 0, "bytes": 0, "skipped": 0}
    if dst_dir.exists():
        # Some sandboxes (iCloud-mounted runs) choke on rmtree because of
        # quarantine-locked leftovers. `ignore_errors=True` lets us push through;
        # copy2 below overwrites anything that survived.
        shutil.rmtree(dst_dir, ignore_errors=True)
    dst_dir.mkdir(parents=True, exist_ok=True)
    copied = 0
    skipped = 0
    total_bytes = 0
    for f in src_dir.rglob("*"):
        if not f.is_file():
            continue
        # Skip hidden files (.DS_Store, .git, etc.) and macOS resource forks.
        if any(part.startswith(".") for part in f.relative_to(src_dir).parts):
            skipped += 1
            continue
        rel = f.relative_to(src_dir)
        dst = dst_dir / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, dst)
        copied += 1
        try:
            total_bytes += f.stat().st_size
        except OSError:
            pass
    return {"copied": copied, "bytes": total_bytes, "skipped": skipped}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pages = load_pages()
    manifest = build_manifest(pages)
    search = build_search(pages)
    bl = backlinks(pages)

    # attach backlinks to each page
    for p in pages:
        p["backlinks"] = bl.get(p["id"], [])

    case_order = [p["id"] for p in sorted(
        (q for q in pages if q["kind"] == "case"), key=_case_sort_key
    )]
    featured_case_id = pick_featured_case(pages)

    meta = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "counts": {
            "case":    sum(1 for p in pages if p["kind"] == "case"),
            "topic":   sum(1 for p in pages if p["kind"] == "topic"),
            "lecture": sum(1 for p in pages if p["kind"] == "lecture"),
            "total":   len(pages),
        },
        "case_order":       case_order,
        "featured_case_id": featured_case_id,
    }

    (OUT / "pages.json").write_text(json.dumps({"pages": pages, "meta": meta}, ensure_ascii=False, default=_json_default))
    (OUT / "manifest.json").write_text(json.dumps({"pages": manifest, "meta": meta}, ensure_ascii=False, default=_json_default))
    (OUT / "search.json").write_text(json.dumps({"pages": search, "meta": meta}, ensure_ascii=False, default=_json_default))

    # Surface frontmatter parse failures so Lint can route them. The file
    # always exists (an empty errors list is informative: "the build saw
    # nothing wrong"); a non-empty list means at least one page silently
    # downgraded to fm={} during the build, which means downstream pages
    # rendered without their schema fields. Lint reads this file on its
    # next run and converts each entry into a `frontmatter-parse-failed`
    # pending issue carrying the path and the YAML excerpt.
    build_errors_payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "frontmatter_errors": getattr(load_pages, "errors", []) or [],
    }
    (OUT / "build_errors.json").write_text(
        json.dumps(build_errors_payload, ensure_ascii=False, default=_json_default, indent=2)
    )

    recent = build_recent(pages)
    (OUT / "recent.json").write_text(json.dumps(recent, ensure_ascii=False, default=_json_default))

    src_stats = copy_source_materials()

    print(f"[build] {meta['counts']}  wrote to {OUT}")
    if build_errors_payload["frontmatter_errors"]:
        print(f"[build] WARN: {len(build_errors_payload['frontmatter_errors'])} frontmatter parse error(s) recorded in build_errors.json")
    print(f"[build] recent: {len(recent['changelog'])} changelog entries, "
          f"{len(recent['ingestion']['processed'])} ingested, "
          f"{len(recent['ingestion']['unprocessed'])} pending, "
          f"{len(recent['ingestion']['broken_refs'])} broken refs, "
          f"{len(recent['pending_issues'])} open issues")
    print(f"[build] source materials: copied {src_stats['copied']} files "
          f"({src_stats['bytes'] / 1_000_000:.1f} MB) to {OUT / 'source'} "
          f"(skipped {src_stats['skipped']} hidden)")


if __name__ == "__main__":
    main()
