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
    """Minimal markdown: headings, checkboxes, quotes, lists, bold, links.

    Source files are hard-wrapped at ~80 cols for readable diffs, so
    soft-wrapped continuation lines are merged back into their block —
    only a blank line or a new block marker starts a new paragraph/item.
    """
    blocks = []  # [type, text], type one of h2/h3/h4/p/quote/li/li-done/li-todo
    open_block = None  # index of the block that can still absorb continuation lines
    for raw in md.splitlines():
        line = raw.strip()
        if not line:
            open_block = None
            continue
        line = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', line)
        line = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", line)
        if line.startswith("### "):
            blocks.append(["h4", line[4:]]); open_block = None
        elif line.startswith("## "):
            blocks.append(["h3", line[3:]]); open_block = None
        elif line.startswith("# "):
            blocks.append(["h2", line[2:]]); open_block = None
        elif line.startswith("> "):
            blocks.append(["quote", line[2:]]); open_block = len(blocks) - 1
        elif re.match(r"- \[[ xX]\] ", line):
            blocks.append(["li-done" if line[3] in "xX" else "li-todo", line[6:]])
            open_block = len(blocks) - 1
        elif line.startswith("- "):
            blocks.append(["li", line[2:]]); open_block = len(blocks) - 1
        elif open_block is not None:
            blocks[open_block][1] += " " + line
        else:
            blocks.append(["p", line]); open_block = len(blocks) - 1

    out, in_ul = [], None
    for typ, text in blocks:
        if typ in ("li", "li-done", "li-todo"):
            want = "plain" if typ == "li" else "log"
            if in_ul != want:
                if in_ul:
                    out.append("</ul>")
                out.append("<ul class=log>" if want == "log" else "<ul>")
                in_ul = want
            if typ == "li":
                out.append(f"<li>{text}</li>")
            else:
                box = "☑" if typ == "li-done" else "☐"
                out.append(f"<li class={'done' if typ == 'li-done' else 'todo'}>{box} {text}</li>")
            continue
        if in_ul:
            out.append("</ul>"); in_ul = None
        out.append(f"<{typ}>{text}</{typ}>")
    if in_ul:
        out.append("</ul>")
    return "\n".join(out)


def days_until(d):
    try:
        return (datetime.strptime(d, "%Y-%m-%d").date() - date.today()).days
    except (ValueError, TypeError):
        return None


MILESTONES = [("1 week", "1w"), ("1 month", "1mo"), ("3 months", "3mo"),
              ("6 months", "6mo"), ("1 year", "1y")]


def milestone_ticks(body, settled):
    """Read the review-log checkboxes to derive each milestone's state
    (done / overdue / upcoming) for the verification-timeline ticker."""
    logged = {}
    for m in re.finditer(r"\[([ xX])\]\s*\*\*\+(1 week|1 month|3 months|6 months|1 year)\*\*\s*\(([\d-]+)\)", body):
        logged[m.group(2)] = (m.group(1).lower() == "x", m.group(3))
    ticks = []
    for label, short in MILESTONES:
        done, d = logged.get(label, (False, ""))
        if done:
            state = "done"
        elif settled:
            state = "closed"
        else:
            dd = days_until(d) if d else None
            state = "overdue" if (dd is not None and dd <= 0) else "future"
        ticks.append((short, state, d))
    return ticks


def ticker_html(ticks):
    dots = []
    for short, state, d in ticks:
        title = f' title="{html.escape(d)}"' if d else ""
        dots.append(f'<span class="tick {state}"{title}><i class="dot"></i>{short}</span>')
    return f'<div class="ticker">{"".join(dots)}</div>'


