# rsrch Research Harness — v4

## Roles

| Role | Model | Does |
|---|---|---|
| Orchestrator | sonnet | Reads goal, decomposes, spawns agents, updates state |
| Researcher | haiku | One subquestion → one fact block |
| Synthesizer | sonnet | Fact blocks → output |

---

## Startup

1. Read `GOAL.md`.
2. Read `STATE.md` if it exists.
3. If answerable from training with high confidence → answer directly. No files changed.
4. Otherwise → decompose and spawn.

---

## Decompose

Break the goal into subquestions. Each must be:
- Answerable by one concrete fact, number, name, or condition
- Independent of other subquestions
- Necessary — output is incomplete without it

No hard cap. Cluster if more than 8.

Spawn all independent Researchers in parallel. Dependent ones sequentially.

Handoff to each Researcher:
```
Role: Researcher
Project: /absolute/path/
Subquestion: [exact text]
Source ID: S[N]
Fact block: facts/S[N].md
```

---

## Researcher protocol

1. Invoke `smart-search` skill to form queries.
2. Search → fetch → extract. Stop at first A/B source. Max 3 fetches.
3. Write fact block to `facts/S[N].md`.
4. Return one line: `Done. facts/S[N].md — answered: yes|partial|no`

Do not read other fact blocks. Do not synthesize across subquestions.

### Source grades

- **A** — primary: official docs, original paper, law, dataset, transcript
- **B** — strong secondary: academic review, specialist publication with citations
- **C** — noise: SEO, blogs, aggregators, LLM output

C sources guide discovery only — never use as evidence.

### Search tiers (stop at first A/B source)

| # | Method | When |
|---|---|---|
| 1 | PubMed MCP `search_articles` + `get_full_text_article` | Scientific/medical topics |
| 2 | `web_search` + `web_fetch` best result | All other topics |
| 3 | PMC full text via curl if PMCID found | Academic, open access |
| 4 | No A/B source found | Write `answered: no`, note where to look |

At tier 4: do not fill from training knowledge.

---

## Fact block format

```markdown
---
id: S[N]
subquestion: [exact text]
answered: yes | partial | no
---

## Answer

[Specific facts only — numbers, names, dates, conditions. One paragraph.]

## Source

- Title:
- URL:
- Quality: A | B | C

## Key quote

> [Exact quote if available]

## Gaps

[What's missing and where to look. Empty if fully covered.]
```

---

## Synthesizer protocol

Input: `GOAL.md` + all fact blocks listed by Orchestrator.

1. Draft output using only what's in fact blocks.
   - `answered: no` → insert `[NOT VERIFIED — source needed]`
   - `answered: partial` → use what's there, note the gap inline
2. Before finalizing: for every factual claim in the draft, confirm it has a supporting fact block. Remove or flag any that don't.
3. Append **Sources** section: all cited IDs with title + URL.
4. Write to `outputs/[filename].md`.

---

## Completion

Update `STATE.md`. Tell the user which files changed.
