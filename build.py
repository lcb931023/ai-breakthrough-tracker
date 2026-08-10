#!/usr/bin/env python3
"""Render claims/*.md into docs/index.html for GitHub Pages.

Source of truth is the markdown files in claims/. Each has YAML-ish flat
frontmatter (claim, source, field, outsider, added, status, next_review,
verdict) and a markdown body holding the review log. No third-party deps.
"""
import html
import json
import re
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent
CLAIMS_DIR = ROOT / "claims"
OUT = ROOT / "docs" / "index.html"

STATUS_ORDER = ["unverified", "contested", "partially-confirmed", "confirmed", "debunked"]

# Display buckets for the verification-progress bar, in progression order.
# Mutually exclusive, so the counts always sum to the number of claims.
BUCKETS = [
    ("unverified", "unverified"),
    ("stale", "went stale"),
    ("contested", "contested"),
    ("partially-confirmed", "partially confirmed"),
    ("confirmed", "confirmed"),
    ("debunked", "refuted"),
]

# `field` is freeform prose, so the filter chip is its head (text before the
# first "/" or "("). This table folds related heads together; anything not
# listed falls through unchanged, so new fields bucket themselves.
DISCIPLINE_MERGE = {
    "Mathematical physics": "Physics",
    "Statistical physics": "Physics",
}


def discipline(field):
    """Collapse a freeform `field` string into a single filter chip label."""
    head = re.split(r"[/(]", field or "")[0].strip()
    return DISCIPLINE_MERGE.get(head, head) or "Other"


def bucket(status, ticks):
    """Which progress bucket a claim falls in.

    A claim that has been reviewed twice and still hasn't moved off
    `unverified` has gone stale — we looked, and nobody serious engaged.
    Stale wins over the raw status so the buckets stay exclusive.
    """
    if status == "unverified" and sum(1 for _, s, _ in ticks if s == "done") >= 2:
        return "stale"
    return status if any(status == b for b, _ in BUCKETS) else "unverified"


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


def card(meta, body, ticks, buck):
    status = meta.get("status", "unverified")
    settled = status in ("confirmed", "debunked")
    nr = meta.get("next_review", "")
    du = days_until(nr)
    overdue = du is not None and du <= 0 and not settled
    is_out = str(meta.get("outsider", "")).lower() == "true"
    outsider = "outsider" if is_out else "insider"
    src = html.escape(meta["source"]) if meta.get("source") else ""
    src_html = f' <a href="{src}">source →</a>' if src else ""
    verdict_html = (f'<p class="verdict"><span class="stamp-label">Verdict</span> '
                    f'{html.escape(meta["verdict"])}</p>') if meta.get("verdict") else ""
    flag_html = '<span class="flag">review due</span>' if overdue else ""
    # Mirror the bar's stale call on the card, so the two never disagree.
    stale_html = '<span class="flag stale">went stale</span>' if buck == "stale" else ""
    return f"""<article class="entry {'overdue' if overdue else ''}"
  data-discipline="{html.escape(discipline(meta.get('field', '')))}"
  data-outsider="{'true' if is_out else 'false'}" data-bucket="{buck}">
  <header>
    <span class="stamp s-{status}">{html.escape(status)}</span>
    <span class="tag">{html.escape(meta.get('field','—'))}</span>
    <span class="tag {outsider}">{outsider}</span>
    {flag_html}{stale_html}
  </header>
  <h2>{html.escape(meta.get('claim','(untitled)'))}</h2>
  <p class="meta">filed {html.escape(meta.get('added','?'))}{src_html}</p>
  {ticker_html(ticks)}
  {verdict_html}
  <details><summary>Full review log</summary>{md_to_html(body)}</details>
</article>"""


def progress_html(counts, total, due_n):
    """The verification-progress bar. Display only — filtering lives below.

    Rendered server-side so the page is correct with JavaScript disabled; the
    script re-renders this same markup as filters narrow the set.
    """
    segs, legend = [], []
    for key, label in BUCKETS:
        n = counts.get(key, 0)
        if n:
            segs.append(f'<span class="seg b-{key}" style="width:{n / total * 100:.4f}%"'
                        f' title="{n} {label}"></span>')
        legend.append(f'<li class="lg b-{key}{"" if n else " zero"}">'
                      f"<b>{n}</b><span>{label}</span></li>")
    due = f'<p class="due-note">{due_n} review{"" if due_n == 1 else "s"} due</p>' if due_n else ""
    return f"""<section class="progress">
  <div class="progress-head">
    <span class="eyebrow">Verification progress</span>
    <span class="pcount" id="pcount">{total} claim{"" if total == 1 else "s"}</span>
  </div>
  <div class="bar" id="bar">{"".join(segs)}</div>
  <ul class="legend" id="legend">{"".join(legend)}</ul>
  {due}
</section>"""


