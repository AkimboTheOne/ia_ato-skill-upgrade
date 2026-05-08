from __future__ import annotations

from pathlib import Path

from .feature_fit_evaluator import evaluate_feature
from .maturity_evaluator import evaluate_maturity


def generate_plan(repo: Path, mode: str, request: str = "") -> dict:
    if mode == "maturity":
        report = evaluate_maturity(repo)
        steps = [
            "Preserve local setup maturity as a reusable strength.",
            "Close structural and documentation gaps reported by maturity analysis.",
            "Implement evidence-producing commands before broadening scope.",
            "Run doctor, validate, and compile checks after changes.",
        ]
    else:
        report = evaluate_feature(repo, request)
        steps = [
            "Confirm request scope and atomicity.",
            "Record assumptions and risks.",
            "Implement only the accepted behavior.",
            "Update docs, memory, harnesses, and changelog after execution with evidence.",
        ]
    return {
        "mode": mode,
        "repo": str(repo),
        "source_status": report.get("status") or report.get("decision"),
        "steps": steps,
        "acceptance": [
            "Outputs include Markdown and JSON evidence.",
            "Dry-run remains default for documentation changes.",
            "Setup maturity signals remain detected as strengths.",
        ],
        "risks": report.get("warnings", []) + report.get("risks", []),
    }


def generate_charter(repo: Path, mode: str, request: str = "") -> dict:
    plan = generate_plan(repo, mode, request)
    return {
        "mode": mode,
        "repo": str(repo),
        "objective": "Controlled upgrade of a skill while preserving atomicity.",
        "scope": plan["steps"],
        "out_of_scope": [
            "Automatic code implementation by default.",
            "Commits, pushes, or pull requests.",
            "Network services, HTTPS, or MCP runtime in baseline v0.2.",
            "Vendoring system binaries or compilers.",
        ],
        "acceptance": plan["acceptance"],
        "risks": plan["risks"],
    }


def render_plan(plan: dict) -> str:
    return _render("Upgrade Plan", plan, "steps")


def render_charter(charter: dict) -> str:
    return _render("Upgrade Charter", charter, "scope")


def _items(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items) if items else "- None"


def _render(title: str, data: dict, scope_key: str) -> str:
    return (
        f"# {title}\n\n"
        f"- Mode: {data['mode']}\n"
        f"- Repo: {data['repo']}\n\n"
        f"## {'Steps' if scope_key == 'steps' else 'Scope'}\n\n"
        f"{_items(data[scope_key])}\n\n"
        "## Acceptance\n\n"
        f"{_items(data['acceptance'])}\n\n"
        "## Risks\n\n"
        f"{_items(data['risks'])}\n"
    )

