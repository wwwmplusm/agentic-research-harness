# Claims Ledger

`claims.md` prevents the final output from silently smuggling weak assumptions into strong claims.

Recommended statuses:

- `verified`: supported by a primary source or 2+ independent A/B sources.
- `plausible`: some support, but not enough for strong wording.
- `contested`: sources disagree.
- `source_gap`: claim found, but primary source not found or inaccessible.
- `discarded`: weak/false; should not be used.

Final outputs should not present `plausible` or `source_gap` claims as certain facts.
