# AGENTS.md — Research Harness Instructions

This repository is a filesystem-first research harness. When working inside a child folder under `research/`, treat the current directory as the active research project.

## Startup protocol

Before answering or researching:

1. Identify the current directory.
2. If inside a research project, read `GOAL.md` first.
3. Read `STATE.md` if present.
4. Read `SOURCES.md` and `claims.md` only when the task involves factual claims, source work, or continuing previous research.
5. Do not bulk-read `sources/`, `claudes/`, `notes/`, or `outputs/` by default. Use indexes first, then open specific files.

## Research protocol

For substantial research:

1. Restate the active question.
2. Decompose it into subquestions.
3. Generate focused search queries for each subquestion.
4. Prefer primary sources over summaries.
5. Save important source text/extracts into `sources/` before using them as evidence.
6. Update `SOURCES.md` with source ID, URL, quality, read status, and saved file path.
7. Map important factual claims in `claims.md`.
8. Write synthesis into `notes/` or `outputs/`.
9. Update `STATE.md` with what changed, open questions, and next actions.

## Quality rules

- Search snippets are discovery only; they are not evidence.
- Do not mark a claim as verified if its only support is a snippet or LLM-generated summary.
- If a source is secondary, chase its citation to the primary source or mark `source_gap`.
- Keep raw sources separate from synthesis.
- Keep `STATE.md` compact enough to read at session start.

## Completion protocol

Before finishing a research session:

1. Update `STATE.md` unless the task was only a conceptual discussion.
2. Update `SOURCES.md` if sources were found/read.
3. Update `claims.md` if important factual claims were made.
4. Tell the user exactly which files changed.
