---
claim: Lech Mazur, an LLM-benchmark author with no formal math training, generated proofs of Sendov's Conjecture and the Phelps–Rodriguez conjecture with GPT-5.6 Pro
source: https://terrytao.wordpress.com/2026/08/12/a-digestion-of-the-proof-of-sendovs-conjecture/
field: Mathematics / complex analysis
outsider: true
added: 2026-08-16
status: partially-confirmed
next_review: 2027-02-16
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
- [x] **+1 week** (2026-08-23) — Independent mechanical corroboration has arrived: Tao's Lean 4 formalization ([github.com/teorth/sendov](https://github.com/teorth/sendov)) reports the build has "no `sorry` and no project-defined `axiom`," and Tao submitted it to [Palomar](https://terrytao.wordpress.com/2026/08/18/palomar-a-registry-of-lean-verified-mathematics/), a new Lean-FRO-backed verification registry, for mechanical typechecking — though Tao himself cautions such checks "fall well short of ... proper human peer review for novelty, interest, and accuracy." Notably, Tao's own Lean formalization was "essentially all written by Claude Opus 5," with no independent human review of that Lean source. On credit: mathematician Karim Adiprasito directly disputed the attribution in Tao's blog comments — "I don't think his name can reasonably be attached as main author without transparency... nice that chatgpt found a proof, even nicer that Terry digested it" — and no one in the thread defended sole-authorship framing for Mazur. Mathematician Teng Zhang engaged constructively, extending the result to a majorization/spectral formulation, without disputing correctness. No journal peer review yet, and ProofAtlas's own site still shows an inconsistent, seemingly stale "planned, not complete" note on Lean verification. Moving to partially-confirmed: credible independent mechanical verification exists, but no peer review and an active, unresolved credit dispute.
- [x] **+1 month** (2026-09-16) — Further independent corroboration, no contradicting evidence found. Mathematician Senjian An posted [a follow-on paper](https://arxiv.org/html/2609.04246) (submitted 22 Aug 2026) that explicitly accepts the Mazur–Tao reductions as proven and replaces their remaining numerical-search step with an elementary scalar-optimization argument backed by a fixed, auditable 272-point rational-arithmetic certificate — a second, differently-trained researcher independently working through and extending the proof's internals is a stronger signal than passive endorsement. An's paper is itself LLM-assisted (ChatGPT, for proof architecture/algebra/code) but states "no language-model output is treated as mathematical evidence." ProofAtlas's own formalization page still explicitly disclaims "accepted-result" status, listing four still-open review categories (formal evidence review, statement alignment, result boundary, public wording) and confirms the Lean build has "no unfinished proof steps" and no extra axioms beyond the standard `propext`/`Classical.choice`/`Quot.sound`. No submission-to-Palomar completion or journal peer review found yet. The Tao-vs-Adiprasito authorship dispute from the prior review period has not resurfaced or been resolved either way. Holding at partially-confirmed: mathematics keeps checking out under independent scrutiny, but the process (peer review, Palomar acceptance, credit) that would move this to confirmed is still unresolved.
- [x] **+3 months** (2026-11-16) — Independent build-out keeps accelerating
  rather than stalling. New arXiv papers now treat the Mazur–Tao result as
  settled foundation to extend: Teng Zhang's
  ["Beyond Sendov's conjecture: the quadratic Tang–Zhang
  inequality"](https://arxiv.org/pdf/2609.19126), a paper making Tao's 2022
  partial bound effective — ["Sendov's conjecture holds for every degree
  n≥10^200000"](https://arxiv.org/pdf/2609.20256) — and follow-on papers on
  Borcea's variance conjectures ([2610.02035](https://arxiv.org/pdf/2610.02035),
  [2610.12499](https://arxiv.org/pdf/2610.12499)) built on the same machinery.
  Multiple independent researchers now working from the result as true is a
  stronger signal than passive endorsement. Boris Alexeev produced a second,
  independent Lean 4 formalization. The [Palomar registry](https://letsdatascience.com/news/palomar-opens-registry-for-lean-verified-mathematics-ec8cddcc)
  opened 18 August with Tao on its scientific advisory board, and Tao has
  submitted his formalization — but no confirmation of full Palomar
  acceptance completing was found, and no journal peer review has concluded.
  A [remio.ai analysis](https://www.remio.ai/post/lech-mazurs-ai-assisted-sendov-conjecture-proof-changes-what-counts-as-evidence)
  states conventional peer review "has not been completed" and flags that
  credit distribution for AI-assisted math "will become contentious," but the
  earlier Tao–Adiprasito credit dispute did not resurface. Holding at
  `partially-confirmed`: the mathematics keeps checking out under growing
  independent scrutiny, but formal peer review and registry completion are
  still open.
- [ ] **+6 months** (2027-02-16) —
- [ ] **+1 year** (2027-08-16) —
