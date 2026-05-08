# Release Notes v0.8.1

`ato-skill-upgrade` reaches a cleaned-up patch release focused on repository consistency.

## Highlights

- Canonical Spanish terminology for durable memory definitions.
- Baseline memory scaffold aligned with documented CLI paths.
- Corrected feature-refine example path in the PO baseline document.
- Package metadata synchronized to `0.8.1`.

## Validation

Release checks:

```bash
./setup-skill.sh
make validate
make test
```

Current expected result:

- version: `0.8.1`
- tests: passing

## Notes

- This release is a documentation and consistency patch.
- No runtime behavior change was introduced in the CLI surface.
