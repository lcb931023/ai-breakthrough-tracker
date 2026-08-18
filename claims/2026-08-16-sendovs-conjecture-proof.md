---
claim: GPT-5.6 Pro, directed by Lech Mazur, generated a proof of Sendov's Conjecture and the Phelps–Rodriguez conjecture, independently reformalized in Lean by Terence Tao
source: https://terrytao.wordpress.com/2026/08/12/a-digestion-of-the-proof-of-sendovs-conjecture/
field: Mathematics / complex analysis
outsider: true
added: 2026-08-16
status: unverified
next_review: 2026-08-23
verdict:
---
## The claim
Lech Mazur — founder/CEO of Advameg, Inc. and City-Data.com, and more recently
an author of LLM evaluation benchmarks, but with no evidence of formal
mathematics training or prior peer-reviewed math work — used **OpenAI's
GPT-5.6 Pro** to generate a proof of **Sendov's Conjecture**, open for 54
years, and the related **Phelps–Rodriguez conjecture**, in complex analysis.
Both concern the location of a polynomial's critical points relative to its
roots.

Specifics:
- Published via ProofAtlas (a platform Mazur appears to run) as "A
  Computer-Assisted Proof of Sendov's Conjecture," dated 5 August 2026.
- Mazur's stated role: designing and running the orchestration/verification
  workflow, and selecting and reconciling GPT-5.6 Pro's outputs. GPT-5.6 Pro
  is credited with the mathematical exploration, proof derivation, exact
  computational testing, and adversarial auditing.
- The proof reduces to a "Conjecture 3" claimed to resolve both target
  conjectures in full generality, via an argument described as elementary
  (using only the fundamental theorem of algebra and the Maclaurin
  inequality, no heavier complex analysis).
- Fields medalist **Terence Tao** independently reformalized the entire
  argument in **Lean 4** (~15,000 lines, versus ~90,000 in the original
  writeup) and posted a "digestion" of the proof on his blog (12 August
  2026), aiming to place it in context with prior literature and streamline
  the exposition.

Reported via [Terence Tao's blog](https://terrytao.wordpress.com/2026/08/12/a-digestion-of-the-proof-of-sendovs-conjecture/)
and [the ProofAtlas paper](https://www.proofatlas.ai/papers/sendov-conjecture/SENDOV_CONJECTURE_PROOF_AUGUST_5_2026.pdf).

## Why it needs watching
- **Outsider profile, but a sophisticated one.** No university degree, PhD,
  or prior math publication record was found for Mazur — his documented
  background is tech entrepreneurship (Advameg/City-Data.com) and, lately,
  AI-benchmark authorship, not research mathematics. He presents himself
  explicitly as the human orchestrator/curator of an AI system rather than
  as the mathematician who derived the proof.
- **Strong early verification signal**, unusually so for a claim this fresh:
  an independent, credentialed expert (Tao) engaged deeply enough to
  reformalize the whole argument in Lean and write up a public exposition —
  that is a much higher bar than typical early-stage "looks plausible"
  commentary. Worth confirming whether Tao's writeup amounts to an
  endorsement of correctness or just a formalization exercise agnostic to
  truth.
- Still a preprint / self-published proof, not peer-reviewed or published in
  a journal.
- Track: does the broader complex-analysis community (beyond Tao) weigh in?
  Does Tao's Lean formalization actually compile and check without gaps?
  Does anyone dispute the division of credit between GPT-5.6 Pro and Mazur's
  orchestration?

## Review log
- [ ] **+1 week** (2026-08-23) —
- [ ] **+1 month** (2026-09-16) —
- [ ] **+3 months** (2026-11-16) —
- [ ] **+6 months** (2027-02-16) —
- [ ] **+1 year** (2027-08-16) —
