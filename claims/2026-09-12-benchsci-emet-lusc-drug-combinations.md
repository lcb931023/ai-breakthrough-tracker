---
claim: Jyothish Soman, a Cambridge-trained computer scientist and engineering manager at AI-for-pharma company BenchSci, and colleagues nominated and contract-lab-tested two drug-target combinations for lung squamous cell carcinoma, finding CDC7+PKMYT1 synergistic in two cell lines, with Emet, BenchSci's LLM agent layer over a 1.5-billion-triple biomedical knowledge graph
source: https://www.biorxiv.org/content/10.64898/2026.09.04.749404v1
field: Biology / oncology drug discovery
outsider: false
added: 2026-09-15
status: unverified
next_review: 2026-09-22
verdict:
---
## The claim
A bioRxiv preprint from BenchSci (v1 posted 9 Sep 2026, v2 10 Sep) reports that
**Emet**, the company's agentic research environment, proposed new drug-target
combinations for **lung squamous cell carcinoma (LUSC)** from an open-ended
prompt, and that two of four tested pairs worked in cell lines.

Who is behind it:
- **Jyothish Soman** (co-first author with Jordan Newington) holds a Cambridge
  computer-science PhD in graphs, HPC, and ML, and is an engineering manager at
  BenchSci. He previously built knowledge graphs at ComplyAdvantage and worked
  at Relation Therapeutics and Juvenescence.
- Co-authors are all BenchSci staff: ML engineers (Nikita Desai, ex-Exscientia;
  Simeon Wong), a computational biologist (Juliana Cudini), and pharma
  executives (Fernando Suarez Saiz, ex-IBM; Peter Grandsard, ~30 years at Amgen;
  Arnab Kundu, ex-AbbVie). No academic oncologist or cancer-biology lab is on
  the paper.
- **BenchSci** is a Toronto company founded in 2015 with roughly US$170M raised
  and ~300–400 employees. It launched Emet on 8 June 2026 and announced an argenx
  deal on 2 Sep 2026. This is a corporate product-validation study, not an
  outsider effort.

The AI engine: a knowledge graph (>1.5B triples from >6M papers and >100
databases) with an LLM agent layer. An "Agentic Research Director" runs a
graph-of-thoughts search with LLM planner, research, critic, and synthesizer
roles that call a graph neural network for link prediction. **No specific LLM
is named.** The supplement stresses that code, not the model, decides what to
explore and when to stop.

Human role: Emet produced dozens of hypotheses and kept the top 20. **Humans
vetted those and picked four to test**, chose the tool compounds, cell lines,
and assays, and contracted the wet lab to **Pharmaron (Beijing)**.

Results (NCI-H520 and SK-MES-1 cells, CellTiter-Glo viability, SynergyFinder+,
score > 10 counted as synergy):
- **CDC7 (TAK-931) + PKMYT1 (RP-6306).** Synergy grew from day 5 to day 7. In
  NCI-H520 the Bliss score rose from 13.49 to 21.65. In SK-MES-1 it rose from
  6.48 (additive) to 12.10. Mean inhibition stayed modest at 26–39%.
- **USP13 (spautin-1) + PI3Kα (alpelisib).** HSA scores were 7.86 and 1.58,
  both additive. Supplementary Bliss scores were −2.61 and −0.40, which is
  independent action, not synergy. The "mechanism confirmation" is western-blot
  densitometry after USP13 knockdown.
- **POLQ+TERT and GOLPH3+TERT** were inconclusive, with data not shown.

## Why it needs watching
- **Vendor self-validation.** Every author works at BenchSci, the lab was paid
  by BenchSci, the preprint has no competing-interests statement, and it landed
  alongside a product launch and sales announcements.
- **Novelty is weaker than claimed.** The paper says CDC7+PKMYT1 has "no
  precedent in any combination screen," but an April 2026 USF undergraduate
  [conference abstract](https://digitalcommons.usf.edu/usf_ourconference/2026/college_engineering/4/)
  reported synergy for the same two drugs in ovarian cancer lines. USP13+PI3K
  follows directly from a 2023
  [Molecular Cancer paper](https://link.springer.com/article/10.1186/s12943-023-01892-x)
  tying USP13 to PI3K/AKT signaling in LUSC. Combining DNA-damage checkpoint
  inhibitors is an established strategy.
- **Thin evidence.** 2D viability in two cell lines only, with no apoptosis,
  cell-cycle, or animal data. Bliss p-values as small as 10⁻¹⁰¹ suggest wells
  were treated as independent samples. The USP13 arm used high micromolar doses
  of spautin-1, which also hits USP10.
- **Autonomy is limited.** Humans chose which 4 of 20 ranked hypotheses to test
  and designed every experiment.
- **No outside engagement yet.** No press, no bioRxiv comments, no expert
  commentary, and no citations as of logging. A
  [2025 GPT-4 study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12134935/) in
  breast cancer is precedent for LLM-nominated, lab-confirmed combinations.
- Track: does an independent lab reproduce CDC7+PKMYT1 synergy in LUSC lines,
  ideally with apoptosis or in vivo data? Does the preprint pass peer review,
  and does review force revised novelty or statistics claims? Does any
  oncologist comment?

## Review log
- [ ] **+1 week** (2026-09-22) —
- [ ] **+1 month** (2026-10-15) —
- [ ] **+3 months** (2026-12-15) —
- [ ] **+6 months** (2027-03-15) —
- [ ] **+1 year** (2027-09-15) —
