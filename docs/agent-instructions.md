# Agent Instructions

Use the root instruction files depending on your agent:

- `AGENTS.md` — generic terminal agents / Codex-style agents.
- `CLAUDE.md` — Claude Code.
- `HERMES.md` — Hermes Agent.

Copy the relevant file into a research workspace if your agent only reads local project instructions.

The important behavior is always the same:

1. Start from `GOAL.md` and `STATE.md`.
2. Do not trust snippets.
3. Save source text before using it as evidence.
4. Update source and claim indexes.
5. Leave the project continuable.
