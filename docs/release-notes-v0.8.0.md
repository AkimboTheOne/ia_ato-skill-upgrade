# Release Notes v0.8.0

`ato-skill-upgrade` reaches a solid pre-productive `v0.8.0` state.

## Highlights

- Local setup through `./setup-skill.sh` and `.venv`.
- Maturity analysis with category scoring.
- Feature-fit analysis and charter/plan generation.
- Read-only external skill review.
- Machine-friendly `run --payload-file` contracts.
- Document reconciliation with evidence classification and dry-run previews.
- Self-review guardrails that block writes and cap recursion depth.
- Synthetic sample skill fixtures for repeatable tests.
- Lightweight schema and version validation.
- GitHub Actions CI.

## Validation

Release checks:

```bash
./setup-skill.sh
make validate
make test
ato-skill-upgrade analyze maturity --json
ato-skill-upgrade review external --repo-path examples/sample-skills/mature-skill --read-only --json
```

Current expected result:

- version: `0.8.0`
- tests: `12`
- mature fixture status: `ready-for-next-cut`
- local repo maturity status: `ready-for-next-cut`

## Known Limits

- GitHub-hosted CI still needs to run after pushing this release.
- External review currently supports local paths, not direct remote clone orchestration.
- Charter generation is useful but still generic for domain-specific features; refined charters may need human review.

