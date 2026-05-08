from __future__ import annotations


MATURITY_HINTS = ("madurez", "maturity", "v1", "v1.0", "diagnost", "brecha", "estabil")
FEATURE_HINTS = ("feature", "mejora", "capacidad", "agregar", "incorporar", "charter")
DOCUMENT_HINTS = ("document", "readme", "changelog", "memoria", "harness", "diff", "ejecutado")


def classify_request(text: str) -> dict:
    normalized = text.lower()
    if "no se si" in normalized or "no sé si" in normalized or "feature o madurez" in normalized or "madurez o feature" in normalized:
        return {
            "status": "ambiguous",
            "mode": "auto",
            "question": "Deseas operar en modo maturity, feature o document?",
            "scores": {"maturity": 0, "feature": 0, "document": 0},
        }
    scores = {
        "maturity": sum(1 for hint in MATURITY_HINTS if hint in normalized),
        "feature": sum(1 for hint in FEATURE_HINTS if hint in normalized),
        "document": sum(1 for hint in DOCUMENT_HINTS if hint in normalized),
    }
    mode = max(scores, key=scores.get)
    if scores[mode] == 0:
        return {
            "status": "ambiguous",
            "mode": "auto",
            "question": "Deseas operar en modo maturity, feature o document?",
            "scores": scores,
        }
    tied = [key for key, value in scores.items() if value == scores[mode]]
    if len(tied) > 1:
        return {
            "status": "ambiguous",
            "mode": "auto",
            "question": "La solicitud mezcla modos. Confirma maturity, feature o document.",
            "scores": scores,
        }
    return {
        "status": "classified",
        "mode": mode,
        "scores": scores,
    }
