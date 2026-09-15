---
claim: Justin Leder, an Anthropic data scientist with an economics degree and no math publications, directed an autonomous AI system that produced a Lean-verified proof that there is no percolation at the critical point on ℤ^d in every dimension d ≥ 2, with unnamed Anthropic Claude models
source: https://github.com/anthropics/formal-math/blob/795efb86f191735c5481675763537cfb4ff37e55/percolation/README.md
field: Mathematics / probability theory (percolation)
outsider: false
added: 2026-09-15
status: unverified
next_review: 2026-09-22
verdict:
---
## The claim
A pinned commit in Anthropic's `formal-math` repository claims an
unconditional, kernel-checked Lean proof that **θ(p_c) = 0 for nearest-neighbour
Bernoulli bond percolation on ℤ^d for all d ≥ 2**. This is the "dying
percolation" conjecture. It was previously known only for d = 2 and for high
dimensions, so the claim closes 3 ≤ d ≤ 10.

Who is behind it:
- **Justin Leder** has been a member of technical staff on Anthropic's data
  science and data engineering team since September 2025. Before that he was a
  McKinsey analyst, a Cruise analytics manager, and co-founder of the YC data
  tool Turntable. His Duke degree is in economics (one database says
  mathematics). He has no math publications and no Lean or probability
  background.
- The README says "no human wrote or edited the Lean code." Leder's stated
  role was "problem selection, direction, reading of the statement file and
  metadata," setting the acceptance standard, and taking responsibility for the
  submission. Anthropic mathematicians **Ralph Furman** and **Levent Alpöge**
  are thanked "for reading and comments."
- He is a genuine outsider to percolation theory, but he works inside the lab
  that built the model. This follows the precedent of the Riemann zeta entry,
  where a non-mathematician Anthropic employee was logged as an insider.

The mathematics:
- The route proves Conjecture 3 of **Kozma–Nitzan**
  ([arXiv:2401.12397](https://arxiv.org/abs/2401.12397)), a uniform gluing
  statement for connection probabilities, via a stronger new **additive gluing
  inequality** built from a "conditioned slack hierarchy" of covariance
  inequalities. Kozma–Nitzan's Theorem 6 then gives θ(p_c) = 0 for d ≥ 2, and
  that implication is re-proved in Lean too. Their Conjectures 1, 2, and 4 are
  not proved.
- The Lean development spans 251 files and ~97.6k lines. All seven main
  theorems depend only on the standard axioms (propext, Classical.choice,
  Quot.sound), with no custom axioms. The only two `sorry`s are deliberate
  placeholders in the challenge file. An independent kernel replay (nanoda) is
  recorded as passing.
- All definitions sit in `Challenge.lean` using Mathlib alone: ℤ^d as
  `Fin d → ℤ`, the Bernoulli measure on edges, clusters via reachability, and
  p_c as an infimum. The README itself says readers "should check that
  Challenge.lean states the intended theorem."
- No model, harness, prompts, or token spend is disclosed beyond "Anthropic's
  Claude models" and "about one week (August 2026)."

## Why it needs watching
- **The artifact was withdrawn from `main` and never announced.** All 13
  commits landed on 28 Aug 2026 within about four hours via
  [PR #22](https://github.com/anthropics/formal-math/pull/22), which Leder
  closed unmerged and whose branch he deleted within an hour. The `percolation/`
  directory does not exist on `main`, and the work survives only as a commit
  reachable by hash. Anthropic has made no public statement. A
  [request for the prompts](https://github.com/anthropics/formal-math/issues/26)
  is unanswered.
- **No human has read the proof or checked the definitions.** Statement
  fidelity is the load-bearing question. The additive gluing inequality holds
  on *arbitrary* finite weighted graphs, a very strong statement that
  [Gil Kalai](https://gilkalai.wordpress.com/2026/09/03/amazing-there-is-no-percolation-at-the-critical-probability-in-all-dimensions-solved-by-ai-via-a-conjecture-of-gady-kozma-and-shahaf-nitzan/)
  notes experts might have expected counterexamples to. Kalai's verdict: "If
  verified, this is a remarkable breakthrough … we still need to verify if the
  formalisation is done correctly."
- **Closest thing to independent use.** UPenn probabilist **Ahmed Bou-Rabee**
  [builds the pinned commit as a dependency](https://github.com/nitromannitol/percolation-after-anthropic)
  and, with more AI help, claims Kozma–Nitzan Conjectures 1, 2, and 4 plus site
  percolation for d ≥ 3. That is a compile, not a human read.
- **Quiet from the key experts.** Kozma, Nitzan, Hutchcroft, Grimmett, Buzzard,
  and Tao have not commented. Hugo Duminil-Copin's only related remark is a
  30 Aug [essay](https://proofsandprompts.com/2026/08/30/care-for-a-little-more-ai/)
  predicting AI would prove θ(p_c)=0 before humans. Timothy Chow reported it on
  [MathOverflow](https://mathoverflow.net/a/514873/11260) with caveats. There is
  no press or Hacker News thread. A Wikipedia edit naming Leder was reverted on
  12 Sep as "promotional, primary-sourced."
- Track: does a percolation specialist confirm that `Challenge.lean` states the
  real conjecture? Does anyone read and endorse the gluing inequality, or find a
  counterexample? Does Anthropic restore, announce, or explain the withdrawn
  work? Do Kozma or Nitzan comment?

## Review log
- [ ] **+1 week** (2026-09-22) —
- [ ] **+1 month** (2026-10-15) —
- [ ] **+3 months** (2026-12-15) —
- [ ] **+6 months** (2027-03-15) —
- [ ] **+1 year** (2027-09-15) —
