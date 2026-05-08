# Maturity Checks

- Root documentation exists.
- CLI entrypoint exists.
- Validation command exists.
- Security guardrails are documented.
- Examples and harnesses are present.
- Root `setup-skill.sh` exists for clone/download onboarding.
- Installation uses local `.venv` instead of global Python.
- Missing system binaries are treated as host prerequisites, not vendored repo contents.
- External review produces category scores, not only a flat pass/fail result.
- Run contracts should be present before declaring machine-readiness.
- High score with small gaps should be reported as `ready-with-notes`, not a hard failure.
- Release governance and CI are required before calling the skill v0.8-ready.
