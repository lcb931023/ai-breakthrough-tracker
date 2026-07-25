---
claim: GPT-5.6 Pro produced a counterexample disproving Goemans' cost conjecture on unsplittable flow (the Dinitz–Garg–Goemans conjecture)
source: https://x.com/DmitryRybin1/status/2079904005652893709
field: Mathematics / graph theory & combinatorial optimization (network flows)
outsider: false
added: 2026-07-25
status: unverified
next_review: 2026-08-01
verdict:
---
## The claim
Dmitry Rybin — an ML PhD (CUHK), math BSc (HSE), math-olympiad medalist (IMC
gold, national olympiad gold), and cofounder of a Shenzhen AI-for-math startup
— announced on X on 22 July 2026 that he used **OpenAI's GPT-5.6 Pro** to
construct an explicit counterexample disproving **Goemans' cost conjecture**
on single-source unsplittable flow, informally called the
**Dinitz–Garg–Goemans conjecture**, open for roughly 30 years.

Background: Dinitz, Garg, and Goemans proved in 1999 that any fractional flow
respecting capacity constraints can be converted into an **unsplittable** flow
(each demand routed along a single path) that violates capacities by at most
the largest single demand. Goemans then conjectured a stronger **cost**
version: that such an unsplittable flow could always be found without
increasing total routing cost above the fractional solution's cost. That is
the conjecture now claimed false.

Specifics:
- Rybin says he used only **4 prompts, 58 words total**, across the entire
  session — including instructions like "do a breakthrough" and "enough of
  partial results, let's finish" — and **published the full chat transcript
  publicly**, so the model's reasoning can be read end-to-end rather than
  taken on faith.
- The counterexample: a fractional solution costing **58**, while every
  unsplittable solution respecting the allowed capacity violation costs **at
  least 60** — a gap of 2, sufficient to break the conjecture.
- Rybin himself has flagged that the result is **not yet independently
  verified** by outside mathematicians.
- The minimal, high-level prompting — with the model apparently doing most of
  the actual mathematical construction rather than being guided step-by-step
  — is itself the notable/scrutinized part of the claim.

Reported via [Rybin's announcement](https://x.com/DmitryRybin1/status/2079904005652893709),
[his follow-up explaining the result](https://x.com/DmitryRybin1/status/2079907499545919968),
and covered by [officechai](https://officechai.com/ai/mathematician-says-gpt-5-6-disproved-the-30-year-old-dinitz-garg-goemans-conjecture-with-4-simple-prompts/)
and others, July 2026.

## Why it needs watching
- **Not the outsider profile.** Rybin has math-adjacent training (ML PhD,
  math BSc, olympiad medals) and runs an AI-for-math startup, so he has both
  the expertise to construct/vet such a counterexample himself and an
  incentive to publicize an AI-math win.
- **The full transcript being public is a real plus for scrutiny** — contrast
  with the Jacobian-conjecture claim already tracked here, where no
  transcript was released. It should be straightforward for outside
  mathematicians to judge exactly how much of the reasoning was the model's
  own vs. Rybin's framing/steering.
- The core numeric claim (fractional cost 58 vs. unsplittable minimum cost
  60) is concrete and checkable by hand or computer — worth confirming an
  independent party has actually verified the arithmetic/graph construction,
  not just cited Rybin's own characterization of it.
- Track: does a combinatorial-optimization / network-flow specialist confirm
  the counterexample is valid and that it falsifies the *cost* conjecture as
  Goemans originally stated it (as opposed to a weaker or differently-scoped
  reading)? Any correction or retraction from Rybin?

## Review log
- [ ] **+1 week** (2026-08-01) —
- [ ] **+1 month** (2026-08-25) —
- [ ] **+3 months** (2026-10-25) —
- [ ] **+6 months** (2027-01-25) —
- [ ] **+1 year** (2027-07-25) —
