from __future__ import annotations

import difflib
import fnmatch
import json
from datetime import datetime, timezone
from pathlib import Path

from ato_skill_upgrade.errors import SkillUpgradeError


ALLOWED_FILES = [
    "README.md",
    "SKILL.md",
    "AGENTS.md",
    "CHANGELOG.md",
    "docs/**",
    "memory/**",
    "harnesses/**",
]
DENIED_PREFIXES = ("cli/", "src/", "services/", "server/", "mcp/", "contracts/", "schemas/", "tests/", "scripts/")
DENIED_FILES = {"pyproject.toml", "Makefile"}


def document_change(
    repo: Path,
    plan: str = "",
    summary: str = "",
    manifest: str = "",
    diff: str = "",
    write: bool = False,
    yes: bool = False,
) -> dict:
    evidence = collect_evidence(repo, plan, summary, manifest, diff)
    if not any(evidence[key] for key in ["detected", "reported", "inferred"]):
        raise SkillUpgradeError("evidencia insuficiente para documentar", 10)
    if write and not yes:
        raise SkillUpgradeError("la escritura documental requiere --write --yes", 11)

    updates = build_updates(evidence)
    ensure_allowed_updates(updates)
    preview = build_preview(repo, updates)
    out_dir = repo / "exports" / "skill-upgrade" / "documentation"
    out_dir.mkdir(parents=True, exist_ok=True)
    preview_path = out_dir / "documentation-diff-preview.md"
    plan_path = out_dir / "documentation-update-plan.md"
    manifest_path = out_dir / "documentation-update-manifest.json"
    validation_path = out_dir / "documentation-validation-report.json"
    updated_manifest_path = out_dir / "updated-files-manifest.json"

    plan_doc = render_documentation_plan(updates, evidence)
    preview_path.write_text(preview, encoding="utf-8")
    plan_path.write_text(plan_doc, encoding="utf-8")

    files_updated: list[str] = []
    if write:
        for rel_path, append_text in updates.items():
            target = repo / rel_path
            original = target.read_text(encoding="utf-8") if target.exists() else ""
            if append_text.strip() not in original:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(original.rstrip() + "\n\n" + append_text.strip() + "\n", encoding="utf-8")
                files_updated.append(rel_path)

    manifest_data = {
        "mode": "document",
        "repo": str(repo),
        "inputs": {
            "plan": plan,
            "summary": summary,
            "manifest": manifest,
            "diff": diff,
        },
        "evidence_status": evidence,
        "files_planned": sorted(updates),
        "files_updated": files_updated,
        "write_enabled": write,
        "dry_run": not write,
        "risks": [],
        "warnings": [] if write else ["dry-run only; no files were modified"],
        "acceptance": [
            "Evidence was classified.",
            "Preview was generated before write.",
            "Only allowed documentation, memory, and harness files are targeted.",
        ],
    }
    manifest_path.write_text(json.dumps(manifest_data, indent=2, ensure_ascii=False), encoding="utf-8")
    validation_path.write_text(json.dumps({"status": "ok", "blocked_files": [], "allowed_files": sorted(updates)}, indent=2), encoding="utf-8")
    updated_manifest_path.write_text(json.dumps({"files_updated": files_updated}, indent=2), encoding="utf-8")
    manifest_data["outputs"] = {
        "documentation_update_plan": str(plan_path),
        "documentation_diff_preview": str(preview_path),
        "documentation_update_manifest": str(manifest_path),
        "documentation_validation_report": str(validation_path),
        "updated_files_manifest": str(updated_manifest_path),
    }
    return manifest_data


def collect_evidence(repo: Path, plan: str, summary: str, manifest: str, diff: str) -> dict:
    evidence = {"detected": [], "reported": [], "inferred": [], "pending": []}
    for label, rel in [("plan", plan), ("summary", summary), ("manifest", manifest), ("diff", diff)]:
        if not rel:
            evidence["pending"].append(f"{label} not provided")
            continue
        path = Path(rel)
        if not path.is_absolute():
            path = repo / path
        if path.exists():
            target = "detected" if label in {"manifest", "diff"} else "reported"
            evidence[target].append(f"{label}: {path}")
        else:
            evidence["pending"].append(f"{label} missing: {path}")
    if evidence["reported"] or evidence["detected"]:
        evidence["inferred"].append("Documentation reconciliation is allowed because at least one evidence source exists.")
    return evidence


def build_updates(evidence: dict) -> dict[str, str]:
    timestamp = datetime.now(timezone.utc).isoformat()
    evidence_lines = "\n".join(f"- {item}" for items in evidence.values() for item in items)
    return {
        "CHANGELOG.md": (
            f"## Documentation Reconciliation - {timestamp}\n\n"
            "Recorded a post-execution documentation reconciliation based on provided evidence.\n"
        ),
        "memory/iteration-history.md": (
            f"## Documentation Reconciliation - {timestamp}\n\n"
            "Evidence reviewed:\n\n"
            f"{evidence_lines}\n"
        ),
        "memory/knowledge.md": (
            "## Documentation Knowledge Update\n\n"
            "- Document mode must classify evidence as detected, reported, inferred, or pending before proposing writes.\n"
            "- Setup robustness remains a maturity strength when local onboarding evidence exists.\n"
        ),
        "harnesses/document-change-checks.md": (
            "## Runtime Checks\n\n"
            "- Documentation reconciliation must generate preview, manifest, and validation report.\n"
            "- Writes require `--write --yes` and must target allowed documentation paths only.\n"
        ),
    }


def ensure_allowed_updates(updates: dict[str, str]) -> None:
    blocked = []
    for rel_path in updates:
        if rel_path in DENIED_FILES or rel_path.startswith(DENIED_PREFIXES):
            blocked.append(rel_path)
            continue
        if not any(fnmatch.fnmatch(rel_path, pattern) for pattern in ALLOWED_FILES):
            blocked.append(rel_path)
    if blocked:
        raise SkillUpgradeError(f"escritura bloqueada por politica: {', '.join(blocked)}", 11)


def build_preview(repo: Path, updates: dict[str, str]) -> str:
    sections = ["# Documentation Diff Preview\n"]
    for rel_path, append_text in updates.items():
        target = repo / rel_path
        old = target.read_text(encoding="utf-8").splitlines(keepends=True) if target.exists() else []
        new_text = (target.read_text(encoding="utf-8") if target.exists() else "").rstrip() + "\n\n" + append_text.strip() + "\n"
        new = new_text.splitlines(keepends=True)
        diff = "".join(difflib.unified_diff(old, new, fromfile=f"a/{rel_path}", tofile=f"b/{rel_path}"))
        sections.append(f"## {rel_path}\n\n```diff\n{diff}```\n")
    return "\n".join(sections)


def render_documentation_plan(updates: dict[str, str], evidence: dict) -> str:
    files = "\n".join(f"- {path}" for path in sorted(updates))
    evidence_lines = "\n".join(f"- {bucket}: {item}" for bucket, items in evidence.items() for item in items)
    return (
        "# Documentation Update Plan\n\n"
        "## Evidence\n\n"
        f"{evidence_lines}\n\n"
        "## Files Planned\n\n"
        f"{files}\n"
    )

