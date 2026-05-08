from __future__ import annotations

import json
from pathlib import Path

from ato_skill_upgrade.errors import SkillUpgradeError

from .context import build_capabilities, build_context
from .external_review import review_external
from .feature_fit_evaluator import evaluate_feature
from .maturity_evaluator import evaluate_maturity


def run_payload(workspace_repo: Path, payload_file: Path) -> dict:
    if not payload_file.exists():
        raise SkillUpgradeError(f"payload no encontrado: {payload_file}", 2)
    payload = json.loads(payload_file.read_text(encoding="utf-8"))
    operation = payload.get("operation", "")
    if not operation:
        raise SkillUpgradeError("payload requiere operation", 2)

    repo = _resolve_repo(workspace_repo, payload.get("repo", "."))
    if operation == "context":
        result = build_context(repo)
    elif operation == "capabilities":
        result = build_capabilities()
    elif operation == "analyze.maturity":
        result = evaluate_maturity(repo)
    elif operation == "analyze.feature":
        request = payload.get("request", "")
        if not request:
            raise SkillUpgradeError("analyze.feature requiere request", 6)
        result = evaluate_feature(repo, request)
    elif operation == "review.external":
        target = payload.get("repo_path", "")
        if not target:
            raise SkillUpgradeError("review.external requiere repo_path", 2)
        result = review_external(workspace_repo, Path(target).resolve(), read_only=bool(payload.get("read_only", True)))
    else:
        raise SkillUpgradeError(f"operation no soportada: {operation}", 6)

    return {"operation": operation, "result": result}


def _resolve_repo(workspace_repo: Path, repo_value: str) -> Path:
    repo = Path(repo_value)
    if not repo.is_absolute():
        repo = workspace_repo / repo
    return repo.resolve()

