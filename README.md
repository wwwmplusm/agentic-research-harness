# Agentic Research Harness

A filesystem-first research workflow for AI agents — built around first-principles thinking and multi-agent fact retrieval.

## Core idea

```text
one research topic = one folder
user orchestrates — AI goes deep on what you ask
haiku agents fetch facts, sonnet reasons about them
filesystem is the memory — chats are disposable
```

## Why this exists

AI-assisted research usually fails because agents:

- search from vague prompts
- trust search snippets
- mix raw sources with conclusions
- lose context between fresh chats
- cannot show which claim came from which source
- treat models and metaphors as facts

This harness gives the AI a strict research structure and a thinking framework — so it goes deep, stays epistemically honest, and survives across sessions.

## How it works

Three roles, user-driven:

| Role | Model | Does |
|---|---|---|
| **Partner** | sonnet | Interactive. Reads folder context, applies first-principles reasoning, spawns Researchers when empirical data is needed. |
| **Researcher** | haiku | Fetches one fact per subquestion. Writes a structured fact block. No synthesis. |
| **Synthesizer** | sonnet | Pulls all facts + notes into a final output. Applies systems thinking. |

You steer the research. The Partner follows your questions, not a preset plan.

## Thinking frameworks

### First-principles (research structure)

Each question is explored through relevant phases:

| Phase | Question |
|---|---|
| P0 Presuppositions | What must already be understood? |
| P1 Concept map | Who formalized it, what problem did it solve, what competed with it? |
| P2 Decomposition | What's FACT / MODEL / METAPHOR / INFERENCE / AXIOM? |
| P3 Genealogy | How did this concept emerge historically? |
| P4 Pressure | Where does it break? What anomalies exist? |
| P5 Synthesis | What hierarchy emerges? What changes in your thinking? |

Depth matches the question — quick asks get P0+P2, deep dives get all phases.

### Systems thinking (synthesis lens)

Applied during synthesis across accumulated knowledge:
- What are the feedback loops between concepts?
- Where are the leverage points?
- What properties emerge at system level that aren't in the parts?

## Quickstart

```bash
git clone https://github.com/wwwmplusm/agentic-research-harness.git
cd agentic-research-harness
python scripts/new-research.py "my research topic"
cd research/my-research-topic
$EDITOR GOAL.md
claude  # or hermes / codex
```

The script creates:

```text
research/my-research-topic/
├── GOAL.md          — why, main question, context, desired output, quality bar
├── STATE.md         — current state, working hypotheses, open questions, systems view
├── SOURCES.md       — source index with quality grades A/B/C
├── claims.md        — claims with type (FACT/MODEL/METAPHOR) and verification status
├── sources/         — saved source files
├── facts/           — fact blocks from Researcher agents
├── notes/           — session notes and personal insights
├── outputs/         — finished synthesis
├── claudes/         — saved chat contexts
└── branches/        — sub-researches on adjacent concepts
```

## Non-linear research

Research is not a linear process. You can branch mid-session:

```text
researching motivation
→ encounter neurons at P1
→ open branches/neurons/ via the script
→ new terminal, new session — full first-principles dive on neurons
→ branches/neurons/outputs/ feeds back as an A-source into motivation research
```

Each branch is a complete research folder. The parent reads its output when synthesizing.

## Claim types

`claims.md` tracks not just verification status but the epistemic type of each claim:

| Type | Meaning |
|---|---|
| `FACT` | Empirically observed, reproducible, tied to a primary source |
| `MODEL` | Simplification of reality — useful but incomplete, breaks at edges |
| `METAPHOR` | Analogy used in explanation — not a mechanism |
| `INFERENCE` | Derived from premises — list the premises |
| `AXIOM` | Accepted as given by a specific community |

## Source quality

- **A — primary:** official docs, original paper, law, dataset, transcript, original book
- **B — strong secondary:** textbook, academic review, expert article with citations
- **C — discovery/noise:** SEO, blogs, aggregators, LLM output

Rules: C sources guide discovery only. A claim cannot be `verified` from a snippet. Chase primary sources or mark a gap.

## Workflow

```text
1.  Create a research project.
2.  Fill in GOAL.md.
3.  Start an AI agent from the project folder.
4.  Ask it questions — it applies first-principles reasoning.
5.  It spawns haiku Researchers when real data is needed.
6.  Findings go into claims.md and notes/.
7.  When a concept needs its own deep dive → open a branch.
8.  When you have enough → ask it to synthesize.
9.  Start a fresh chat whenever context gets too big.
```

## Repository layout

```text
agentic-research-harness/
├── README.md
├── CLAUDE.md          — agent instructions (Claude Code)
├── AGENTS.md          — agent instructions (generic)
├── HERMES.md          — agent instructions (Hermes)
├── scripts/
│   └── new-research.py
├── templates/
│   └── research/      — file templates copied into each project
├── research/          — your local projects (gitignored)
├── docs/
└── examples/
```

## Works with

- Claude Code
- Hermes Agent
- OpenAI Codex CLI
- Any terminal agent that can read/write files and search the web

The harness is tool-agnostic. Swap the agent, keep the structure.

## Privacy

The `research/` directory is gitignored by default. Commit templates and docs — not private sources or chat transcripts.

## License

MIT
