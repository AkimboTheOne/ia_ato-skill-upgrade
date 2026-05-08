# Validation

Run:

```bash
./setup-skill.sh
make test
ato-skill-upgrade doctor --json
ato-skill-upgrade validate --format json
```

Validation checks the expected baseline files and directories.
`make test` compiles Python sources and runs the stdlib unittest suite.
