---
claim: OpenAI's math team, led by ML researcher Sébastien Bubeck, produced a 166-page proof of finite-time blow-up for the forced 3D Navier–Stokes equations, claiming to settle the Clay Millennium Prize Problem, with ~10,000 concurrent agents running an unreleased model more capable than GPT-6 Astra
source: https://openai.com/index/navier-stokes-solution/
field: Mathematics / fluid dynamics (PDE)
outsider: false
added: 2026-09-15
status: contested
next_review: 2026-09-22
verdict:
---
## The claim
OpenAI's paper "Finite Time Blowup for Navier–Stokes"
([PDF](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf),
166 pages, authored only as "OpenAI") claims a **disproof**, not a regularity
result. For every viscosity ν > 0 it builds a smooth, compactly supported
**force**, zero initial velocity, and a smooth finite-energy solution on
R³×[0,1) whose L∞ norm blows up as t → 1. OpenAI says this establishes
alternative (C) of the Clay problem statement on R³, and alternative (D) on the
torus via compact support.

Who is behind it:
- **Sébastien Bubeck** leads OpenAI's math team and ran the effort. His
  background is ML and optimization, not PDE. By his own account the team had
  math, physics, and CS backgrounds but "lacked research-level expertise in
  fluid dynamics."
- **Ven Chandrasekaran**, Mark Chen, Noam Brown, and Sam Altman are the other
  named OpenAI figures. **No outside mathematician co-authored or checked the
  proof.** This is a big-lab result, logged here despite the tracker's
  outsider preference because it is the most prominent and most disputed AI
  math claim to date.

Process, per OpenAI: an internal model trained from 28 Aug ran as ~10,000
concurrent agents for 88 hours (1–5 Sep), exchanging 2.7M messages and ~130B
output tokens. GPT-6 Astra then produced a
[Lean 4 formalization](https://github.com/openai/NavierStokesAndEuler) in 17
more hours. The mechanism is an inward-spiraling, axially stretched vortex
built with a Córdoba–Martínez-Zoroa-style multi-scale amplification. A
companion 57-page paper claims blow-up for the unforced Euler equations.

## Why it needs watching
- **Forced only.** The unforced Cauchy problem, which most PDE specialists mean
  by "Navier–Stokes," is untouched. Princeton's **Stan Palasek**
  [pointed out](https://mathstodon.xyz/@palasek/117235270483911935) a heuristic
  obstacle to removing the force in 3D via this style of lacunary construction,
  which **Terence Tao** [called](https://mathstodon.xyz/@tao/117236063705269594)
  "a good observation." It does not refute the forced result.
- **Priority and conduct dispute.** NYU's **Tristan Buckmaster** and
  **Levent Alpöge** (an Anthropic employee, collaborating personally) say they
  had smooth-forced blow-up for IPM, Boussinesq, and 3D Euler on 15 Aug,
  Lean-verified 22 Aug, using Claude and Codex. Buckmaster's
  [statement](https://cims.nyu.edu/~tristanb/statement.pdf) says OpenAI's first
  prompt was sent "after information about our work had reached OpenAI," and
  that Bubeck pushed to drop Alpöge from authorship. He also says he has not
  seen OpenAI's proof and is "not accusing anyone of anything." Bubeck
  [called](https://x.com/SebastienBubeck/status/2097214122471432349) the
  allegations "false and inflammatory." OpenAI's paper does not cite
  Alpöge–Buckmaster.
- **OpenAI's data-use story shifted.** It moved from "cannot rule out" that
  de-identified Codex data helped its models (8 Sep), to "categorically"
  impossible (9 Sep), to "no user inputs past July 3rd" (13 Sep), per the
  [Wikipedia timeline](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_priority_controversy).
- **Community backlash at the framing.** Tao's blog post
  ["A Severe Misalignment of AI in Mathematics"](https://terrytao.wordpress.com/2026/09/11/a-severe-misalignment-of-ai-in-mathematics/)
  (11 Sep), signed by 25 Fields Medalists, criticizes the rushed announcement.
  **Charles Fefferman**, who wrote the Clay problem statement, told
  [Quanta](https://www.quantamagazine.org/ai-has-solved-one-of-maths-1-million-millennium-prize-problems-20260908/)
  he was "thrilled that the problem was solved" and called Córdoba and
  Martínez-Zoroa "the heroes of the story."
- **No independent verification yet, and no error found.** The Lean build is
  public but only self-assessed. The
  [Clay Institute](https://www.claymath.org/news/navier-stokes-announcement/)
  says the problem "has apparently been settled" and promises a "deliberately
  unhurried" evaluation. The prize requires publication plus two years of
  acceptance, and OpenAI says it will not claim it.
- Track: does an outside group reproduce the Lean build and audit its
  definitions against the Clay statement? Does a human write-up reach a
  journal? Does the Alpöge–Buckmaster work appear and how do the two compare?
  Does Clay's evaluation reach a conclusion? Does anyone remove the force?

## Review log
- [ ] **+1 week** (2026-09-22) —
- [ ] **+1 month** (2026-10-15) —
- [ ] **+3 months** (2026-12-15) —
- [ ] **+6 months** (2027-03-15) —
- [ ] **+1 year** (2027-09-15) —
