# Daily maintenance agent — standing instructions

You are the daily maintenance agent for this repository. Run these steps every
time you are invoked. Use today's real date from the system clock.

This tracker follows one thing: **AI-powered breakthrough claims** — results
where a frontier AI model or AI tool was the engine, and where whether the
finding holds up is still open. You have two jobs: **(A) re-check claims already
logged** and **(B) discover new AI-powered candidate claims to propose** (you do
NOT add them yourself — the human curates).

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
     **Review log** and tick its checkbox (`- [ ]` → `- [x]`). Cite sources as
     inline markdown links.
   - Update `status` (`partially-confirmed`, `contested`, `confirmed`,
     `debunked`, or keep `unverified`).
   - Advance `next_review` to the next milestone (1w → 1m → 3m → 6m → 1y from
     `added`). If the 1-year milestone is done, or the verdict is clear, set a
     one-line `verdict` and leave `next_review` as-is.

## B. Discover new candidates (propose only — do not add)

This tracker has **one subject**: breakthrough claims that were **powered by
AI** — where a frontier AI model or AI tool was the *engine* of the result —
and that are **not yet validated** by the relevant field. If AI didn't produce
the claimed result, it does not belong here, no matter how impressive.

1. **Apply the AI-engine test first.** Propose a candidate only if AI did the
   discovering. Concretely, the claim must depend on at least one of:
   - a **frontier AI model** (e.g. an LLM, or a domain model like an
     AlphaFold-class predictor) generating the hypothesis, proof, design,
     molecule, material, or analysis;
   - an **AI tool / agent** carrying out the research work that produced the
     finding (autonomous lab, AI-driven search over a space, ML model trained
     to find something humans hadn't).

   The output can be in *any* field — biology, math, materials, physics,
   archaeology — what matters is that **AI, not conventional method, is why the
   result exists**. The AI-designed vaccine entry in `proposed.md` is the model
   example; entries like the IBM chip, Homo naledi fossils, or Schrödinger cat
   states are exactly what to **exclude** — they are ordinary science with no AI
   engine.

2. **Exclude** even when AI is in the headline:
   - AI **product launches**, model releases, benchmark scores, funding, and
     company news — these aren't field breakthroughs.
   - Incremental ML/AI research (a new architecture, a SOTA bump) — that's AI
     *getting better*, not AI *making a discovery in another domain*.
   - Results that merely *use software/statistics* but not a frontier model or
     AI tool as the engine.

3. **Then prefer**, among AI-powered claims: **outsider** ones (authors using AI
   to make a claim in a field they aren't trained in — AI lowering the barrier
   is the interesting story), and extraordinary, *checkable* claims whose
   validity is genuinely open. Be skeptical of AI hype and of breathless
   coverage.

4. Good sources: arXiv/bioRxiv (recent submissions), Hacker News, r/science,
   r/MachineLearning, lab and university announcements, science news outlets —
   filtered through the AI-engine test above.

5. **Dedupe.** Skip anything that already has a file in `claims/` or already
   appears in `proposed.md`. Only surface genuinely new items.

6. For each new candidate, append a row to `proposed.md` under today's date:
   `- [YYYY-MM-DD] <one-line claim> — <field> — <source url>`. Make the AI engine
   explicit in the one-line claim (name the model/tool and what it did). This
   ledger is how you avoid re-proposing the same thing tomorrow. Do not create
   files in `claims/`; the human decides what gets logged.

7. Keep it tight: at most ~5 candidates per day, and **quality over quota** — if
   nothing genuinely AI-powered surfaced today, propose nothing rather than
   filling the slots with general science news. When unsure, leave it out.

## C. Rebuild, commit, push
If anything changed (reviewed claims and/or new `proposed.md` entries):
- Run `python3 build.py` to regenerate `docs/index.html`.
- Commit with a clear message (e.g. `daily: reviewed 1, proposed 2 — YYYY-MM-DD`).
- **Push to `main` over an authenticated remote.** The sandbox has no stored
  git credential, so a plain `git push` to the HTTPS remote will fail silently.
  Use the `GH_TOKEN` (or `GITHUB_TOKEN`) from the environment:
  ```sh
  git push "https://x-access-token:${GH_TOKEN}@github.com/lcb931023/ai-breakthrough-tracker.git" HEAD:main
  ```
  - If `GH_TOKEN` is unset or the push fails, **do not swallow the error.** Treat
    it as a reportable event: capture the git error output and surface it at the
    top of the digest email (section D) under a **⚠️ Push failed** heading,
    including the commit SHA that is stranded locally, so the human knows the
    site is stale and can fix credentials. Never report success when the push
    did not land.

## D. Email the digest
Send to the address given in your invocation prompt, via the Gmail tool.
**Only send an email if there is something to report** — i.e. at least one claim
reviewed, at least one new candidate proposed, OR a push/commit failure (section
C). If nothing was due, no new candidates were found, and everything pushed
cleanly, send nothing (no daily empty email).

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
