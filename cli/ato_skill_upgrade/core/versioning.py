from __future__ import annotations

import re
from pathlib import Path

from ato_skill_upgrade import __version__


def read_pyproject_version(repo: Path) -> str:
    text = (repo / "pyproject.toml").read_text(encoding="utf-8")
    match = re.search(r'^version\s*=\s*"([^"]+)"', text, flags=re.MULTILINE)
    return match.group(1) if match else ""


def validate_version(repo: Path) -> dict:
    pyproject_version = read_pyproject_version(repo)
    status = "ok" if pyproject_version == __version__ else "error"
    return {
        "status": status,
        "package_version": __version__,
        "pyproject_version": pyproject_version,
    }

