# Self Review

Self-review is a controlled inception workflow.

Rules:

- maximum depth is `1`,
- `--write` is blocked,
- a manifest or review report should be provided as evidence,
- outputs are generated in dry-run mode only.

Example:

```bash
ato-skill-upgrade document change \
  --review-report exports/skill-upgrade/external-review/external-review-report.json \
  --self-review \
  --max-depth 1 \
  --json
```

