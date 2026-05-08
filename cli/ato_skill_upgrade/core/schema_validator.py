from __future__ import annotations

import json
from pathlib import Path


def validate_json_schemas(repo: Path) -> dict:
    contracts = repo / "contracts"
    results = []
    if not contracts.exists():
        return {"status": "error", "schemas": [], "errors": ["contracts directory missing"]}

    for path in sorted(contracts.glob("*.json")):
        errors = []
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            results.append({"schema": path.name, "status": "error", "errors": [str(exc)]})
            continue
        if "$schema" not in data:
            errors.append("missing $schema")
        if "title" not in data:
            errors.append("missing title")
        if data.get("type") != "object":
            errors.append("top-level type should be object")
        results.append({"schema": path.name, "status": "ok" if not errors else "error", "errors": errors})

    status = "ok" if results and all(item["status"] == "ok" for item in results) else "error"
    return {"status": status, "schemas": results, "errors": [err for item in results for err in item["errors"]]}

