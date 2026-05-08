from __future__ import annotations

from pathlib import Path

from ato_skill_upgrade import __version__


REQUIRED_FILES = ["README.md", "SKILL.md", "AGENTS.md", "CHANGELOG.md", "pyproject.toml", "setup-skill.sh"]
REQUIRED_DIRS = ["docs", "memory", "harnesses", "examples", "workspace", "exports", "contracts"]


def build_context(repo: Path) -> dict:
    return {
        "skill": "ato-skill-upgrade",
        "version": __version__,
        "activation": "@skill-upgrade",
        "baseline_mode": "A - Core CLI Skill",
        "repo": str(repo),
        "modes": ["maturity", "feature", "document"],
        "write_default": "dry-run",
        "workspace_dir": "workspace/skill-upgrade",
        "export_dir": "exports/skill-upgrade",
    }


def build_capabilities() -> dict:
    return {
        "modes": {
            "maturity": ["analyze", "plan", "charter"],
            "feature": ["analyze", "plan", "charter"],
            "document": ["document change", "preview", "manifest"],
        },
        "commands": [
            "context",
            "capabilities",
            "usage",
            "examples",
            "schema",
            "doctor",
            "validate",
            "ask",
            "iterate",
            "analyze",
            "plan",
            "charter",
            "document change",
        ],
        "guardrails": [
            "dry-run by default",
            "document writes require --write --yes",
            "document mode cannot modify code",
            "evidence is required for post-execution documentation",
            "local setup uses .venv and treats system binaries as host prerequisites",
        ],
    }


def validate_structure(repo: Path) -> dict:
    missing_files = [path for path in REQUIRED_FILES if not (repo / path).is_file()]
    missing_dirs = [path for path in REQUIRED_DIRS if not (repo / path).is_dir()]
    status = "ok" if not missing_files and not missing_dirs else "error"
    return {
        "status": status,
        "missing_files": missing_files,
        "missing_dirs": missing_dirs,
    }
