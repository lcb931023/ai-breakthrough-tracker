# Web UI: discipline / outsider filters + verification-progress readout

**Date:** 2026-08-10
**Status:** approved, implemented

## Goal

Three additions to the generated site (`docs/index.html`):

1. Filter claims by discipline.
2. Filter to outsider claims only.
3. Show verification progress at the top of the page — how much of the docket is
   unverified, partially confirmed, refuted, or has gone stale.

## Decisions

### Staleness is derived, not stored

"Went stale" (nobody serious engaged with the claim) is not in the frontmatter
vocabulary. It is computed in `build.py`:

```
stale := (ticked review milestones >= 2) AND (status == "unverified")
```

Meaning: we looked repeatedly and the community said nothing. This needs no
schema change, no `AGENT.md` change, and no backfill of existing claim files.
Against the corpus as of 2026-08-10 it flags exactly one entry — the Linear A
decipherment (added 2026-06-26, 1w and 1mo milestones ticked, still unverified).

Rejected alternatives: a purely age-based rule (flags claims that are merely
young-and-quiet, and silently marks everything stale if the review cadence
breaks), and an explicit `stale: true` frontmatter key (most accurate, but needs
an `AGENT.md` rule so the daily agent maintains it, plus backfill).

### Buckets are mutually exclusive

The six display buckets must sum to the claim total, so `stale` takes precedence
over the raw status: a stale claim counts as `stale`, **not** as `unverified`.
`unverified` on the page therefore means "unverified and not yet stale".

Buckets, in display order: `unverified`, `stale`, `contested`,
`partially-confirmed`, `confirmed`, `debunked` (labelled "refuted").
`contested` and `confirmed` are included even though the original request
listed only four — omitting them would hide claims from the counts.

### Discipline chips: derived head + a small merge map

`field` values are freeform prose ("Mathematics / graph theory (spectral graph
theory)"). The chip is the text before the first `/` or `(`, then a small
hardcoded table folds related heads together:

```
DISCIPLINE_MERGE = {"Mathematical physics": "Physics",
                    "Statistical physics": "Physics"}
```

Unknown heads fall through unchanged, so a new field the daily agent invents
buckets itself with no code change; the map only needs updating when two heads
should merge. Current result: Mathematics 4, Physics 2, Linguistics 1.

Rejected: using the full field string verbatim (7 chips for 7 claims, nearly all
singletons — the chip row would be longer than the list it filters).

### Progress bar is display-only; filters are a separate row

A proportional segmented bar with a count legend sits at the top, replacing the
`tracked / still open / review due` stats row. It is **not** clickable — status
filtering lives in the filter row instead, so there is one control per job.

The bar recomputes as filters are applied, so it reads as the state of the slice
currently in view, showing `N of M claims` when a filter is active. Discipline
chip counts stay corpus-level (static) — they label the corpus, not the slice.

The filter row has three independent, AND-ed controls: discipline chips, an
`outsider only` toggle, and a status `<select>`. The status dropdown is beyond
the original three asks; it is cheap and easily removed.

## Implementation

Inline vanilla JS plus `data-` attributes, preserving the zero-dependency,
single-output-file design.

- `build.py` stamps `data-discipline`, `data-outsider`, `data-bucket` on each
  `<article class="entry">`.
- ~60 lines of inline JS toggle the `hidden` attribute on cards and re-render
  the bar, legend, and count.
- **Progressive enhancement:** `build.py` emits the correct full-corpus bar and
  legend, and the filter row carries `hidden`, which JS removes on load. With JS
  disabled the page renders exactly as it does today plus a correct progress
  bar — never less useful than before.
- Stale claims get a `went stale` marker in the card header so the card list
  agrees with the bar (the status stamp still reads `unverified`).
- Accessibility: real `<button>`s with `aria-pressed`, a labelled `<select>`,
  `title` on bar segments, and an empty state when no claims match.

Rejected: pure CSS `:has()` + radios (three independent dimensions needs a
combinatorial selector explosion, and no live counts), and one static page per
filter combination (4 x 2 x 7 pages, no combined filtering).

### Build hazard

`PAGE` is rendered with `str.format`, so every literal brace in the template is
doubled. The new JS is brace-dense and doubling it by hand invites a `KeyError`
at build time. The script therefore lives in a separate `SCRIPT` constant passed
in as a `{script}` **value**, not embedded in the template — its braces are never
seen by `str.format`.

## Verification

- `python3 build.py` runs clean and still reports 7 claims.
- The six bucket counts sum to the claim total.
- Linear A is the only stale entry.
- The page still renders all cards with JavaScript disabled.
