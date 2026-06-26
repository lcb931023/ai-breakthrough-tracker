#!/usr/bin/env python3
"""Render claims/*.md into docs/index.html for GitHub Pages.

Source of truth is the markdown files in claims/. Each has YAML-ish flat
frontmatter (claim, source, field, outsider, added, status, next_review,
verdict) and a markdown body holding the review log. No third-party deps.
"""
import html
import re
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent
CLAIMS_DIR = ROOT / "claims"
OUT = ROOT / "docs" / "index.html"

STATUS_ORDER = ["unverified", "contested", "partially-confirmed", "confirmed", "debunked"]


def parse_claim(text):
    """Split a claim file into (frontmatter dict, body markdown)."""
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.DOTALL)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" not in line or line.lstrip().startswith("-"):
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip().strip("\"'")
    return meta, m.group(2).strip()


def md_to_html(md):
    """Minimal markdown: headings, checkboxes, quotes, lists, bold, links."""
    out, in_list = [], False
    for raw in md.splitlines():
        line = raw.rstrip()
        if not line:
            if in_list:
                out.append("</ul>"); in_list = False
            continue
        line = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', line)
        line = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", line)
        line = re.sub(r"==([^=]+)==", r"<mark>\1</mark>", line)
        if line.startswith("### "):
            tag = ("h4", line[4:])
        elif line.startswith("## "):
            tag = ("h3", line[3:])
        elif line.startswith("# "):
            tag = ("h2", line[2:])
        elif line.startswith("> "):
            tag = ("blockquote", line[2:])
        elif re.match(r"- \[[ xX]\] ", line):
            done = line[3] in "xX"
            box = "☑" if done else "☐"
            if not in_list:
                out.append("<ul class=log>"); in_list = True
            out.append(f"<li class={'done' if done else 'todo'}>{box} {line[6:]}</li>")
            continue
        elif line.startswith("- "):
            if not in_list:
                out.append("<ul>"); in_list = True
            out.append(f"<li>{line[2:]}</li>")
            continue
        else:
            tag = ("p", line)
        if in_list:
            out.append("</ul>"); in_list = False
        out.append(f"<{tag[0]}>{tag[1]}</{tag[0]}>")
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


def days_until(d):
    try:
        return (datetime.strptime(d, "%Y-%m-%d").date() - date.today()).days
    except (ValueError, TypeError):
        return None


def card(meta, body):
    status = meta.get("status", "unverified")
    nr = meta.get("next_review", "")
    du = days_until(nr)
    due = du is not None and du <= 0 and status not in ("confirmed", "debunked")
    when = "" if du is None else (f"in {du}d" if du > 0 else f"{-du}d overdue" if du < 0 else "today")
    outsider = "outsider" if str(meta.get("outsider", "")).lower() == "true" else "insider"
    due_badge = '<span class="tag duebadge">review due</span>' if due else ""
    when_html = f"<em>({when})</em>" if when else ""
    src = html.escape(meta["source"]) if meta.get("source") else ""
    src_html = f'· source: <a href="{src}">link</a>' if src else ""
    verdict_html = (f'<p class="verdict"><strong>Verdict:</strong> '
                    f'{html.escape(meta["verdict"])}</p>') if meta.get("verdict") else ""
    return f"""<article class="card {'due' if due else ''}">
  <header>
    <span class="badge s-{status}">{html.escape(status)}</span>
    <span class="tag">{html.escape(meta.get('field','—'))}</span>
    <span class="tag {outsider}">{outsider}</span>
    {due_badge}
  </header>
  <h2>{html.escape(meta.get('claim','(untitled)'))}</h2>
  <p class="meta">added {html.escape(meta.get('added','?'))} ·
     next review {html.escape(nr) or '—'} {when_html} {src_html}</p>
  {verdict_html}
  <details><summary>Review log</summary>{md_to_html(body)}</details>
</article>"""


