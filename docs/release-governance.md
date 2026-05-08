# Release Governance

Use semantic pre-release milestones for this skill.

Current practical target:

- `v0.7`: productive validation and scoring.
- `v0.8`: CI, release governance, and hardening.
- `v1.0`: stable CLI behavior after real-world usage against multiple skill repos.

Release checklist:

- `./setup-skill.sh`
- `make validate`
- `make test`
- `ato-skill-upgrade analyze maturity --json`
- `ato-skill-upgrade review external --repo-path examples/sample-skills/mature-skill --read-only --json`
- changelog updated,
- memory updated,
- version synchronized between `pyproject.toml` and `ato_skill_upgrade.__version__`.

