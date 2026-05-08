from __future__ import annotations

from .repository_scanner import scan_repository


def evaluate_maturity(repo) -> dict:
    scan = scan_repository(repo)
    signals = scan["signals"]
    strengths = []
    gaps = []
    warnings = []

    required_strengths = {
        "readme": "Root README exists.",
        "skill_doc": "SKILL.md defines activation and operating role.",
        "agents_doc": "AGENTS.md gives coding-agent instructions.",
        "changelog": "CHANGELOG.md records baseline changes.",
        "pyproject": "Python package metadata exists.",
        "makefile": "Makefile exposes operational commands.",
        "memory": "Memory files preserve knowledge and decisions.",
        "harnesses": "Harnesses encode behavior and safety checks.",
        "examples": "Examples support human and machine invocation.",
        "validation_docs": "Validation documentation exists.",
        "security_docs": "Security documentation exists.",
    }
    for key, message in required_strengths.items():
        if signals.get(key):
            strengths.append(message)
        else:
            gaps.append(f"Missing or incomplete: {message}")

    setup_checks = [
        ("root_setup_entrypoint", "Root setup-skill.sh provides a visible clone/download onboarding path."),
        ("local_venv_install", "Installer and docs use local .venv instead of global Python."),
        ("pep668_documented", "PEP 668 / externally managed Python is documented as an onboarding concern."),
        ("dependency_boundary_documented", "Dependency boundary is documented: Python packages in pyproject.toml, system binaries as host prerequisites."),
        ("install_script", "Install script exists."),
        ("setup_script", "Setup script exists."),
        ("doctor_script", "Doctor script exists."),
        ("local_setup_docs", "Local setup documentation exists."),
    ]
    setup_score = 0
    for key, message in setup_checks:
        if signals.get(key):
            setup_score += 1
            strengths.append(message)
        else:
            gaps.append(f"Setup maturity gap: {message}")

    if setup_score >= 6:
        strengths.append("Local setup is a maturity strength and should be proposed as a reusable pattern for target skills.")
    else:
        warnings.append("Local setup is not yet strong enough to present as a reusable maturity pattern.")

    if signals.get("document_change_harness") and signals.get("inline_iteration_harness"):
        strengths.append("v0.2 harnesses for document change and inline iteration are present.")
    else:
        gaps.append("v0.2 harnesses for document change and inline iteration should be present.")
    if signals.get("scope_inflation_terms", 0) >= 3:
        warnings.append("Possible scope inflation detected: platform/server/catalog/orchestrator language should be governed.")

    categories = build_maturity_matrix(signals)
    score = round(sum(item["score"] for item in categories.values()) / len(categories))
    status = classify_status(score, gaps, warnings)

    return {
        "mode": "maturity",
        "repo": scan["repo"],
        "status": status,
        "score": score,
        "categories": categories,
        "strengths": strengths,
        "gaps": gaps,
        "warnings": warnings,
        "signals": signals,
        "recommendations": [
            "Keep setup robustness as a first-class maturity check.",
            "Use generated reports, plans, charters, and document-change manifests as operational evidence.",
            "Use dry-run evidence before any documentation write.",
        ],
    }


def build_maturity_matrix(signals: dict) -> dict:
    return {
        "setup_onboarding": score_category(
            signals,
            ["root_setup_entrypoint", "local_venv_install", "pep668_documented", "dependency_boundary_documented", "install_script", "setup_script", "doctor_script"],
        ),
        "cli_surface": score_category(signals, ["pyproject", "makefile"]),
        "contracts_schemas": score_category(signals, ["contracts", "run_contracts"]),
        "tests": score_category(signals, ["tests"]),
        "docs": score_category(signals, ["readme", "skill_doc", "agents_doc", "validation_docs", "security_docs", "local_setup_docs"]),
        "memory": score_category(signals, ["memory"]),
        "harnesses": score_category(signals, ["harnesses", "document_change_harness", "inline_iteration_harness"]),
        "security_write_policy": score_category(signals, ["security_docs", "write_policy_docs"]),
        "evidence_exports": score_category(signals, ["examples", "contracts"]),
    }


def classify_status(score: int, gaps: list[str], warnings: list[str]) -> str:
    if score >= 95 and not warnings:
        if not gaps:
            return "ready-for-next-cut"
        if len(gaps) <= 2:
            return "ready-with-notes"
    if score >= 80 and len(gaps) <= 4 and not warnings:
        return "needs-minor-work"
    return "needs-work"


def score_category(signals: dict, keys: list[str]) -> dict:
    present = [key for key in keys if signals.get(key)]
    missing = [key for key in keys if not signals.get(key)]
    score = round((len(present) / len(keys)) * 100) if keys else 0
    return {"score": score, "present": present, "missing": missing}


def render_maturity_report(report: dict) -> str:
    return _render_report("Maturity Report", report)


def _list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items) if items else "- None"


def _render_report(title: str, report: dict) -> str:
    return (
        f"# {title}\n\n"
        f"- Mode: {report['mode']}\n"
        f"- Status: {report['status']}\n"
        f"- Score: {report['score']}\n\n"
        "## Categories\n\n"
        f"{_render_categories(report.get('categories', {}))}\n\n"
        "## Strengths\n\n"
        f"{_list(report['strengths'])}\n\n"
        "## Gaps\n\n"
        f"{_list(report['gaps'])}\n\n"
        "## Warnings\n\n"
        f"{_list(report['warnings'])}\n\n"
        "## Recommendations\n\n"
        f"{_list(report['recommendations'])}\n"
    )


def _render_categories(categories: dict) -> str:
    if not categories:
        return "- None"
    return "\n".join(f"- {name}: {data['score']}" for name, data in categories.items())
