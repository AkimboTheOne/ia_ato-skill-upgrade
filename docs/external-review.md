# External Review

External review evaluates another skill repository in read-only mode.

```bash
ato-skill-upgrade review external --repo-path /path/to/skill --read-only --json
```

The workspace repository receives the outputs under `exports/skill-upgrade/external-review/`.
The target repository is never modified.

Outputs:

- `external-review-report.md`
- `external-review-report.json`
- `read-manifest.json`
- `maturity-suggestions.md`
- `feature-suggestions.md`

