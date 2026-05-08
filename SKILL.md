# ato-skill-upgrade

Use this skill when a user asks to improve, mature, extend, or document changes to an existing skill repository.

## Activation

`@skill-upgrade`

Natural language activation is supported for:

- maturity assessment,
- feature fit evaluation,
- post-execution documentation.

## Operating Role

This skill supports the planner of the main coding agent. It does not replace the main agent and does not implement code changes by default.

## Modes

- `maturity`: evaluate readiness, gaps, risks, and v1.0 path.
- `feature`: determine if a capability belongs in the skill, needs reformulation, should be postponed, or should become a separate skill.
- `document`: update documentation, memory, and harnesses based only on executed or verifiable evidence.

## Maturity Strength

The skill treats robust local onboarding as a maturity feature:

- root `setup-skill.sh`,
- `.venv`-only install path,
- PEP 668 awareness,
- Python dependencies in `pyproject.toml`,
- host binaries and compilers outside the repository.

## Safety Rules

- Do not read outside the target repo without explicit authorization.
- Do not print secrets.
- Do not run arbitrary commands.
- Do not write by default.
- Do not modify code in `document` mode.
- Do not document unexecuted work as completed.
- Do not generate a final plan when critical ambiguity remains unresolved.
- Use the Spanish canonical memory terminology in `memory/terminology-es.md` when editing durable definitions or iteration history.
