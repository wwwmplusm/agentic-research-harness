# Hermes Research Harness

This directory contains research projects. Each child folder under `research/` is one research project.

When Hermes is launched from a project folder, treat the current working directory as the active research project.

## Startup protocol

1. Identify the current project folder with `pwd`.
2. Read `GOAL.md`.
3. Read `STATE.md` if it exists.
4. Read `SOURCES.md` and `claims.md` only when the task involves research, factual claims, source work, or continuing previous work.
5. Do not read all files in `sources/`, `claudes/`, `notes/`, or `outputs/` by default. Use indexes first, then open specific files.

## Research quality rules

- Search results and snippets are discovery only; they are not evidence.
- Prefer primary sources over summaries.
- For every important A/B source, fetch and save the full available text or the best available extract into `sources/` before using it as evidence.
- Every saved source must have a source ID, URL, accessed date, read status, extraction method, and quality grade.
- If full text cannot be retrieved, mark the source honestly as `partial`, `abstract_only`, `snippet_only`, or `inaccessible`.
- Do not mark a claim as verified if its evidence is only a search snippet or LLM-generated summary.
- If a source is secondary, chase its citation to the primary source or mark the claim as `source_gap`.

## Completion protocol

Before finishing a research session:

1. Update `STATE.md` with what changed and the next step.
2. Update `SOURCES.md` if sources were found or read.
3. Update `claims.md` if important factual claims were made.
4. Tell the user exactly which files changed.

If the task was only conceptual discussion and no files changed, say so explicitly.
