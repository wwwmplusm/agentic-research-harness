# Workflow

## 1. Create project

```bash
python scripts/new-research.py "topic name"
```

## 2. Fill `GOAL.md`

Define:

- why this matters;
- the main question;
- relevant context;
- desired output;
- quality bar.

## 3. Start an agent in the project folder

```bash
cd research/topic-name
hermes
```

## 4. Research in loops

Use short loops:

1. subquestion;
2. search;
3. source save;
4. source index;
5. claim update;
6. notes update (`notes/` — agent writes here, not `outputs/`);
7. state update.

## 5. End every substantial session with state

`STATE.md` should let a fresh agent continue without reading the entire history.
