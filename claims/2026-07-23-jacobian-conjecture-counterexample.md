---
claim: Claude Fable 5 generated an explicit degree-7 polynomial counterexample to the 1939 Jacobian conjecture
source: https://x.com/__alpoge__/status/2079028340955197566
field: Mathematics / algebraic geometry
outsider: false
added: 2026-07-23
status: unverified
next_review: 2026-07-30
verdict:
---
## The claim
Levent Alpöge, a mathematician at Anthropic, announced on X on 20 July 2026
that the **Jacobian conjecture** — posed by Ott-Heinrich Keller in 1939, one of
algebraic geometry's oldest open problems — is **false in dimension 3 and
above**. He credits **Claude Fable 5** with generating the counterexample
while he was "working during the World Cup final."

Specifics:
- The counterexample is an explicit degree-7 polynomial map
  F = (P, Q, R): ℂ³ → ℂ³ with **constant nonzero Jacobian determinant
  (det J_F ≡ −2)** — the conjecture's hypothesis — but **no polynomial
  inverse**: three distinct points, (0, 0, −1/4), (1, −3/2, 13/2), and
  (−1, 3/2, 13/2), all map to the same output (−1/4, 0, 0), so F is not
  even injective.
- The map is short enough (216 characters) to state in a single social-media
  post, and the determinant is **independently hand-checkable** — Alpöge
  included Wolfram Alpha links, and multiple outside users report verifying
  the arithmetic themselves within hours.
- **No prompt transcript, model log, or research notebook has been released**,
  so the end-to-end discovery process (how much search, how many failed
  attempts, how it was guided) cannot yet be independently audited.
  Researchers reportedly expected a counterexample, if any, to require degree
  up to ~200; Fable found one at degree 7.
- Fields Medalist **Terence Tao** wrote a same-week ["digestion" blog
  post](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/)
  giving a geometric interpretation of *why* the construction works — he
  treats the counterexample as established ("It was recently shown (using
  the Fable AI) that the conjecture is false in three dimensions") and notes
  the construction "appears like a massive miracle... highly unlikely to be
  located by brute force." His own AI disclosure is narrow: "I used an AI
  chatbot to discuss various aspects of this problem and to confirm several
  of the calculations made here" — i.e. Tao used AI to check the *write-up*,
  not to validate Alpöge/Fable's original discovery process.

Reported via [Alpöge's X thread](https://x.com/__alpoge__/status/2079028340955197566),
[Terence Tao's blog](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/),
[ForkLog](https://forklog.com/en/anthropics-claude-fable-5-finds-counterexample-to-1939-jacobian-conjecture/),
and [The Conversation](https://theconversation.com/hello-there-the-jacobian-conjecture-is-false-thanx-why-a-tiny-social-media-post-has-mathematicians-rethinking-ai-283883),
July 2026.

## Why it needs watching
- **Not the outsider profile** — Alpöge is a professional mathematician at
  the AI lab whose model he's crediting, so there's an obvious incentive to
  narrate this as "AI did it." The arithmetic (determinant ≡ −2, the
  three-way collision) is trivially checkable and looks solid; the open
  question is narrower and about *provenance*: how much of the actual
  search/discovery was Fable's versus Alpöge's own guidance, since no
  transcript has been published.
- **The result itself is not yet formally verified end-to-end.** What's been
  checked so far is the arithmetic of one explicit example, not a full
  peer-reviewed proof that this map is a valid counterexample under every
  reading of the conjecture, nor any formalization in Lean/Coq. Contrast
  with the Fable-5 QAOA proof (mechanically checked in Lean) — here nothing
  has been machine-verified yet.
- Tao's involvement is a strong positive signal for the *mathematics*, but
  his own disclosure shows he used AI only to check his write-up, not to
  independently reproduce the discovery — worth not overstating.
- Track: does a named domain expert (algebraic geometer) formally confirm
  the counterexample resolves the conjecture as stated (vs. a degenerate
  reading of it)? Does Anthropic or Alpöge release the actual
  transcript/log? Does any specialist push back on the construction or on
  the "AI found it" framing?

## Review log
- [ ] **+1 week** (2026-07-30) —
- [ ] **+1 month** (2026-08-23) —
- [ ] **+3 months** (2026-10-23) —
- [ ] **+6 months** (2027-01-23) —
- [ ] **+1 year** (2027-07-23) —
