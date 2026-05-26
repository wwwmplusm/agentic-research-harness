# Agentic Research Harness

A filesystem-first research workflow for AI agents.

Most AI research workflows treat chat as the workspace. This harness treats the filesystem as the workspace. The chat can be thrown away; the research survives in structured files.

Core idea:

```text
one research question = one folder
goal first
sources separate from synthesis
claims tied to evidence
state updated after each session
AI chats are disposable; files are the memory
```

## Why this exists

AI-assisted research usually fails because agents:

- search from vague prompts;
- trust search snippets;
- use secondary summaries instead of primary sources;
- mix raw source material with conclusions;
- lose context between fresh chats;
- cannot show which claim came from which source.

This repo gives agents a small but strict research harness: project folders, source indexes, claim ledgers, saved source texts, and session state.

## Quickstart

```bash
git clone https://github.com/YOUR-USER/agentic-research-harness.git
cd agentic-research-harness
python scripts/new-research.py "my research topic"
cd research/my-research-topic
$EDITOR GOAL.md
hermes
# or: claude
# or: codex
```

The script creates:

```text
research/my-research-topic/
├── GOAL.md
├── STATE.md
├── SOURCES.md
├── claims.md
├── sources/
├── notes/
├── outputs/
└── claudes/
```

## How to use with an AI agent

Launch the agent from inside a research project folder:

```bash
cd research/my-research-topic
hermes
```

Then ask it to continue the research. The agent instructions in `AGENTS.md`, `CLAUDE.md`, and `HERMES.md` tell compatible agents to:

1. Read `GOAL.md`.
2. Read `STATE.md`.
3. Use `SOURCES.md` and `claims.md` when factual claims or source work are involved.
4. Search by decomposed subquestions, not by raw prompt only.
5. Prefer primary sources.
6. Save important source text into `sources/` before using it as evidence.
7. Update `SOURCES.md` and `claims.md`.
8. Write synthesis into `notes/` or `outputs/`.
9. Update `STATE.md` before finishing.

## Project file roles

| File/folder | Purpose |
|---|---|
| `GOAL.md` | Why the research exists, main question, context, desired output, quality bar. |
| `STATE.md` | Current understanding, open questions, source gaps, next actions. Read this at session start. |
| `SOURCES.md` | Index of sources with quality grade, read status, saved file path, and URL. |
| `claims.md` | Important claims mapped to evidence source IDs and confidence. |
| `sources/` | Preserved source texts, extracts, PDFs, transcripts, raw markdown. Not synthesis. |
| `notes/` | Intermediate notes, subquestion analysis, working synthesis. |
| `outputs/` | Finished artifacts: report, essay, post, guide, skill, decision memo, plan. |
| `claudes/` | Optional cold storage for important AI-session transcripts or saved answers. |

## Source quality ladder

- **A — primary source:** official docs, law, government page, original paper, dataset, original report, transcript, original book/chapter.
- **B — strong secondary source:** textbook, academic review, expert article with citations, reputable publication.
- **C — discovery/noise:** SEO pages, generic blogs, unsourced summaries, weak aggregators, LLM output.

Rules:

- Search snippets are discovery only; they are not evidence.
- C sources can guide discovery but should not support final claims.
- A claim cannot be `verified` if the only evidence is a snippet.
- If a secondary source makes an important claim, chase the primary source or mark a source gap.

## Repository layout

```text
agentic-research-harness/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── HERMES.md
├── docs/
├── examples/
├── research/              # your local research projects; gitignored except .gitkeep
├── scripts/
└── templates/
```

## Recommended workflow

```text
1. Create a research project.
2. Fill in GOAL.md.
3. Start an AI agent from the project folder.
4. Ask it to make a small research plan.
5. Search and save sources.
6. Update SOURCES.md.
7. Convert important findings into claims.md.
8. Write synthesis in notes/ or outputs/.
9. Update STATE.md.
10. Start a fresh chat whenever context gets too big.
```

## Works with

Any agent or research process that can read/write files and search the web:

- Hermes Agent
- Claude Code
- OpenAI Codex CLI
- other terminal agents
- Brave Search MCP
- Parallel Search
- manual browser research

The harness is deliberately tool-agnostic.

## Privacy warning

Do not publish your real research folders by accident. The `research/` directory is gitignored by default. Commit templates, examples, and docs — not private sources or chat transcripts.

## License

MIT
