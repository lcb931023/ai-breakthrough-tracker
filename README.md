# AI Breakthrough Tracker

A watchlist for **AI-powered** "breakthrough" claims — results where a frontier
AI model or AI tool was the *engine* of the discovery (often made by
**outsiders** to a field, since AI lowers the barrier to entry), and where
whether the finding actually *holds up* is the open question. Each claim is
logged when it surfaces, then re-checked against what the scientific community
says at fixed intervals: **1 week, 1 month, 3 months, 6 months, 1 year**.

A daily cloud agent (Claude Code routine) does two things: re-checks any claims
that are due (researching current consensus, updating the files, rebuilding the
site) and scans for new candidate claims to **propose** for logging. It emails a
digest only on days there's something to report. New claims are curated by a
human — the agent proposes, it does not auto-add.

## Layout
- `claims/*.md` — **source of truth**, one file per claim (YAML frontmatter + review log).
- `build.py` — renders `claims/` into `docs/index.html`. No dependencies.
- `docs/index.html` — the published site (GitHub Pages serves from `/docs`).
- `proposed.md` — ledger of candidates the agent surfaced but hasn't logged (dedupe + curation queue).
- `AGENT.md` — standing instructions for the daily cloud agent.
- `specs/` — design docs for changes to the tooling.

## The site
A verification-progress bar at the top breaks the docket into six mutually
exclusive buckets, and the list can be filtered by discipline, by outsider-only,
and by bucket. Filtering is progressive enhancement — with JavaScript off every
claim still renders.

Five buckets are just `status`. The sixth, **went stale**, is derived at build
time and stored nowhere:

> a claim has gone stale when **2 or more review milestones are ticked and its
> `status` is still `unverified`** — we looked repeatedly and nobody serious
> engaged.

Stale takes precedence over the raw status so the buckets always sum to the
claim total; `unverified` on the site therefore means "unverified and not yet
stale". Nothing to maintain by hand — it follows from the review log.

Discipline chips are derived too: the `field` string up to its first `/` or `(`,
passed through a small merge table in `build.py` (`DISCIPLINE_MERGE`) that folds
e.g. *Mathematical physics* and *Statistical physics* into **Physics**. A new
field buckets itself with no code change; edit the table only to merge two heads.

## Add a claim
Copy any file in `claims/`, rename it `YYYY-MM-DD-short-slug.md`, and fill the
frontmatter:

| key | meaning |
|-----|---------|
| `claim` | one-line description |
| `source` | link to paper / preprint / announcement |
| `field` | the discipline whose community will judge it |
| `outsider` | `true` if authors are outside that field's mainstream |
| `added` | ISO date logged |
| `status` | `unverified` → `partially-confirmed` / `confirmed` / `contested` / `debunked` |
| `next_review` | `added` + 1 week, then advanced each milestone |
| `verdict` | filled in once settled |

Then run `python3 build.py` (the agent does this automatically).
