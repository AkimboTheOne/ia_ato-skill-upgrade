from __future__ import annotations

from pathlib import Path

from .natural_language import classify_request
from .repository_scanner import scan_repository


def evaluate_feature(repo: Path, request: str) -> dict:
    scan = scan_repository(repo)
    signals = scan["signals"]
    classification = classify_request(request)
    strengths = []
    risks = []
    decision = "accepted-for-charter"

    lower = request.lower()
    if "setup" in lower or "instal" in lower or ".venv" in lower or "pep 668" in lower:
        if all(signals.get(key) for key in ["root_setup_entrypoint", "local_venv_install", "dependency_boundary_documented"]):
            strengths.append("The repository already contains the local setup maturity pattern required for this feature.")
            strengths.append("The feature fits as a maturity reusable pattern, not as unrelated runtime behavior.")
        else:
            risks.append("Setup feature is relevant but current repository lacks full onboarding signals.")
    if classification["status"] == "ambiguous":
        decision = "needs-clarification"
        risks.append(classification["question"])

    if "mcp" in lower or "https" in lower or "server" in lower:
        decision = "postpone"
        risks.append("Network, HTTPS, MCP, or server behavior is outside baseline v0.2.")

    if not strengths:
        strengths.append("Feature request can be evaluated against atomicity, evidence, and documentation guardrails.")

    return {
        "mode": "feature",
        "repo": str(repo),
        "request": request,
        "decision": decision,
        "fit": decision in {"accepted-for-charter", "needs-clarification"},
        "strengths": strengths,
        "risks": risks,
        "classification": classification,
        "atomicity": "preserved" if decision != "postpone" else "at-risk",
        "recommendations": [
            "Keep setup/onboarding improvements in maturity knowledge, docs, and harnesses.",
            "Require a charter before implementation when the feature changes behavior.",
            "Separate out-of-scope platform behavior into a future skill or roadmap item.",
        ],
    }


def render_feature_report(report: dict) -> str:
    def list_items(items: list[str]) -> str:
        return "\n".join(f"- {item}" for item in items) if items else "- None"

    return (
        "# Feature Fit Report\n\n"
        f"- Decision: {report['decision']}\n"
        f"- Atomicity: {report['atomicity']}\n\n"
        "## Request\n\n"
        f"{report['request']}\n\n"
        "## Strengths\n\n"
        f"{list_items(report['strengths'])}\n\n"
        "## Risks\n\n"
        f"{list_items(report['risks'])}\n\n"
        "## Recommendations\n\n"
        f"{list_items(report['recommendations'])}\n"
    )

