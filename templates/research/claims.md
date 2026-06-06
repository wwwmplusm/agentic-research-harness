# Claims

| ID | Claim | Type | Status | Evidence | Quote/file anchor | Confidence | Notes |
|---|---|---|---|---|---|---|---|

## Types

- **FACT** — empirically observed and reproducible; tied to a primary source
- **MODEL** — simplification of reality; useful but incomplete; breaks at edges
- **METAPHOR** — analogy used in explanation; not a mechanism; must not be treated as FACT
- **INFERENCE** — derived from premises; list the premises in Notes
- **AXIOM** — accepted as given by a specific community; note which community

## Status

- **verified** — supported by a primary source or 2+ independent A/B sources
- **plausible** — some support, but not enough for strong wording
- **contested** — sources disagree
- **source_gap** — claim found, but primary source not found or inaccessible
- **discarded** — weak/false; should not be used

## Rules

- A claim cannot be `verified` if evidence is only `snippet_only`.
- Important claims should point to source IDs from `SOURCES.md`.
- Final outputs must not present `plausible` or `source_gap` claims as certain facts.
- METAPHOR claims must never appear in outputs without being labelled as analogy.
