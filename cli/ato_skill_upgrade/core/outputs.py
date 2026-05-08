from __future__ import annotations

import json
from pathlib import Path


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def output_paths(repo: Path, kind: str, stem: str) -> tuple[Path, Path]:
    base = repo / "exports" / "skill-upgrade" / kind
    return base / f"{stem}.md", base / f"{stem}.json"

