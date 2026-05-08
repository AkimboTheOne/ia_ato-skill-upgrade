# Knowledge

- Baseline v0.2 treats `ato-skill-upgrade` as a support skill for the main coding agent.
- The skill helps think, plan, and document; it does not replace execution by the main agent.
- `document` mode documents only executed or verifiable changes.
- Local onboarding should expose a root `./setup-skill.sh` entrypoint.
- Setup must create or reuse `.venv` and avoid installing into global Python, preventing PEP 668 failures.
- Python dependencies are declared in `pyproject.toml`; system binaries and compilers are prerequisites, not repository contents.
- External review must be read-only and write outputs only into the active workspace repo.
- Productive maturity analysis uses category scores instead of a single flat checklist.
- `run --payload-file` is the machine-friendly surface for repeatable automation.
- Sample skill fixtures are the preferred way to test maturity and feature suggestions without depending on remote repos.
- Self-review is allowed only as dry-run with maximum depth 1.
- External review reports are detected evidence for documentation reconciliation.
- Maturity status should distinguish minor gaps from material failure.
- Schema validation is lightweight and dependency-free in this phase.
- v0.8 introduces CI and version consistency validation.
- Release readiness requires setup, validate, tests, maturity analysis, external review, changelog, memory, and synchronized version metadata.
