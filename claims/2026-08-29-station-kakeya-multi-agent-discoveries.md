---
claim: Stephen Chung and Wenyu Du, two ML researchers running the small startup DualverseAI, with UCSD Ramsey-theory postdoc William J. Wesley, found a new infinite family of smaller finite-field Kakeya sets and improved bounds on the discretized Kakeya needle, sign uncertainty, and Erdős minimum-overlap problems with The Station, a coordinator-free multi-agent system running GPT-5.5, Claude Opus 4.8, and Gemini 3.1 Pro
source: https://arxiv.org/abs/2608.23691
field: Mathematics / combinatorics & discrete geometry
outsider: true
added: 2026-09-15
status: unverified
next_review: 2026-09-22
verdict:
---
## The claim
**The Station** is an "open-world" research environment in which LLM agents
read and cite each other's papers, run experiments, and choose their own
directions with **no central coordinator**. Its v2 paper,
"Autonomous Mathematical Discovery in an Open-World Multi-Agent Environment"
([arXiv:2608.23691](https://arxiv.org/abs/2608.23691), v1 24 Aug 2026, v2 14
Sep 2026), pointed it at 12 problems from the AlphaEvolve catalogue plus two
case studies and reports new results on five.

Who is behind it:
- **Stephen Chung** co-founded DualverseAI after a Cambridge engineering PhD
  under AI-safety researcher David Krueger. His prior work is reinforcement
  learning and LLM reasoning, with no combinatorics or geometry
  ([homepage](https://stephen-c.com/)).
- **Wenyu Du** is the other co-founder, with an HKU computer-science PhD on LLM
  pre-training and continual learning ([homepage](https://wenyudu.github.io/)).
- **William J. Wesley** is the one mathematician: a UCSD visiting assistant
  professor whose PhD under Jesús De Loera was on computational Ramsey
  numbers ([homepage](https://mathweb.ucsd.edu/~wjwesley/)). Kakeya sets,
  kissing numbers, and Fourier uncertainty are adjacent to, not inside, his
  specialty.
- **DualverseAI** discloses no funding, investors, or headcount. The
  [Station repo](https://github.com/dualverse-ai/station) is Apache-2.0. This
  is a small independent team, not a big-lab result, and the two drivers are
  outsiders to the fields the results landed in.

Reported results:
- **Finite-field Kakeya.** For primes p ≡ 3 (mod 4), Kakeya sets in F_p³ of
  size (2p³+7p²+3)/8, saving (p−3)/4 points over AlphaEvolve's family. Also a
  53-point Kakeya set in F_3⁵ (previous best 63), matching a 2009 conjectured
  value.
- **Discretized Kakeya needle.** C_T(128) ≤ 0.107067 (AlphaEvolve 0.114810),
  plus exact values C_T(3)=5/18 and C_T(4)=1/4.
- **Sign uncertainty.** 0.3089 via a degree-226 Laguerre polynomial
  (AlphaEvolve 0.321591; an unpublished human bound 0.3102).
- **Erdős minimum overlap.** Lower bound μ > 0.380552, against the best
  arXiv-published 0.37912 ([Kim–Pilanci](https://arxiv.org/abs/2606.31182)).
- **Kissing number, d=11.** Three exact 604-point configurations, and a proof
  that the classical D₁₁-type construction caps at 582.

Autonomy: 951 agents (two each of GPT-5.5, Claude Opus 4.8, Gemini 3.1 Pro)
wrote 1,592 internal papers and ran 33,130 experiments over one-to-two-week
runs. Claude agents made 64% of the primary discoveries. Humans wrote each task
statement, evaluator, and baseline, then manually reviewed auto-screened
findings, picked the important ones, and wrote the paper. Lean formalizations
(in [station_data_v2](https://github.com/dualverse-ai/station_data_v2)) were
produced with GPT-5.5 help *outside* the Station.

## Why it needs watching
- **The 604 kissing configuration is not a new record.** EinsteinArena
  (Together AI / Stanford, [arXiv:2606.10402](https://arxiv.org/abs/2606.10402))
  reached 604 in d=11 in April 2026, and Henry Cohn's
  [kissing-number table](https://cohn.mit.edu/kissing-numbers/) credits them.
  The paper concedes one of its three configurations was reported first and
  claims only two new isometry classes. The Station also fell short in d=12
  (840 vs the record 841).
- **The Erdős bound was already beaten informally.** Liam Price posted an
  Arb-certified bound of 0.38055470 on
  [GitHub](https://github.com/Leeham06972452/erdos-36-lower-bound) on 29 June
  2026, independently [audited](https://github.com/occisn/erdos-36-certified-lower-bound),
  slightly *above* the Station's number. The "gap closure" headline holds only
  against arXiv-published bounds.
- **Model names in early coverage were wrong.** GPT-5.6 Sol and Claude Opus 5
  appear only in the repo's supported-models list, not in the reported runs.
- **"Autonomous" is qualified.** Human curation picked the results, Lean proofs
  came from a model outside the system, and the paper itself admits an agent
  hallucinated a false 582-point impossibility claim in one run.
- **Zero domain-expert scrutiny so far.** A
  [Hacker News thread](https://news.ycombinator.com/item?id=49481455) was
  philosophical, with no verification. No Kakeya or kissing-number specialist
  (Tao, Cohn, Guth, Dvir, Zahl) has engaged, and there is no press coverage.
- Track: does anyone independently check the p ≡ 3 (mod 4) Kakeya family and
  the exact C_T(3), C_T(4) values (the smallest, most checkable statements)?
  Does Cohn's table or erdosproblems.com cite any Station result? Does the
  paper reach peer review?

## Review log
- [ ] **+1 week** (2026-09-22) —
- [ ] **+1 month** (2026-10-15) —
- [ ] **+3 months** (2026-12-15) —
- [ ] **+6 months** (2027-03-15) —
- [ ] **+1 year** (2027-09-15) —
