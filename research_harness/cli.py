"""Console entrypoint for installed usage."""
from __future__ import annotations

import runpy
from pathlib import Path


def main() -> None:
    script = Path(__file__).resolve().parents[1] / "scripts" / "new-research.py"
    runpy.run_path(str(script), run_name="__main__")
