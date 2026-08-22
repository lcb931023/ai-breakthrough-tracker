---
claim: A neurosurgery resident with no formal math training used GPT-5.6 Sol's 16-hour autonomous run to produce a proof of the 22-year-old Crouzeix's Conjecture
source: https://www.scmp.com/tech/tech-trends/article/3363966/chinese-doctor-stuns-maths-world-cracking-decades-old-problem-using-chatgpt
field: Mathematics / numerical linear algebra (matrix analysis)
outsider: true
added: 2026-08-15
status: partially-confirmed
next_review: 2026-09-15
verdict:
---
## The claim
**Shanmu Jin**, a postdoctoral researcher and neurosurgery resident at Peking
Union Medical College Hospital in Beijing, has no formal academic background
in advanced mathematics — his undergraduate degree is in geology, followed by
an MD. He says his interest in matrix analysis grew out of his own clinical
research on transcranial ultrasound. Working essentially alone, he set
**GPT-5.6 Sol** (in ChatGPT's "Work" mode) loose on **Crouzeix's Conjecture**
— posed by Michel Crouzeix in 2004 and open for 22 years, stating that for any
matrix A and any function f, ‖f(A)‖ ≤ 2·sup{|f(z)| : z in the numerical range
of A}.

Specifics:
- The model ran **autonomously for ~16 hours**, using a prompt Jin adapted
  from one OpenAI had used for its Cycle Double Cover proof: disconnected
  from the internet (forcing derivation from axioms rather than lookup),
  instructed to pursue multiple divergent proof branches rather than
  converging early, to adversarially attack its own candidate arguments with
  counterexamples, and not to stop short of a complete proof.
- The key step was a sampling strategy that converts the bound into a
  simpler positivity condition.
- Jin open-sourced everything on GitHub — prompt, successive manuscript
  drafts, a Lean formalization, and an "axiom audit" —
  [jinshanmu/CrouzeixConjecture](https://github.com/jinshanmu/CrouzeixConjecture).
- Cornell numerical analyst **Alex Townsend** learned of the claim (via
  ChatGPT itself, on July 30, telling him the problem "had been solved three
  days ago"), reviewed the manuscript, and brought in **Anne Greenbaum**
  (University of Washington). Both, along with **Michel Crouzeix** himself,
  checked the argument and believe it is correct. Townsend wrote up the story
  for [SIAM News](https://alextownsend.net/essays/SIAMNews_CrouzeixConjecture.pdf).
- **Not yet peer-reviewed.**
- Notably, eight days later (4 August 2026), professional mathematicians
  **Emiel Lorist and Felix Schwenninger** posted an independent, five-page,
  purely human-derived proof using a different method (double-layer-potential
  representation plus a perturbation lemma for 2-dilations) —
  [arXiv:2608.03841](https://arxiv.org/abs/2608.03841) — with no mention of
  AI assistance and no reference to Jin's proof, suggesting genuinely
  convergent, independent resolution of the conjecture rather than one proof
  copying the other.

## Why it needs watching
- **Strong outsider case** — a physician with no formal math training,
  reportedly getting a correct answer to a 22-year-old open problem in a
  specialist subfield via an autonomous AI run.
- **Verification so far is informal** — Townsend, Greenbaum, and Crouzeix
  have checked the argument and found no error, but there is no peer-reviewed
  publication, and Jin's manuscript submission status (e.g. to Annals or a
  specialist journal) should be tracked.
- **The independent Lorist–Schwenninger proof is the strongest evidence** —
  if a completely separate, human, peer-reviewable proof reaches the same
  conclusion by a different route, that's a good sign the conjecture is
  actually true regardless of any lingering doubts about Jin's specific
  argument. Track whether the Lorist–Schwenninger paper clears peer review.
- Watch for: formal peer review or journal acceptance of either proof, a Lean
  formalization of Jin's proof reaching completion, any errors found by
  outside reviewers, and broader numerical-analysis community commentary
  (MathOverflow, specialist blogs, conference talks).

## Review log
- [x] **+1 week** (2026-08-22) — No error has surfaced in Jin's manuscript ("The Numerical Range Is a 2-Spectral Set," posted 27 Jul) despite continued informal scrutiny; Townsend, Greenbaum, and Crouzeix's earlier read-through still stands and independent computational/adversarial audits in Jin's own repo report none found. The independent Lorist–Schwenninger proof ([arXiv:2608.03841](https://arxiv.org/abs/2608.03841), submitted 4 Aug via a different double-layer-potential method) remains the strongest corroborating signal — two structurally different routes reaching the same conclusion. Neither manuscript has entered formal peer review or a journal pipeline yet, and no MathOverflow or specialist-blog rebuttal has appeared. Coverage: [Remio](https://www.remio.ai/post/shanmu-jin-used-ai-on-the-crouzeix-conjecture-but-the-proof-still-needs-human-ju), [Townsend's SIAM News essay](https://alextownsend.net/essays/SIAMNews_CrouzeixConjecture.pdf). Status moved to partially-confirmed on the strength of convergent independent derivations, pending actual peer review.
- [ ] **+1 month** (2026-09-15) —
- [ ] **+3 months** (2026-11-15) —
- [ ] **+6 months** (2027-02-15) —
- [ ] **+1 year** (2027-08-15) —
