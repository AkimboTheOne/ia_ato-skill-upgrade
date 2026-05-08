from __future__ import annotations


def classify_recommendations(report: dict) -> list[dict]:
    recommendations: list[dict] = []
    for item in report.get("strengths", []):
        recommendations.append({"type": "strength", "message": item})
    for item in report.get("gaps", []):
        recommendations.append({"type": "maturity_gap", "message": item})
    for item in report.get("warnings", []):
        recommendations.append({"type": "postpone", "message": item})

    signals = report.get("signals", {})
    if signals.get("root_setup_entrypoint") and signals.get("local_venv_install"):
        recommendations.append(
            {
                "type": "feature_candidate",
                "message": "Promote local setup onboarding as a reusable maturity feature for other skills.",
            }
        )
    if signals.get("contracts") and signals.get("tests"):
        recommendations.append(
            {
                "type": "feature_candidate",
                "message": "Use contracts and tests as machine-checkable readiness evidence.",
            }
        )
    return recommendations


def split_recommendations(items: list[dict]) -> tuple[list[dict], list[dict]]:
    maturity = [item for item in items if item["type"] in {"strength", "maturity_gap", "postpone"}]
    features = [item for item in items if item["type"] in {"feature_candidate", "out_of_scope"}]
    return maturity, features

