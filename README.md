# AI Breakthrough Tracker

A watchlist for "breakthrough" claims — especially ones made by **outsiders** to
a field, where whether the finding actually *holds up* is the open question.
Each claim is logged when it surfaces, then re-checked against what the
scientific community says at fixed intervals: **1 week, 1 month, 3 months,
6 months, 1 year**.

A weekly cloud agent (Claude Code routine) reviews any claims that are due,
researches the current consensus, updates the claim files, regenerates the
website, and emails a digest.

## Layout
- `claims/*.md` — **source of truth**, one file per claim (YAML frontmatter + review log).
- `build.py` — renders `claims/` into `docs/index.html`. No dependencies.
- `docs/index.html` — the published site (GitHub Pages serves from `/docs`).
- `AGENT.md` — standing instructions for the weekly cloud agent.

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
