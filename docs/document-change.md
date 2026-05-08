# Document Change

`document change` reconciles documentation after an executed change.

The mode requires evidence and defaults to dry-run.
Write behavior requires `--write --yes` and is limited to documentation, memory, and harness files.

Dry-run outputs:

- `documentation-update-plan.md`
- `documentation-diff-preview.md`
- `documentation-update-manifest.json`
- `documentation-validation-report.json`
- `updated-files-manifest.json`

External review reports can be used as evidence:

```bash
ato-skill-upgrade document change --review-report exports/skill-upgrade/external-review/external-review-report.json --json
```

Self-review blocks writes and caps recursion depth at `1`.