def filters_html(claims_meta, total):
    """Filter controls. Carries `hidden` so a no-JS page never shows dead UI."""
    counts = {}
    for m in claims_meta:
        d = discipline(m.get("field", ""))
        counts[d] = counts.get(d, 0) + 1
    # Biggest discipline first, ties broken alphabetically.
    chips = [f'<button type="button" class="chip on" data-d="all" aria-pressed="true">'
             f"All <b>{total}</b></button>"]
    for d, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        chips.append(f'<button type="button" class="chip" data-d="{html.escape(d)}"'
                     f' aria-pressed="false">{html.escape(d)} <b>{n}</b></button>')
    opts = "".join(f'<option value="{k}">{l}</option>' for k, l in BUCKETS)
    return f"""<div class="filters" id="filters" hidden>
  <div class="chips" role="group" aria-label="Filter by discipline">{"".join(chips)}</div>
  <div class="frow">
    <button type="button" class="chip toggle" id="outsider" aria-pressed="false">outsider only</button>
    <label class="sel" for="status">status
      <select id="status"><option value="all">any</option>{opts}</select>
    </label>
    <button type="button" class="chip reset" id="reset" hidden>reset</button>
  </div>
</div>
<p class="empty" id="empty" hidden>No claims match these filters.</p>"""


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

    counts, cards = {}, []
    for meta, body in claims:
        status = meta.get("status", "unverified")
        ticks = milestone_ticks(body, status in ("confirmed", "debunked"))
        buck = bucket(status, ticks)
        counts[buck] = counts.get(buck, 0) + 1
        cards.append(card(meta, body, ticks, buck))

    total = len(claims)
    OUT.write_text(PAGE.format(
        progress=progress_html(counts, total, due_n) if total else "",
        filters=filters_html([m for m, _ in claims], total) if total else "",
        cards="\n".join(cards) or "<p>No claims logged yet.</p>",
        built=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        script=SCRIPT,
    ))
    stale_n = counts.get("stale", 0)
    print(f"Built {OUT} — {total} claims, {open_n} open, {due_n} due, {stale_n} stale.")


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
[hidden] {{ display:none !important; }}

.progress {{ margin:0 0 1.3rem; padding:.9rem 0 1rem; border-top:1px solid var(--ink);
             border-bottom:1px solid var(--line-strong); }}
.progress-head {{ display:flex; justify-content:space-between; align-items:baseline; gap:1rem; }}
.pcount {{ font-family:var(--mono); font-size:.72rem; color:var(--mut); font-variant-numeric:tabular-nums; }}
.bar {{ display:flex; height:.6rem; margin:.7rem 0 .85rem; background:var(--line);
        border-radius:2px; overflow:hidden; }}
.seg {{ display:block; min-width:3px; background:var(--c); }}
.legend {{ list-style:none; display:flex; flex-wrap:wrap; gap:.3rem 1.15rem; margin:0; padding:0; }}
.lg {{ display:flex; align-items:center; gap:.4rem; font-family:var(--mono); font-size:.72rem; color:var(--mut); }}
.lg::before {{ content:""; width:.55rem; height:.55rem; border-radius:2px; background:var(--c); flex:none; }}
.lg b {{ font-size:1.05rem; font-weight:600; font-variant-numeric:tabular-nums; color:var(--ink); }}
.lg.zero {{ opacity:.4; }}
.lg.zero b {{ color:var(--mut); }}
.due-note {{ margin:.85rem 0 0; font-family:var(--mono); font-size:.7rem; color:var(--flag);
             font-weight:700; letter-spacing:.03em; text-transform:uppercase; }}
.due-note::before {{ content:"▸ "; }}

.b-unverified {{ --c:var(--gray); }}
.b-contested {{ --c:var(--amber); }}
.b-partially-confirmed {{ --c:var(--teal); }}
.b-confirmed {{ --c:var(--green); }}
.b-debunked {{ --c:var(--flag); }}
/* Stale should read as absence of attention, not as a verdict — hatched, not solid. */
.b-stale {{ --c:var(--mut); }}
.seg.b-stale, .lg.b-stale::before {{
  background:repeating-linear-gradient(45deg,var(--mut) 0 2px,transparent 2px 5px);
  box-shadow:inset 0 0 0 1px var(--line-strong); }}

.filters {{ display:flex; flex-direction:column; gap:.55rem; margin:0 0 2rem; }}
.chips,.frow {{ display:flex; flex-wrap:wrap; gap:.4rem; align-items:center; }}
.chip {{ font-family:var(--mono); font-size:.7rem; letter-spacing:.03em; text-transform:uppercase;
         color:var(--mut); background:transparent; border:1px solid var(--line-strong);
         border-radius:3px; padding:.25rem .55rem; cursor:pointer; }}
