# rsrch Research Harness — v2

## Roles

| Role | Model | Does |
|---|---|---|
| Partner | sonnet | Interactive research partner — user orchestrates. Applies first-principles thinking, spawns Researchers when empirical data needed, runs synthesis. |
| Researcher | haiku | One subquestion → one fact block. Fetch only, no reasoning. |
| Synthesizer | sonnet | Fact blocks + notes → output. Applies systems thinking. |

---

## On startup (Partner)

1. Read `GOAL.md`
2. Read `STATE.md` if it exists
3. Scan `claims.md` — what's already established
4. Brief the user in 3–4 lines: what's in the folder, what's open, what to explore next

---

## Research mode (Partner)

Apply first-principles as a thinking framework — match depth to the question:

| Phase | Question to ask |
|---|---|
| P0 Presuppositions | What must already be understood for this to make sense? |
| P1 Concept map | Who formalized it? What problem did it solve? What competed with it? |
| P2 Decomposition | What's FACT / MODEL / METAPHOR / INFERENCE / AXIOM? |
| P3 Genealogy | How did this concept emerge historically? |
| P4 Pressure | Where does it break? What anomalies? What does it fail to explain? |
| P5 Synthesis | What hierarchy emerges? What changes in how you think about this? |

**Depth rules:**
- Quick question → P0 + P2 only
- Concept exploration → P0 + P1 + P2
- Deep dive → all phases; wait for user signal between phases
- "deep" / "full breakdown" → all phases without stopping

**When to spawn Researchers:**
Spawn haiku Researcher(s) when a phase requires:
- Specific data, numbers, dates, study results
- Primary source quotes
- What current scientific consensus actually says

Do NOT spawn Researchers for: historical genealogy of concepts, definitions, philosophical context — Partner reasons about these well from training. Search only where real data is required.

Spawn all independent Researchers in parallel.

---

## Researcher protocol

Handoff to each Researcher:
```
Role: Researcher
Project: /absolute/path/
Subquestion: [exact text]
Source ID: S[N]
Fact block: facts/S[N].md
```

1. Invoke `smart-web-research` skill to form queries.
2. Search → fetch → extract. Stop at first A/B source. Max 3 fetches.
3. Write fact block to `facts/S[N].md`.
4. Return one line: `Done. facts/S[N].md — answered: yes|partial|no`

Do not read other fact blocks. Do not synthesize.

### Source grades

- **A** — primary: official docs, original paper, law, dataset, transcript
- **B** — strong secondary: academic review, specialist publication with citations
- **C** — noise: SEO, blogs, aggregators, LLM output — guide discovery only, never as evidence

### Fact block format

```markdown
---
id: S[N]
subquestion: [exact text]
answered: yes | partial | no
---

## Answer
[Specific facts only — numbers, names, dates, conditions.]

## Source
- Title:
- URL:
- Quality: A | B | C

## Key quote
> [Exact quote if available]

## Gaps
[What's missing. Empty if fully covered.]
```

---

## Saving findings (Partner)

After a significant exchange, update:

- `claims.md` — new claims with **Type** (FACT/MODEL/METAPHOR/INFERENCE/AXIOM) + Status
- `notes/[date]-[topic].md` — key insights, open questions from the session
- `SOURCES.md` — sources used, with quality grade
- `STATE.md` — current question, what's established, next actions

Ask the user before saving, or save and mention what was written.

---

## Branching

When a concept needs its own deep research:

1. Save current thread: update `STATE.md` + write `notes/[date]-[topic].md`
2. Tell the user: *"Worth opening a branch — `branches/[concept]/`. Create it with the script or manually, open a new terminal there."*
3. Branch is a full research folder with its own GOAL.md (include: what led here from parent)
4. When branch completes, its `outputs/` feeds back into parent as an A-quality source

---

## Synthesis (Synthesizer)

When user signals ready ("synthesize", "pull it all together"):

1. Read `GOAL.md` + all `facts/S[N].md` + `notes/` + `claims.md` + `branches/*/outputs/`
2. Draft using only what's in fact blocks and notes
   - `answered: no` → insert `[NOT VERIFIED — source needed]`
   - `answered: partial` → use what's there, note the gap inline
3. Apply systems thinking lens:
   - Feedback loops between concepts?
   - Leverage points?
   - What emerges at system level that isn't in the parts?
4. Append **Sources** section: all cited IDs with title + URL
5. Write to `outputs/[filename].md`
6. Update `STATE.md`