def main():
    claims = []
    for f in sorted(CLAIMS_DIR.glob("*.md")):
        meta, body = parse_claim(f.read_text())
        if meta.get("claim"):
            claims.append((meta, body))
    # Soonest review first; settled claims sink to the bottom.
    claims.sort(key=lambda c: (
        c[0].get("status") in ("confirmed", "debunked"),
        c[0].get("next_review", "9999"),
    ))
    open_n = sum(1 for m, _ in claims if m.get("status") not in ("confirmed", "debunked"))
    due_n = sum(1 for m, _ in claims
                if (days_until(m.get("next_review", "")) or 1) <= 0
                and m.get("status") not in ("confirmed", "debunked"))
    cards = "\n".join(card(m, b) for m, b in claims)
    OUT.write_text(PAGE.format(
        cards=cards or "<p>No claims logged yet.</p>",
        total=len(claims), open_n=open_n, due_n=due_n,
        built=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    ))
    print(f"Built {OUT} — {len(claims)} claims, {open_n} open, {due_n} due.")


PAGE = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>AI Breakthrough Tracker</title>
<style>
:root {{ color-scheme: light dark; --bg:#fff; --fg:#1a1a1a; --mut:#666; --line:#e5e5e5; --card:#fafafa; }}
@media (prefers-color-scheme:dark){{ :root{{ --bg:#15171a; --fg:#e8e8e8; --mut:#9aa0a6; --line:#2a2d31; --card:#1c1f23; }} }}
* {{ box-sizing:border-box; }}
body {{ font:16px/1.6 system-ui,-apple-system,sans-serif; max-width:52rem; margin:0 auto; padding:2rem 1.2rem 4rem; background:var(--bg); color:var(--fg); }}
h1 {{ font-size:1.7rem; margin:0 0 .3rem; }}
.lede {{ color:var(--mut); margin:0 0 1.5rem; }}
.stats {{ display:flex; gap:1.5rem; margin:1.5rem 0; padding:1rem; border:1px solid var(--line); border-radius:.6rem; }}
.stats b {{ display:block; font-size:1.6rem; }}
.stats span {{ color:var(--mut); font-size:.85rem; }}
.card {{ border:1px solid var(--line); border-radius:.6rem; padding:1rem 1.2rem; margin:1rem 0; background:var(--card); }}
.card.due {{ border-color:#d97706; }}
.card h2 {{ font-size:1.15rem; margin:.4rem 0; }}
.card header {{ display:flex; gap:.5rem; flex-wrap:wrap; align-items:center; }}
.badge,.tag {{ font-size:.74rem; padding:.15rem .55rem; border-radius:1rem; font-weight:600; }}
.tag {{ background:transparent; border:1px solid var(--line); color:var(--mut); font-weight:500; }}
.tag.outsider {{ border-color:#a855f7; color:#a855f7; }}
.duebadge {{ border-color:#d97706; color:#d97706; }}
.badge {{ color:#fff; }}
.s-unverified{{background:#6b7280;}} .s-contested{{background:#d97706;}}
.s-partially-confirmed{{background:#0891b2;}} .s-confirmed{{background:#16a34a;}} .s-debunked{{background:#dc2626;}}
.meta {{ color:var(--mut); font-size:.85rem; margin:.3rem 0; }}
.verdict {{ font-size:.92rem; }}
details {{ margin-top:.6rem; }} summary {{ cursor:pointer; color:var(--mut); font-size:.9rem; }}
.log {{ list-style:none; padding-left:0; }} .log .done {{ color:var(--mut); }}
mark {{ background:#fde68a; color:#1a1a1a; padding:0 .15rem; }}
blockquote {{ border-left:3px solid var(--line); margin:.5rem 0; padding-left:.8rem; color:var(--mut); }}
footer {{ margin-top:3rem; color:var(--mut); font-size:.8rem; border-top:1px solid var(--line); padding-top:1rem; }}
a {{ color:#2563eb; }}
</style></head><body>
<h1>AI Breakthrough Tracker</h1>
<p class="lede">A watchlist for "breakthrough" claims — especially outsider claims — re-checked against
scientific consensus at 1 week, 1 month, 3 / 6 / 12 months. Auto-updated daily.</p>
<div class="stats">
  <div><b>{total}</b><span>tracked</span></div>
  <div><b>{open_n}</b><span>still open</span></div>
  <div><b>{due_n}</b><span>review due</span></div>
</div>
{cards}
<footer>Last built {built} · source of truth: <code>claims/*.md</code> · regenerated by <code>build.py</code></footer>
</body></html>"""


if __name__ == "__main__":
    main()
