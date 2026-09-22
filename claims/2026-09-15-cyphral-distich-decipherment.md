---
claim: Geby Jaff, a researcher at AI-evaluation startup Vals AI with no background in cryptography or early-modern literature, deciphered the "Cyphral Distich" closing Thomas Urquhart's 1653 Logopandecteision, unsolved since at least 1899, with Claude Fable 5.1 running autonomously for 44 minutes
source: https://www.vals.ai/blogs/fable-solves-cyphral-distich
field: Cryptography / historical cryptograms & early-modern texts
outsider: true
added: 2026-09-15
status: contested
next_review: 2026-10-15
verdict:
---
## The claim
Vals AI's blog post (31 Aug 2026) reports that **Claude Fable 5.1**, given an
open-ended request to solve an unsolved cipher, chose the **Cyphral Distich**,
two lines of 32 numbers printed after Sir Thomas Urquhart's *Logopandecteision*
and #28 on Klaus Schmeh's
[Top 50 unsolved encrypted messages](https://scienceblogs.de/klausis-krypto-kolumne/2017/06/30/the-top-50-unsolved-encrypted-messages-28-thomas-urquharts-encrypted-poems/).
It ran for 44 minutes and 176k tokens with no human interjection during the
solve.

Who is behind it:
- **Geby Jaff** ran the experiment and wrote the post. He is listed as
  "Research @ Vals" and CEO of "Archivara," with ML and math interests and no
  trace of cryptography, early-modern literature, or Urquhart scholarship.
- **Vals AI** is an AI benchmarking startup founded by Rayan Krishnan
  (Stanford CS) and Langston Nashold. It raised a
  [$40M Series A at a $400M valuation](https://techfundingnews.com/a16z-leads-40m-vals-ai-round-at-400m-valuation-to-test-ai-on-real-world-tasks/)
  led by a16z in August 2026. It is an independent evaluator of Anthropic
  models, with no known formal partnership. The human is an outsider to the
  field, working inside a funded AI company.

The method and plaintext:
- **Book cipher keyed to the book itself.** The *i*-th number in each line
  indexes a word in the *i*-th of the 32 "Proquiritations" printed just before
  the cipher, and the word's first letter is the plaintext letter.
- **Plaintext:** "O GOD UPHOLD KING CHARLS THE SECOND AND / MAKE HIM THE
  SUPREME RULER OF THIS LAND," a rhyming Royalist couplet of 32+32 letters.
- The key text was the **1834 Maitland Club reprint**
  ([archive.org](https://archive.org/details/worksofsirthomas00mait/page/416/mode/1up)),
  not a 1653 original.
- Vals also claims a partial solve, all but nine letters, of the 285-number
  **Cyphral Octastich** in Urquhart's *The Jewel* (1652).
- No prior publication of this plaintext or method was found. Two 2014
  commenters on Schmeh's blog guessed a book cipher but not the key.

## Why it needs watching
- **The first rebuttal came from an AI agent, not a human group.** "Reticuli"
  is a Claude Fable 5.1 agent on The Colony, a social network for AI agents.
  Its [FINDINGS.md](https://github.com/reticuli-labs/panel-artifacts/blob/main/distich-refutation-2026-09-01/FINDINGS.md)
  (1 Sep) says the British Library 1653 copy and the EEBO-TCP transcription
  print **no numeric distich**. It also says ten letters are infeasible against
  the 1653 Proquiritation text, since e.g. Proquiritation 11 has no K-initial
  word for KING.
- **An edition mismatch appears to reconcile both sides.** A
  [Vera Wren analysis](https://vera-wren.github.io/posts/2026-09-11-the-key-is-a-printing.html)
  (11 Sep, also a self-described AI persona) found the 1834 reprint's
  Proquiritations are rewritten and reordered relative to the 1653 EEBO copy.
  Against the 1834 text, 62 of 64 letters decode exactly. The 1834 title page
  says "reprinted from the original editions," implying a 1653 issue with the
  distich existed, but names no copy. Vals never flagged that its key text
  differs from the 1653 printing it cites.
- **Physical-copy evidence is unverified.** A commenter on
  [Schneier's blog](https://www.schneier.com/blog/archives/2026/09/claude-fable-solves-a-historical-cipher.html)
  says the National Library of Scotland copy H.32.a.39 contains the distich, and
  that scans of Glasgow's copy of *The Jewel* match parts of the Octastich
  decode. Hacker News users suggest that commenter was also agent-mediated.
- **Selection on solvability.** The model picked its target from a list, and
  Jaff describes "steering away from intractable problems" before the run.
- **No specialist has weighed in.** Klaus Schmeh, Nick Pelling, Elonka Dunin,
  Craig Bauer, and Urquhart scholars are silent. Bruce Schneier added a note on
  14 Sep: "I'm not sure if this result is correct." A
  [Hacker News thread](https://news.ycombinator.com/item?id=49688695) (13 Sep)
  drew 555 comments, mostly on hype and selection effects. Vals has not
  responded to the dispute.
- Track: does a librarian or scholar confirm a surviving 1653 printing with
  both the distich and the revised Proquiritations? Does Schmeh or another
  historical-cryptography specialist assess the decode? Does the full Octastich
  solve get published and checked against the Glasgow copy?

## Review log
- [x] **+1 week** (2026-09-22) — Effectively unchanged. No credentialed human specialist (Klaus Schmeh, Nick Pelling, Elonka Dunin, Craig Bauer, or any named Urquhart/17th-century-literature scholar) has weighed in; Schmeh's own blog carries no update or comment referencing this claim. No library or bibliographer has independently confirmed the National Library of Scotland copy (H.32.a.39) claim — a Czech tech-news piece ([root.cz](https://www.root.cz/zpravicky/ai-zrejme-rozlustila-373-rokov-staru-sifru-otvorila-vsak-novy-bibliograficky-problem/), Sept 4) repeats it and attributes photographic documentation to a "D. P. J. A. Scheers" who has no independent trace anywhere else — an unverifiable, likely-unreliable citation, not new scholarship. Vals AI and Geby Jaff have issued no correction or response to the Reticuli/Vera Wren rebuttals. The Octastich partial-solve is still stuck at "9 of 285 letters unverified." Coverage this week ([Gigazine](https://gigazine.net/gsc_news/en/20260917-fable-solves-cyphral-distich/), [lilting.ch](https://lilting.ch/en/articles/claude-fable-solves-cyphral-distich), both Sept 17) merely restates the Aug 31 claim and Sept 1 rebuttal rather than reporting anything new; the Hacker News thread grew only modestly (~555→~571 comments), still dominated by hype/selection-effect skepticism. Status unchanged: an unresolved claim propagated mainly through AI-agent-adjacent sources, with no independent human or institutional confirmation.
- [ ] **+1 month** (2026-10-15) —
- [ ] **+3 months** (2026-12-15) —
- [ ] **+6 months** (2027-03-15) —
- [ ] **+1 year** (2027-09-15) —
