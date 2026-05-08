from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from ato_skill_upgrade import __version__
from ato_skill_upgrade.core.charter_generator import generate_charter, generate_plan, render_charter, render_plan
from ato_skill_upgrade.core.context import build_capabilities, build_context, validate_structure
from ato_skill_upgrade.core.documentation_reconciler import document_change
from ato_skill_upgrade.core.feature_fit_evaluator import evaluate_feature, render_feature_report
from ato_skill_upgrade.core.iteration import create_session
from ato_skill_upgrade.core.maturity_evaluator import evaluate_maturity, render_maturity_report
from ato_skill_upgrade.core.natural_language import classify_request
from ato_skill_upgrade.core.outputs import output_paths, write_json, write_text
from ato_skill_upgrade.errors import SkillUpgradeError


def emit(data: object, as_json: bool = False) -> None:
    if as_json or isinstance(data, (dict, list)):
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return
    print(data)


def add_common_repo(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--repo", default=".", help="Target skill repository")


def cmd_context(args: argparse.Namespace) -> int:
    emit(build_context(Path(args.repo).resolve()), args.json)
    return 0


def cmd_capabilities(args: argparse.Namespace) -> int:
    emit(build_capabilities(), args.json)
    return 0


def cmd_usage(_: argparse.Namespace) -> int:
    emit("Use @skill-upgrade or ato-skill-upgrade <command>. Start with context, ask, iterate, analyze, plan, charter, or document change.")
    return 0


def cmd_examples(_: argparse.Namespace) -> int:
    emit({"examples": ["ato-skill-upgrade ask \"que le falta a este skill para v1.0\"", "ato-skill-upgrade iterate --repo . --mode auto --request request.md", "ato-skill-upgrade document change --repo . --plan plan.md --summary execution-summary.md --dry-run"]})
    return 0


def cmd_schema(args: argparse.Namespace) -> int:
    schema_dir = Path(args.repo).resolve() / "contracts"
    schemas = sorted(path.name for path in schema_dir.glob("*.json")) if schema_dir.exists() else []
    emit({"schemas": schemas, "status": "ok" if schemas else "warning"}, args.json)
    return 0


def cmd_doctor(args: argparse.Namespace) -> int:
    repo = Path(args.repo).resolve()
    structure = validate_structure(repo)
    data = {
        "status": "ok" if structure["status"] == "ok" else "warning",
        "version": __version__,
        "repo_exists": repo.exists(),
        "repo": str(repo),
        "structure": structure,
    }
    emit(data, args.json)
    return 0 if repo.exists() else 3


def cmd_validate(args: argparse.Namespace) -> int:
    result = validate_structure(Path(args.repo).resolve())
    emit(result, args.format == "json")
    return 0 if result["status"] == "ok" else 7


def cmd_ask(args: argparse.Namespace) -> int:
    emit(classify_request(args.prompt), args.json)
    return 0


def cmd_iterate(args: argparse.Namespace) -> int:
    request = args.text
    if args.request:
        request = Path(args.request).read_text(encoding="utf-8")
    if not request:
        raise SkillUpgradeError("iterate requiere --text o --request", 6)
    emit(create_session(Path(args.repo).resolve(), request, args.mode), args.json)
    return 0


def read_request(repo: Path, args: argparse.Namespace) -> str:
    if getattr(args, "request_text", ""):
        return args.request_text
    if getattr(args, "request", ""):
        path = Path(args.request)
        if not path.is_absolute():
            path = repo / path
        return path.read_text(encoding="utf-8")
    return ""


def cmd_analyze(args: argparse.Namespace) -> int:
    repo = Path(args.repo).resolve()
    if args.mode == "maturity":
        report = evaluate_maturity(repo)
        md = render_maturity_report(report)
        md_path, json_path = output_paths(repo, "reports", "maturity-report")
    elif args.mode == "feature":
        request = read_request(repo, args)
        if not request:
            raise SkillUpgradeError("analyze feature requiere --request o --request-text", 6)
        report = evaluate_feature(repo, request)
        md = render_feature_report(report)
        md_path, json_path = output_paths(repo, "reports", "feature-fit-report")
    else:
        raise SkillUpgradeError("modo invalido para analyze", 2)
    write_text(md_path, md)
    write_json(json_path, report)
    report["outputs"] = {"markdown": str(md_path), "json": str(json_path)}
    emit(report, args.json)
    return 0 if report.get("status", "ok") != "needs-work" else 7


def cmd_plan(args: argparse.Namespace) -> int:
    repo = Path(args.repo).resolve()
    request = read_request(repo, args)
    plan = generate_plan(repo, args.mode, request)
    md_path, json_path = output_paths(repo, "plans", f"{args.mode}-plan")
    write_text(md_path, render_plan(plan))
    write_json(json_path, plan)
    plan["outputs"] = {"markdown": str(md_path), "json": str(json_path)}
    emit(plan, args.json)
    return 0


def cmd_charter(args: argparse.Namespace) -> int:
    repo = Path(args.repo).resolve()
    request = read_request(repo, args)
    charter = generate_charter(repo, args.mode, request)
    md_path, json_path = output_paths(repo, "charters", f"{args.mode}-charter")
    write_text(md_path, render_charter(charter))
    write_json(json_path, charter)
    charter["outputs"] = {"markdown": str(md_path), "json": str(json_path)}
    emit(charter, args.json)
    return 0


def cmd_document_change(args: argparse.Namespace) -> int:
    repo = Path(args.repo).resolve()
    result = document_change(
        repo=repo,
        plan=args.plan,
        summary=args.summary,
        manifest=args.manifest,
        diff=args.diff,
        write=args.write,
        yes=args.yes,
    )
    emit(result, args.json)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ato-skill-upgrade", description="Controlled skill upgrade CLI")
    parser.add_argument("--version", action="version", version=__version__)
    sub = parser.add_subparsers(dest="command", required=True)

    for name, handler in [
        ("context", cmd_context),
        ("capabilities", cmd_capabilities),
        ("doctor", cmd_doctor),
    ]:
        p = sub.add_parser(name)
        add_common_repo(p)
        p.add_argument("--json", action="store_true")
        p.set_defaults(func=handler)

    p = sub.add_parser("validate")
    add_common_repo(p)
    p.add_argument("--format", choices=["text", "json"], default="text")
    p.set_defaults(func=cmd_validate)

    p = sub.add_parser("usage")
    p.set_defaults(func=cmd_usage)

    p = sub.add_parser("examples")
    p.set_defaults(func=cmd_examples)

    p = sub.add_parser("schema")
    add_common_repo(p)
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_schema)

    p = sub.add_parser("ask")
    p.add_argument("prompt")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_ask)

    p = sub.add_parser("iterate")
    add_common_repo(p)
    p.add_argument("--mode", choices=["auto", "maturity", "feature", "document"], default="auto")
    p.add_argument("--request", default="")
    p.add_argument("--text", default="")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_iterate)

    for name, handler in [("analyze", cmd_analyze), ("plan", cmd_plan), ("charter", cmd_charter)]:
        p = sub.add_parser(name)
        add_common_repo(p)
        p.add_argument("mode", choices=["maturity", "feature"])
        p.add_argument("--request", default="")
        p.add_argument("--request-text", default="")
        p.add_argument("--json", action="store_true")
        p.set_defaults(func=handler)

    document = sub.add_parser("document")
    document_sub = document.add_subparsers(dest="document_command", required=True)
    p = document_sub.add_parser("change")
    add_common_repo(p)
    p.add_argument("--plan", default="")
    p.add_argument("--summary", default="")
    p.add_argument("--manifest", default="")
    p.add_argument("--diff", default="")
    p.add_argument("--dry-run", action="store_true", default=True)
    p.add_argument("--write", action="store_true")
    p.add_argument("--yes", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_document_change)

    return parser


def run(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except SkillUpgradeError as exc:
        print(str(exc), file=sys.stderr)
        return exc.exit_code


def main() -> None:
    raise SystemExit(run())


if __name__ == "__main__":
    main()
