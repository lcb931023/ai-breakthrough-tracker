---
claim: GPT-5.6 Sol Ultra produced a complete proof of the Cycle Double Cover Conjecture
source: https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_proof.pdf
field: Mathematics / graph theory
outsider: false
added: 2026-07-13
status: partially-confirmed
next_review: 2026-08-13
verdict:
---
## The claim
OpenAI reports that **GPT-5.6 Sol Ultra**, running **64 parallel subagents for
~1 hour**, generated a complete proof of the **Cycle Double Cover Conjecture** —
a ~50-year-old open problem in graph theory (posed by Seymour, 1979): every
bridgeless graph admits a collection of cycles such that every edge lies in
exactly two of them.

Specifics:
- The proof PDF, published on OpenAI's CDN (10 July 2026), attributes authorship
  **entirely to the model**.
- The argument reportedly reduces the problem via the **8-flow theorem** and
  linear algebra over **GF(3)** (the three-element field).
- OpenAI also released the [prompt used](https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_prompt.pdf).

Reported via OpenAI and covered on
[Hacker News](https://news.ycombinator.com/item?id=48863490),
[The Decoder](https://the-decoder.com/openais-gpt-5-6-sol-ultra-reportedly-solves-a-50-year-old-math-problem-in-under-an-hour/),
and others, July 2026.

## Why it needs watching
- **Not the outsider profile** — this is a flagship OpenAI lab announcement, AI
  used by its own makers as a marketing demonstration. The interesting question
  is narrow: does the proof actually hold?
- **No formal verification.** Unlike the Fable-5 QAOA proof (mechanically checked
  end-to-end in Lean 4), this proof is **not peer-reviewed and not machine-
  verified** — it's a natural-language argument the community must check by hand,
  expected to take days to weeks.
- **Authorship dispute already brewing.** Mathematicians are flagging possible
  gaps and questioning how much of the reasoning was the model's own vs. baked
  into the human prompter's search-guiding constraints (see the released prompt).
- **The conjecture is a graveyard.** The Cycle Double Cover Conjecture has a
  history of announced "proofs" that later collapsed — strong prior for
  skepticism until specialists sign off.

## Review log
- [x] **+1 week** (2026-07-20) — First real domain-expert engagement: Thomas Bloom (mathematician, University of Manchester) [reviewed the proof on X](https://x.com/thomasfbloom/status/2075855061494706240) and called it "a very nice proof" — short, elementary, and combining only known tools in a way "that could have been discovered in the 1980s," with the interesting part being a small counterintuitive twist a human might have abandoned early. That's a positive signal from a credentialed outsider-to-the-hype-cycle reviewer, not a rubber stamp: Bloom also flagged that the proof omits citation to a foundational 1983 Bermond–Jackson–Jaeger paper whose ideas appear to underlie the core reduction — an attribution gap, not (so far) a correctness gap. No formal peer review, journal submission, or independent full line-by-line verification has happened yet, and — contrary to some aggregator claims — [no Lean/Coq formalization exists](https://dev.to/jamilxt/gpt-56-claims-to-solve-a-50-year-old-math-problem-nobody-can-confirm-it-50f7): commentary notes current Lean graph-theory libraries (e.g. Graphlib) aren't mature enough for a proof at this level, so it remains a natural-language argument the community must check by hand. Given the conjecture's history of collapsed "proofs," one favorable spot-check from one mathematician is meaningful but not sufficient. Status moved to partially-confirmed: a specialist read it and found the mathematics plausible/elementary rather than crankish, but full verification is still pending.
- [ ] **+1 month** (2026-08-13) —
- [ ] **+3 months** (2026-10-13) —
- [ ] **+6 months** (2027-01-13) —
- [ ] **+1 year** (2027-07-13) —
