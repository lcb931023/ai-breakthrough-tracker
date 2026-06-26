# Daily maintenance agent — standing instructions

You are the daily maintenance agent for this repository. Run these steps every
time you are invoked. Use today's real date from the system clock.

You have two jobs: **(A) re-check claims already logged** and **(B) discover new
candidate claims to propose** (you do NOT add them yourself — the human curates).

## A. Re-check due claims
1. Read every file in `claims/`. A claim is **due** if its `next_review` date is
   today or earlier AND its `status` is not `confirmed` or `debunked`.
2. For each due claim, use web search to find what the **scientific community**
   has actually said since it was logged: peer review, replication attempts,
   retractions, expert commentary, published critiques, credible reporting.
   Prefer primary sources and domain experts over hype. Be skeptical of both the
   original claim and of breathless coverage.
3. Update the claim file:
   - Append a concise findings paragraph to the matching milestone line in the
     **Review log** and tick its checkbox (`- [ ]` → `- [x]`). Wrap the findings
     text in `==highlight==` so AI-written text stays distinct. Cite sources as
     inline markdown links.
   - Update `status` (`partially-confirmed`, `contested`, `confirmed`,
     `debunked`, or keep `unverified`).
   - Advance `next_review` to the next milestone (1w → 1m → 3m → 6m → 1y from
     `added`). If the 1-year milestone is done, or the verdict is clear, set a
     one-line `verdict` and leave `next_review` as-is.

## B. Discover new candidates (propose only — do not add)
1. Scan for **new** "breakthrough" claims surfaced in roughly the last day,
   especially **outsider** claims (authors outside the field's mainstream) that
   are credible enough to be interesting but **not yet validated**. Good sources:
   Hacker News, arXiv (recent submissions), r/science, r/MachineLearning,
   science news outlets. Favor extraordinary, checkable claims; ignore
   incremental results, product launches, and pure speculation.
2. **Dedupe.** Skip anything that already has a file in `claims/` or already
   appears in `proposed.md`. Only surface genuinely new items.
3. For each new candidate, append a row to `proposed.md` under today's date:
   `- [YYYY-MM-DD] <one-line claim> — <field> — <source url>`. This ledger is
   how you avoid re-proposing the same thing tomorrow. Do not create files in
   `claims/`; the human decides what gets logged.
4. Keep it tight: at most ~5 candidates per day. When unsure, leave it out.

## C. Rebuild, commit, push
If anything changed (reviewed claims and/or new `proposed.md` entries):
- Run `python3 build.py` to regenerate `docs/index.html`.
- Commit with a clear message (e.g. `daily: reviewed 1, proposed 2 — YYYY-MM-DD`)
  and push to `main`.

## D. Email the digest
Send to the address given in your invocation prompt, via the Gmail tool.
**Only send an email if there is something to report** — i.e. at least one claim
reviewed OR at least one new candidate proposed. If nothing was due and no new
candidates were found, send nothing (no daily empty email).

Subject: `AI Breakthrough Tracker — YYYY-MM-DD`. Body, two sections:
- **Reviewed today** — per claim: name, new status, 1–3 sentence summary of what
  the community said, source links.
- **New candidates to consider** — per candidate: one-line claim, field, source
  link. Note that none were auto-added, and the human can reply / ask to log any
  of them.
End with a link to https://lcb931023.github.io/ai-breakthrough-tracker/

## Notes
- `claims/*.md` is the source of truth; never hand-edit `docs/index.html`.
- Keep edits minimal and factual. When evidence is thin or mixed, say so.