.chip b {{ font-weight:600; font-variant-numeric:tabular-nums; opacity:.6; }}
.chip:hover {{ border-color:var(--ink); color:var(--ink); }}
.chip.on {{ background:var(--ink); border-color:var(--ink); color:var(--bg); }}
.chip.toggle::before {{ content:"◆ "; }}
.chip.toggle.on {{ background:var(--flag); border-color:var(--flag); color:var(--bg); }}
.chip.reset {{ border-style:dashed; }}
.sel {{ display:flex; align-items:center; gap:.35rem; font-family:var(--mono); font-size:.7rem;
        letter-spacing:.03em; text-transform:uppercase; color:var(--mut); }}
.sel select {{ font:inherit; text-transform:none; color:var(--ink); background:transparent;
               border:1px solid var(--line-strong); border-radius:3px; padding:.22rem .3rem; }}
.chip:focus-visible, .sel select:focus-visible {{ outline:2px solid var(--teal); outline-offset:2px; }}
.empty {{ color:var(--mut); font-family:var(--mono); font-size:.85rem; padding:2rem 0;
          border-top:1px solid var(--ink); }}

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
.flag.stale {{ color:var(--mut); }}
.flag.stale::before {{ content:"~ "; }}

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
{progress}
{filters}
{cards}
<footer>Last built {built} · source of truth: <code>claims/*.md</code> · regenerated by <code>build.py</code></footer>
{script}
</body></html>"""

# Passed into PAGE.format() as a *value*, never as part of the template, so its
# braces don't need doubling. Bucket labels are injected from BUCKETS so the
# client-side list can't drift from the Python one.
SCRIPT = """<script>
(function () {
  var BUCKETS = __BUCKETS__;
  var cards = [].slice.call(document.querySelectorAll('.entry'));
  var filters = document.getElementById('filters');
  if (!cards.length || !filters) return;
  var bar = document.getElementById('bar');
  var legend = document.getElementById('legend');
  var pcount = document.getElementById('pcount');
  var empty = document.getElementById('empty');
  var reset = document.getElementById('reset');
  var outsider = document.getElementById('outsider');
  var statusSel = document.getElementById('status');
  var chips = [].slice.call(filters.querySelectorAll('.chip[data-d]'));
  var TOTAL = cards.length;
  var state = { d: 'all', outsider: false, status: 'all' };

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  function matches(c) {
    if (state.d !== 'all' && c.getAttribute('data-discipline') !== state.d) return false;
    if (state.outsider && c.getAttribute('data-outsider') !== 'true') return false;
    if (state.status !== 'all' && c.getAttribute('data-bucket') !== state.status) return false;
    return true;
  }

  function render() {
    var counts = {}, n = 0;
    cards.forEach(function (c) {
      var ok = matches(c);
      c.hidden = !ok;
      if (ok) {
        n++;
        var b = c.getAttribute('data-bucket');
        counts[b] = (counts[b] || 0) + 1;
      }
    });
    bar.innerHTML = BUCKETS.map(function (b) {
      var v = counts[b[0]] || 0;
      if (!v) return '';
      return '<span class="seg b-' + b[0] + '" style="width:' + (v / n * 100).toFixed(4) +
             '%" title="' + v + ' ' + esc(b[1]) + '"></span>';
    }).join('');
    legend.innerHTML = BUCKETS.map(function (b) {
      var v = counts[b[0]] || 0;
      return '<li class="lg b-' + b[0] + (v ? '' : ' zero') + '"><b>' + v + '</b><span>' +
             esc(b[1]) + '</span></li>';
    }).join('');
    pcount.textContent = n === TOTAL ? TOTAL + ' claim' + (TOTAL === 1 ? '' : 's')
                                     : n + ' of ' + TOTAL + ' claims';
    bar.hidden = n === 0;
    empty.hidden = n > 0;
    reset.hidden = state.d === 'all' && !state.outsider && state.status === 'all';
  }

  function press(el, on) {
    el.classList.toggle('on', on);
    el.setAttribute('aria-pressed', on ? 'true' : 'false');
  }

  chips.forEach(function (chip) {
    chip.addEventListener('click', function () {
      state.d = chip.getAttribute('data-d');
      chips.forEach(function (o) { press(o, o === chip); });
      render();
    });
  });

  outsider.addEventListener('click', function () {
    state.outsider = !state.outsider;
    press(outsider, state.outsider);
    render();
  });

  statusSel.addEventListener('change', function () {
    state.status = statusSel.value;
    render();
  });

  reset.addEventListener('click', function () {
    state = { d: 'all', outsider: false, status: 'all' };
    chips.forEach(function (o) { press(o, o.getAttribute('data-d') === 'all'); });
    press(outsider, false);
    statusSel.value = 'all';
    render();
  });

  filters.hidden = false;
  render();
})();
</script>""".replace("__BUCKETS__", json.dumps(BUCKETS))


if __name__ == "__main__":
    main()