def card(meta, body):
    status = meta.get("status", "unverified")
    settled = status in ("confirmed", "debunked")
    nr = meta.get("next_review", "")
    du = days_until(nr)
    overdue = du is not None and du <= 0 and not settled
    outsider = "outsider" if str(meta.get("outsider", "")).lower() == "true" else "insider"
    src = html.escape(meta["source"]) if meta.get("source") else ""
    src_html = f' <a href="{src}">source →</a>' if src else ""
    verdict_html = (f'<p class="verdict"><span class="stamp-label">Verdict</span> '
                    f'{html.escape(meta["verdict"])}</p>') if meta.get("verdict") else ""
    flag_html = '<span class="flag">review due</span>' if overdue else ""
    return f"""<article class="entry {'overdue' if overdue else ''}">
  <header>
    <span class="stamp s-{status}">{html.escape(status)}</span>
    <span class="tag">{html.escape(meta.get('field','—'))}</span>
    <span class="tag {outsider}">{outsider}</span>
    {flag_html}
  </header>
  <h2>{html.escape(meta.get('claim','(untitled)'))}</h2>
  <p class="meta">filed {html.escape(meta.get('added','?'))}{src_html}</p>
  {ticker_html(milestone_ticks(body, settled))}
  {verdict_html}
  <details><summary>Full review log</summary>{md_to_html(body)}</details>
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
:root {{
  color-scheme: light dark;
  --bg:#eef2ea; --ink:#1f2a22; --mut:#5c6b5f; --line:#c9d4c3; --line-strong:#a9b8a4;
  --flag:#b3402a; --amber:#a5680f; --teal:#0f766e; --green:#2f7d4f; --gray:#6b7280;
  --serif: "Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;
  --sans: -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  --mono: ui-monospace,"SF Mono",Menlo,Consolas,monospace;
}}
@media (prefers-color-scheme:dark){{
  :root{{ --bg:#141a13; --ink:#dfe6d6; --mut:#8b9a86; --line:#2b352a; --line-strong:#3b4a38;
          --flag:#e2734f; --amber:#d99a3d; --teal:#2dd4c7; --green:#5fbf82; --gray:#98a29a; }}
}}
* {{ box-sizing:border-box; }}
body {{ font:16px/1.6 var(--sans); max-width:44rem; margin:0 auto; padding:3rem 1.2rem 4rem;
        background:var(--bg); color:var(--ink); }}
.eyebrow {{ font:.72rem/1 var(--mono); letter-spacing:.12em; text-transform:uppercase; color:var(--mut); }}
h1 {{ font-family:var(--serif); font-weight:600; font-size:2.1rem; margin:.35rem 0 .6rem; }}
.lede {{ color:var(--mut); margin:0 0 1.6rem; max-width:38rem; }}
.stats {{ display:flex; gap:2rem; margin:0 0 2.2rem; padding:.8rem 0; border-top:1px solid var(--ink);
          border-bottom:1px solid var(--line-strong); font-family:var(--mono); }}
.stats b {{ display:block; font-size:1.5rem; font-weight:600; font-variant-numeric:tabular-nums; }}
.stats span {{ color:var(--mut); font-size:.72rem; letter-spacing:.04em; text-transform:uppercase; }}

.entry {{ border-top:1px solid var(--line); padding:1.5rem 0; }}
.entry:first-of-type {{ border-top:1px solid var(--ink); }}
.entry.overdue {{ border-left:3px solid var(--flag); padding-left:1rem; margin-left:-1rem; }}
.entry header {{ display:flex; gap:.5rem; flex-wrap:wrap; align-items:center; }}
.entry h2 {{ font-family:var(--serif); font-weight:600; font-size:1.28rem; line-height:1.35; margin:.6rem 0 .3rem; }}

.stamp,.tag {{ font-family:var(--mono); font-size:.68rem; letter-spacing:.03em; text-transform:uppercase; }}
.stamp {{ border:1.5px solid; border-radius:3px; padding:.1rem .5rem; font-weight:700; transform:rotate(-1deg); display:inline-block; }}
.tag {{ color:var(--mut); }}
.tag.outsider {{ color:var(--flag); }}
.tag.outsider::before {{ content:"◆ "; }}
.tag.insider::before {{ content:"◇ "; }}
.s-unverified{{ color:var(--gray); border-color:var(--gray); }}
.s-contested{{ color:var(--amber); border-color:var(--amber); }}
.s-partially-confirmed{{ color:var(--teal); border-color:var(--teal); }}
.s-confirmed{{ color:var(--green); border-color:var(--green); }}
.s-debunked{{ color:var(--flag); border-color:var(--flag); }}
.flag {{ font-family:var(--mono); font-size:.68rem; letter-spacing:.03em; text-transform:uppercase;
         color:var(--flag); font-weight:700; }}
.flag::before {{ content:"▸ "; }}

.meta {{ color:var(--mut); font-size:.85rem; margin:.2rem 0; font-family:var(--mono); }}
.meta a {{ color:var(--mut); }}

.ticker {{ position:relative; display:flex; justify-content:space-between; margin:1rem 0 .4rem; padding-top:.7rem; max-width:22rem; }}
.ticker::before {{ content:""; position:absolute; top:.95rem; left:.3rem; right:.3rem; height:1px; background:var(--line-strong); }}
.tick {{ position:relative; z-index:1; display:flex; flex-direction:column; align-items:center; gap:.35rem;
         font-family:var(--mono); font-size:.66rem; color:var(--mut); }}
.tick .dot {{ width:.6rem; height:.6rem; border-radius:50%; background:var(--bg); border:1.5px solid var(--line-strong); display:block; }}
.tick.done .dot {{ background:var(--ink); border-color:var(--ink); }}
.tick.done {{ color:var(--ink); }}
.tick.overdue .dot {{ background:var(--flag); border-color:var(--flag); animation:pulse 2.2s ease-in-out infinite; }}
.tick.overdue {{ color:var(--flag); font-weight:700; }}
.tick.closed .dot {{ opacity:.3; }}
.tick.closed {{ opacity:.5; }}
@media (prefers-reduced-motion:reduce){{ .tick.overdue .dot {{ animation:none; }} }}
@keyframes pulse {{ 0%,100%{{ box-shadow:0 0 0 0 rgba(179,64,42,.35); }} 50%{{ box-shadow:0 0 0 4px rgba(179,64,42,0); }} }}

.verdict {{ font-size:.92rem; margin:.8rem 0 .2rem; padding:.5rem .7rem; border:1px solid var(--line-strong); border-radius:2px; }}
.stamp-label {{ font-family:var(--mono); font-size:.68rem; text-transform:uppercase; letter-spacing:.05em; color:var(--mut); }}

details {{ margin-top:.7rem; }}
summary {{ cursor:pointer; color:var(--mut); font-size:.82rem; font-family:var(--mono); }}
summary:focus-visible, a:focus-visible {{ outline:2px solid var(--teal); outline-offset:2px; }}
details[open] summary {{ margin-bottom:.6rem; }}
details :is(h2,h3,h4,p,li,blockquote) {{ font-family:var(--mono); font-size:.86rem; line-height:1.5; }}
details :is(p,li) {{ margin:.5em 0; }}
details ul {{ margin:.5em 0; padding-left:1.3em; }}
.log {{ list-style:none; padding-left:0; }} .log .done {{ color:var(--mut); }}
blockquote {{ border-left:3px solid var(--line-strong); margin:.5rem 0; padding-left:.8rem; color:var(--mut); }}

footer {{ margin-top:3rem; color:var(--mut); font-size:.78rem; font-family:var(--mono);
          border-top:1px solid var(--line); padding-top:1rem; }}
a {{ color:var(--teal); }}
</style></head><body>
<p class="eyebrow">Watchlist — claims pending verification</p>
<h1>AI Breakthrough Tracker</h1>
<p class="lede">"Breakthrough" claims where an AI model was the engine of discovery — often
made by outsiders to the field. Each is re-checked against scientific consensus at
1 week, 1 month, 3 / 6 / 12 months, and the docket updates automatically.</p>
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
