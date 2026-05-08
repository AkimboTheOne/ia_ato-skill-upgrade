# ato-skill-upgrade

`ato-skill-upgrade` is a Python CLI skill activated by `@skill-upgrade`.
It supports coding agents that need to evaluate, plan, and document controlled upgrades to existing skills.

This repository implements baseline `v0.2` as a core CLI skill with three modes:

- `maturity`: diagnose gaps and plan stabilization toward v1.0.
- `feature`: evaluate whether a requested capability fits the current skill.
- `document`: reconcile documentation, memory, and harnesses after an executed change.

## Quickstart

```bash
./setup-skill.sh
source .venv/bin/activate
ato-skill-upgrade context --json
ato-skill-upgrade validate --format json
```

Equivalent flows:

```bash
make setup
./scripts/setup.sh --with-tests
make install
```

## Local Setup Policy

The skill declares Python dependencies in `pyproject.toml`, but system binaries, compilers, and package managers are not part of this repository.
`make install` and `./setup-skill.sh` create or reuse a local `.venv` and install only into that environment.

This avoids PEP 668 `externally-managed-environment` failures on Homebrew or OS-managed Python installations.
If a required binary such as `make` or `python>=3.11` is missing, setup prints an OS package manager hint instead of vendoring or compiling it.

## Guardrails

- Dry-run is the default posture.
- Documentation writes require `--write --yes`.
- `document` mode does not modify code, tests, scripts, schemas, contracts, or build files.
- Post-execution documentation requires evidence from a plan, summary, manifest, diff, or validation report.

## Current Capability

Implemented:

- context discovery and capability reporting,
- structure validation and doctor checks,
- natural language request classification,
- inline iteration session creation,
- external read-only skill review,
- maturity analysis,
- feature-fit analysis,
- maturity and feature plans,
- maturity and feature charters,
- document-change dry-run reconciliation with evidence classification, preview, manifest, and validation report.
- machine-friendly `run --payload-file` contracts.
- guarded self-review for dry-run documentation planning.

The local setup pattern is intentionally part of maturity knowledge: a downloaded skill should expose `./setup-skill.sh`, install into `.venv`, avoid global Python writes, and document the boundary between declared Python dependencies and host binaries.

External read-only review can evaluate another local skill repository without modifying it:

```bash
ato-skill-upgrade review external --repo-path /path/to/skill --read-only --json
```

Machine invocation:

```bash
ato-skill-upgrade run --payload-file examples/inputs/run-context.json --json
```

Guarded self-review:

```bash
ato-skill-upgrade document change --review-report exports/skill-upgrade/external-review/external-review-report.json --self-review --json
```
