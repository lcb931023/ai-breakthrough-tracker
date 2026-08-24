---
claim: Anthropic reports Claude autonomously ran de novo protein-binder design campaigns against 15 targets, producing 354 wet-lab-confirmed binders out of 1,320 designs (22.6-35.1% hit rate) as measured by Adaptyv Bio and Twist Bioscience
source: https://www.anthropic.com/research/Claude-accelerates-protein-design
field: Biology / protein engineering
outsider: false
added: 2026-08-22
status: partially-confirmed
next_review: 2026-08-29
verdict:
---
## The claim
Anthropic reports that **Claude** — **Opus 4.8** and an unreleased
**Mythos Preview** build — autonomously ran de novo protein
**minibinder** design campaigns against **15 clinically relevant targets**
(PD-L1, TREM2, TNFα, EGFR, 15-PGDH, RBX1 and others), with no human input on
individual designs during a run. Of **1,320 designs**, **354 were confirmed to bind**, hitting
**14 of 15 targets**.

Specifics:
- Claude was given a ~16,000-word protocol prompt, up to
  **12,500 H100 GPU-hours**, and access to existing open-source tools (**RFdiffusion**,
  **ProteinMPNN**, **ESMFold2** and others). Claude chose binding sites,
  composed ~24 distinct tool workflows, ran optimization cycles, and ranked
  candidates — the model is the **orchestrator**, not the source of the
  underlying structure-prediction models (which come from the Baker lab,
  Columbia, MIT, ByteDance).
- Hit rates: **Mythos Preview 26.7%** and **Opus 4.8 22.6%** in 48-hour
  multi-target mode; **Mythos Preview 35.1%** in 24-hour single-target mode.
  Anthropic cites **10–15%** as a typical industry campaign hit rate.
- **Adaptyv Bio** and **Twist Bioscience** independently expressed and tested
  the designs. Adaptyv published [its own case study](https://www.adaptyvbio.com/blog/anthropic-1)
  reporting a 95% expression rate, binding measured by
  **SPR at 5 target concentrations in duplicate**, and overall
  **354/1,320 = 26.8%**. Adaptyv
  says Claude beat its own prior public design competitions on the same
  targets (TREM2: **80%** vs **38.3%**; RBX1 single-target: **40%** vs
  **3.7%** across 245 competition entrants) and improved best affinity on
  15-PGDH from **1.7 μM to 33.4 nM**. Its conclusion: Claude "seems to have
  matched or even surpassed expert protein designers" at orchestrating design
  tools.
- Prompts, computational models, and experimental data were released on
  HuggingFace.

Published as an [Anthropic research post](https://www.anthropic.com/research/Claude-accelerates-protein-design)
on 18 August 2026, with two linked technical reports. Not a peer-reviewed
paper.

## Why it needs watching
- **Vendor self-report, not an outsider claim.** Anthropic is reporting on its
  own models, and Adaptyv/Twist are paid service providers — independent in
  *execution* (they ran the assays and published concurring numbers) but not
  disinterested parties. Same pattern as the Riemann zeta critical-line claim
  logged 2026-08-11, in wet-lab form. Logged despite this tracker's outsider
  preference because the physical measurement is genuinely third-party and
  falsifiable.
- **The comparative claim is the soft part.** "22–35% vs a 10–15% industry
  baseline" is the headline, but that baseline is a rule of thumb, not a
  matched control. Target choice, binding-site difficulty, assay stringency,
  and what counts as a "hit" all move the number. The Adaptyv competition
  comparisons (TREM2, RBX1) are the tightest evidence, since the same lab ran
  the same assay on the same target.
- **Binders are not drugs, and affinity matters.** Anthropic says so itself.
  Former pharma executive **Martin Shkreli** called the work "not impressive,"
  citing weak affinities and noting that no intracellular targets were
  attempted ([TechTimes](https://www.techtimes.com/articles/325081/20260820/claude-runs-autonomous-protein-design-campaign-wet-lab-confirms-twice-industry-hit-rate.htm)).
  Anthropic also flags that "more extensive characterization to confirm our
  hit rates and affinity measurements" is still pending — the reported numbers
  are explicitly provisional.
- **Known failures are in the report.** MBP produced
  **0 binders from 90 designs**; the synthetic beta-barrel BBF-14 also went badly; GDF-8 (mature)
  was dropped for target aggregation. Anthropic admits it cannot explain why
  Opus 4.8 succeeded where Mythos Preview failed on one target.
- Track: does an unaffiliated lab reproduce a campaign from the released
  prompts? Does the promised fuller characterization hold the hit rates and
  affinities? Do protein-design specialists (Baker lab and peers) publish an
  assessment, and does the "matched or surpassed experts" framing survive it?
  Does any of this reach a preprint or journal?

## Review log
- [ ] **+1 week** (2026-08-29) —
- [ ] **+1 month** (2026-09-22) —
- [ ] **+3 months** (2026-11-22) —
- [ ] **+6 months** (2027-02-22) —
- [ ] **+1 year** (2027-08-22) —
