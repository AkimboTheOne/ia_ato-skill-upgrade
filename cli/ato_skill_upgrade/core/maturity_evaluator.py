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

    score_total = 100
    score = max(0, score_total - (len(gaps) * 6) - (len(warnings) * 2))
    status = "ready-for-next-cut" if score >= 80 else "needs-work"

    return {
        "mode": "maturity",
        "repo": scan["repo"],
        "status": status,
        "score": score,
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
        "## Strengths\n\n"
        f"{_list(report['strengths'])}\n\n"
        "## Gaps\n\n"
        f"{_list(report['gaps'])}\n\n"
        "## Warnings\n\n"
        f"{_list(report['warnings'])}\n\n"
        "## Recommendations\n\n"
        f"{_list(report['recommendations'])}\n"
    )
