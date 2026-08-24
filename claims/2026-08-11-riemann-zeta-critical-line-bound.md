---
claim: Jarred Sumner, a non-mathematician at Anthropic, raised the known lower bound on Riemann zeta zeros that are simple and on the critical line from 41.6% to 67.2% with an unreleased research build of Claude
source: https://www.anthropic.com/research/riemann-zeta
field: Mathematics / analytic number theory
outsider: false
added: 2026-08-11
status: partially-confirmed
next_review: 2026-09-11
verdict:
---
## The claim
Anthropic reports that an **unreleased research version of Claude**, prompted
by **Jarred Sumner** (an Anthropic staff member who is **not a
mathematician**), generated the proof strategy behind a new unconditional
result in analytic number theory: raising the known lower bound on the
proportion of nontrivial Riemann zeta zeros that are **simple and lie on the
critical line** from the prior **41.6%** (a figure built up incrementally by
Baluyot, Goldston, Suriajaya, and Turnage-Butterbaugh) to **67.2%**.

Specifics:
- Claude ran across **two sessions inside Claude Code**, coordinating roughly
  **60 subagents**, producing **~31 million output tokens**, and executing
  **~2,400 shell commands** plus hundreds of Python scripts.
- Anthropic says the model tried and discarded **~650 failed proof ideas**
  before landing on the successful approach: treating on- and
  off-critical-line zeros as a unified geometric space via Weil's explicit formula,
  Hermitian quadratic forms, Sylvester's law of inertia, and a new
  rank-trace inequality.
- Anthropic mathematicians **Levent Alpöge** and **Ralph Furman** validated
  the result afterward and formalized parts of it in Lean; external
  mathematicians **Brian Conrey** and **Dan Goldston** were also involved in
  review.
- Anthropic is explicit that **it does not expect this technique to lead to
  a full proof of the Riemann Hypothesis** — this is progress on a related,
  narrower quantitative question, not a resolution of the conjecture itself.

Reported via [Anthropic's official research
post](https://www.anthropic.com/research/riemann-zeta), published 10 August
2026; also covered by
[kingy.ai](https://kingy.ai/blog/claude-riemann-hypothesis-67-percent-result/)
and
[xenospectrum.com](https://xenospectrum.com/en/claude-riemann-zeta-critical-line-lower-bound/).

## Why it needs watching
- **Single-vendor self-report** — Anthropic reporting on its own unreleased
  model, on its own research blog. The AI-engine test passes cleanly (Claude
  generated the proof strategy, not just assisted with writeup), but there
  is no independent party confirming the framing or the significance yet.
- **Model unreleased and unidentified** — no external party can reproduce
  the process even in principle until (if ever) this research build is
  released or its exact configuration is disclosed.
- **No peer review yet.** The result touches a famous, heavily-scrutinized
  area (Riemann zeta zero-density estimates), so specialists in analytic
  number theory should weigh in relatively quickly if there's a flaw or if
  the bound doesn't actually improve on the state of the art once checked
  against the full literature (some outside commentary already flagged that
  the method appears to plateau around ~68%, which is worth verifying).
- Track: does a specialist outside Anthropic (e.g. authors of the papers the
  67.2% bound builds on — Baluyot, Goldston, Suriajaya, Turnage-Butterbaugh)
  comment on or verify the claimed improvement? Does Anthropic release the
  Lean formalization or full proof for independent scrutiny? Does any
  math-community venue (e.g. MathOverflow, a number theory seminar) surface
  a gap?

## Review log
- [x] **+1 week** (2026-08-18) — Anthropic has since published the full
  manuscript, a shorter explanatory note, a large provenance appendix,
  process transcripts, and a public Lean 4 formalization repo
  ([anthropics/zeta-23-lean](https://github.com/anthropics/zeta-23-lean)),
  which passes automated proof-checking — meaning the logical chain no
  longer has to be taken on Anthropic's word. External number theorists
  **Brian Conrey** and **Dan Goldston** reviewed the paper on short notice
  and their reaction has been reported as positive; notably Goldston is
  also a co-author of the Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh
  work the 67.2% bound builds on, so his review carries direct domain
  authority even though it isn't full journal peer review. No credible
  flaw, gap, or retraction has surfaced in the week since publication —
  coverage from [Forbes](https://www.forbes.com/sites/jonmarkman/2026/08/13/claude-just-broke-a-math-record-that-stood-for-37-years/),
  [TechSpot](https://www.techspot.com/news/113472-anthropic-claude-tried-solve-riemann-hypothesis-found-something.html),
  and [xenospectrum](https://xenospectrum.com/en/claude-riemann-zeta-critical-line-lower-bound/)
  is largely favorable, and one commentator called it possibly the biggest
  analytic-number-theory result since the 2013 bounded-gaps-between-primes
  work. Caveats remain real: the underlying model is still unreleased and
  unidentified (so the *process* can't be independently reproduced, only
  the *output* checked), and there's been no formal journal peer review —
  upgrading to `partially-confirmed` reflects the public, checkable proof
  plus credible outside math review, short of full field consensus.
- [ ] **+1 month** (2026-09-11) —
- [ ] **+3 months** (2026-11-11) —
- [ ] **+6 months** (2027-02-11) —
- [ ] **+1 year** (2027-08-11) —
