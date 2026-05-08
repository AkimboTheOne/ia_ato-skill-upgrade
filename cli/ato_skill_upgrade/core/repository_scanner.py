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
        "contracts": any(path.startswith("contracts/") and path.endswith(".json") for path in files),
        "tests": any(path.startswith("tests/") and path.endswith(".py") for path in files),
        "run_contracts": "contracts/run.request.schema.json" in files and "contracts/run.response.schema.json" in files,
        "write_policy_docs": "write_policy" in combined or "write policy" in combined or "--write" in combined,
        "cache_behavior": "cache" in combined or "ttl" in combined,
        "scope_inflation_terms": count_scope_inflation(content_index),
    }


def count_scope_inflation(content_index: dict[str, str]) -> int:
    scope_text = "\n".join(
        text
        for path, text in content_index.items()
        if path in {"README.md", "SKILL.md", "AGENTS.md"}
    ).lower()
    relevant_lines = []
    for line in scope_text.splitlines():
        if any(marker in line for marker in ["out of scope", "fuera de alcance", "blocked", "forbidden", "bloqueado"]):
            continue
        relevant_lines.append(line)
    filtered = "\n".join(relevant_lines)
    return sum(1 for term in ["platform", "https", "mcp", "catalog", "orchestrator"] if term in filtered)
