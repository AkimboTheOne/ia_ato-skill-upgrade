from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from ato_skill_upgrade.errors import SkillUpgradeError

from .maturity_evaluator import evaluate_maturity, render_maturity_report
from .outputs import write_json, write_text
from .recommendations import classify_recommendations, split_recommendations
from .repository_scanner import scan_repository


def review_external(workspace_repo: Path, target_repo: Path, read_only: bool = True) -> dict:
    if not read_only:
        raise SkillUpgradeError("external review requiere --read-only en v0.3", 11)
    if not target_repo.exists() or not target_repo.is_dir():
        raise SkillUpgradeError(f"repo objetivo no encontrado: {target_repo}", 3)

    report = evaluate_maturity(target_repo)
    scan = scan_repository(target_repo)
    recommendations = classify_recommendations(report)
    maturity_items, feature_items = split_recommendations(recommendations)

    out_dir = workspace_repo / "exports" / "skill-upgrade" / "external-review"
    out_dir.mkdir(parents=True, exist_ok=True)
    report_md = out_dir / "external-review-report.md"
    report_json = out_dir / "external-review-report.json"
    read_manifest = out_dir / "read-manifest.json"
    maturity_md = out_dir / "maturity-suggestions.md"
    feature_md = out_dir / "feature-suggestions.md"

    payload = {
        "mode": "external-review",
        "read_only": True,
        "target_repo": str(target_repo),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "maturity": report,
        "recommendations": recommendations,
        "outputs": {
            "external_review_report_md": str(report_md),
            "external_review_report_json": str(report_json),
            "read_manifest": str(read_manifest),
            "maturity_suggestions": str(maturity_md),
            "feature_suggestions": str(feature_md),
        },
    }
    manifest = {
        "mode": "external-review",
        "read_only": True,
        "target_repo": str(target_repo),
        "files_read": scan["files"],
        "sensitive_files_skipped": [".env"],
        "writes_performed": [],
    }

    write_text(report_md, render_maturity_report(report))
    write_json(report_json, payload)
    write_json(read_manifest, manifest)
    write_text(maturity_md, render_suggestions("Maturity Suggestions", maturity_items))
    write_text(feature_md, render_suggestions("Feature Suggestions", feature_items))
    return payload


def render_suggestions(title: str, items: list[dict]) -> str:
    lines = [f"# {title}", ""]
    if not items:
        lines.append("- None")
    for item in items:
        lines.append(f"- `{item['type']}`: {item['message']}")
    lines.append("")
    return "\n".join(lines)

