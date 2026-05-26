#!/usr/bin/env python3
"""Create a new research project folder with the standard research harness."""
from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESEARCH_DIR = ROOT / "research"
TEMPLATE = ROOT / "templates" / "research"


def slugify(text: str) -> str:
    text = text.strip().lower().replace(" ", "-")
    text = re.sub(r"[^a-z0-9._-]+", "-", text, flags=re.IGNORECASE)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "new-research"


def write_from_template(project: Path, template_name: str, target_name: str | None = None) -> None:
    target_name = target_name or template_name
    content = (TEMPLATE / template_name).read_text(encoding="utf-8")
    content = content.replace("YYYY-MM-DD", date.today().isoformat())
    (project / target_name).write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a new research project")
    parser.add_argument("name", help="Folder name / research topic")
    parser.add_argument("--root", type=Path, default=DEFAULT_RESEARCH_DIR, help="Research root directory")
    parser.add_argument("--goal", help="Initial GOAL.md context text", default="")
    parser.add_argument("--minimal", action="store_true", help="Only create GOAL.md and directories")
    args = parser.parse_args()

    research_root = args.root.expanduser().resolve()
    project = research_root / slugify(args.name)
    if project.exists():
        raise SystemExit(f"Project already exists: {project}")

    for directory in [project, project / "sources", project / "notes", project / "outputs", project / "claudes"]:
        directory.mkdir(parents=True, exist_ok=True)

    if args.goal:
        goal = (
            "# GOAL\n\n"
            "## Why / context\n\n"
            f"{args.goal.strip()}\n\n"
            "## Main question\n\n[Fill in]\n\n"
            "## Desired output\n\n[Fill in]\n\n"
            "## Quality bar\n\n[Fill in]\n"
        )
        (project / "GOAL.md").write_text(goal, encoding="utf-8")
    else:
        write_from_template(project, "GOAL.md")

    if not args.minimal:
        for name in ["STATE.md", "SOURCES.md", "claims.md", "RESEARCH_PROTOCOL.md"]:
            write_from_template(project, name)

    print(project)
    print("Next:")
    print(f"  cd {project}")
    print("  $EDITOR GOAL.md")
    print("  hermes  # or claude / codex")


if __name__ == "__main__":
    main()
