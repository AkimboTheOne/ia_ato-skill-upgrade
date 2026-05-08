# Maturity Model

Maturity analysis checks structure, documentation, safety, examples, memory, harnesses, and local setup.

The product maturity matrix uses these categories:

- setup/onboarding,
- CLI surface,
- contracts/schemas,
- tests,
- docs,
- memory,
- harnesses,
- security/write policy,
- evidence/exports.

Status levels:

- `ready-for-next-cut`: high score, no gaps or warnings.
- `ready-with-notes`: high score with at most minor gaps.
- `needs-minor-work`: acceptable score with limited gaps.
- `needs-work`: material gaps or warnings.

Local setup is a first-class maturity signal when:

- `setup-skill.sh` exists at repository root,
- setup creates or reuses `.venv`,
- global Python installation is avoided,
- PEP 668 is documented,
- Python dependencies are declared in `pyproject.toml`,
- system binaries and compilers are host prerequisites.

The setup pattern is reported as a strength and should be proposed when evaluating other skills.
