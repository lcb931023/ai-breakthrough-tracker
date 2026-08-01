---
claim: Grok 4.5, running as the autonomous "Capy" agent, found a counterexample refuting Graffiti Conjecture 284
source: https://x.com/justinsunyt/status/2080116559352316409
field: Mathematics / graph theory (spectral graph theory)
outsider: true
added: 2026-07-25
status: partially-confirmed
next_review: 2026-08-25
verdict:
---
## The claim
Capy is a YC-backed autonomous AI-software-engineering agent (cofounded by Nalin
Semwal and Justin Sun) built to triage issues and ship code changes on its own.
On 23 July 2026, during an internal Slack discussion unrelated to its usual
job, someone shared **Graffiti Conjecture 284** — one of many conjectures
mechanically generated in the 1980s–90s by Siemion Fajtlowicz's automated
"Graffiti" program, open for roughly 30 years. It states that in any connected
graph with girth ≥ 5, the minimum **dual degree** (average degree of a
vertex's neighbors) is bounded above by minus the smallest eigenvalue of the
graph's distance matrix.

Specifics:
- Capy, running on **Grok 4.5 Medium**, was not assigned the problem — it
  decided on its own to take a shot at it, and produced a counterexample in
  about **8 minutes**.
- The counterexample is the well-known **Hoffman–Singleton graph** (50
  vertices, 7-regular, girth 5, diameter 2), which violates the conjectured
  inequality.
- Per Capy co-founder Justin Sun's account, the agent internally spawned
  adversarial review tasks using other models (referred to as "Sol" and
  "Fable") to try to break its own counterexample; both reportedly confirmed
  the Hoffman–Singleton graph does violate the bound.
- Elon Musk amplified the claim on X: "Grok 4.5 just solved a graph theory
  conjecture that has been open for ~30 years."
- No named spectral-graph-theory specialist has publicly reviewed or
  confirmed the counterexample as of writing.

Reported via [Justin Sun's X thread](https://x.com/justinsunyt/status/2080116559352316409),
amplified by [Elon Musk](https://x.com/elonmusk/status/2080165738464280725),
and covered by [Windows News AI](https://windowsnews.ai/article/ai-generated-counterexample-could-overturn-30-year-graph-theory-conjectureif-it-holds-up.440161),
July 2026.

## Why it needs watching
- **Strong outsider signal on two levels.** The human, Justin Sun, is a
  software/startup founder (Capy, YC-backed), not a professional
  mathematician. And the discovery wasn't a directed research task — the
  agent chose to attempt an open problem on its own initiative during an
  unrelated Slack conversation.
- **Verification so far is AI-on-AI.** The "adversarial review" that checked
  the counterexample was other AI models, not an independent human graph
  theorist — a materially lower bar than expert peer review.
- **Graffiti conjectures have a mixed, decades-long track record** — several
  papers over the years have specifically hunted for and found
  counterexamples to Graffiti's automatically-generated conjectures (e.g.
  "A computational attack on the conjectures of Graffiti"). Worth checking
  whether Conjecture 284 specifically was already known to be resolved,
  refuted, or narrowed in the prior literature before crediting this as a
  first refutation.
- Track: does a credentialed spectral/algebraic graph theorist confirm the
  Hoffman–Singleton graph actually violates the inequality as Conjecture 284
  states it (vs. a misreading of the conjecture's exact hypotheses)? Does
  any prior paper already cover this case?

## Review log
- [x] **+1 week** (2026-08-01) — The significant development is an independent, human-authored preprint: [Samuil Petkov (ENS Paris), "Counterexamples, Spectral Obstructions, and Deletion Stability for WOW-284," arXiv:2607.27452](https://arxiv.org/abs/2607.27452) (29 July 2026), which derives counterexamples to Graffiti/WOW-284 at orders 38, 39, 40, 42, and 50, confirms the Hoffman–Singleton graph is a genuine violation (dual-degree gap of 3), and backs the arithmetic with Lean 4 kernel-checked proofs. It never mentions Capy or Grok, suggesting parallel human verification rather than reliance on the AI transcript. Checking the classic exhaustive-search paper, [Brewster, Dinneen & Faber, "A computational attack on the conjectures of Graffiti" (1995)](https://www.cs.auckland.ac.nz/~mjd/graffiti/graffiti1.pdf), it only tested graphs of ≤10 vertices, so the 50-vertex Hoffman–Singleton counterexample was genuinely new, not previously known. No named senior spectral/algebraic graph theorist has publicly commented by name, and no retraction has appeared from Capy/Justin Sun/Nalin Semwal. Coverage of this claim is frequently conflated in outlets with an unrelated same-week wave of "AI refutes old Graffiti conjecture" stories, a sign reporting is derivative rather than independently fact-checked. Status moved to partially-confirmed: mathematically corroborated by an independent, formally-verified (Lean) human preprint, but still only a preprint with no peer review or named-authority endorsement.
- [ ] **+1 month** (2026-08-25) —
- [ ] **+3 months** (2026-10-25) —
- [ ] **+6 months** (2027-01-25) —
- [ ] **+1 year** (2027-07-25) —
