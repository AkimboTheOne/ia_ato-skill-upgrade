from __future__ import annotations

from pathlib import Path


TEXT_EXTENSIONS = {".md", ".txt", ".yaml", ".yml", ".toml", ".sh", ".py", ".json"}
SENSITIVE_NAMES = {".env"}


def read_text_if_safe(path: Path, max_bytes: int = 256_000) -> str:
    if not path.is_file() or path.name in SENSITIVE_NAMES:
        return ""
    if path.suffix and path.suffix not in TEXT_EXTENSIONS:
        return ""
    if path.stat().st_size > max_bytes:
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def scan_repository(repo: Path) -> dict:
    files = {str(path.relative_to(repo)) for path in repo.rglob("*") if path.is_file() and ".git" not in path.parts and ".venv" not in path.parts}
    dirs = {str(path.relative_to(repo)) for path in repo.rglob("*") if path.is_dir() and ".git" not in path.parts and ".venv" not in path.parts}
    content_index = {}
    for rel in sorted(files):
        text = read_text_if_safe(repo / rel)
        if text:
            content_index[rel] = text

    return {
        "repo": str(repo),
        "files": sorted(files),
        "dirs": sorted(dirs),
        "content_index": content_index,
        "signals": detect_signals(files, content_index),
    }


def detect_signals(files: set[str], content_index: dict[str, str]) -> dict:
    combined = "\n".join(content_index.values()).lower()
    return {
        "root_setup_entrypoint": "setup-skill.sh" in files,
        "local_venv_install": ".venv" in combined,
        "pep668_documented": "pep 668" in combined or "externally-managed-environment" in combined,
        "dependency_boundary_documented": "system binaries" in combined and "pyproject.toml" in combined,
        "install_script": "scripts/install.sh" in files,
        "setup_script": "scripts/setup.sh" in files,
        "doctor_script": "scripts/doctor.sh" in files,
        "pyproject": "pyproject.toml" in files,
        "makefile": "Makefile" in files,
        "skill_doc": "SKILL.md" in files,
        "readme": "README.md" in files,
        "agents_doc": "AGENTS.md" in files,
        "changelog": "CHANGELOG.md" in files,
        "memory": any(path.startswith("memory/") for path in files),
        "harnesses": any(path.startswith("harnesses/") for path in files),
        "examples": any(path.startswith("examples/") for path in files),
        "document_change_harness": "harnesses/document-change-checks.md" in files,
        "inline_iteration_harness": "harnesses/inline-iteration-checks.md" in files,
        "validation_docs": "docs/validation.md" in files,
        "security_docs": "docs/security.md" in files,
        "local_setup_docs": "docs/local-setup.md" in files,
    }

