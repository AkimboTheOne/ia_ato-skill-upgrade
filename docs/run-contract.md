# Run Contract

`run` provides a machine-friendly execution surface.

```bash
ato-skill-upgrade run --payload-file examples/inputs/run-context.json --json
```

Supported operations:

- `context`
- `capabilities`
- `analyze.maturity`
- `analyze.feature`
- `review.external`

Schemas:

- `contracts/run.request.schema.json`
- `contracts/run.response.schema.json`

