# Local Setup

Recommended first command after cloning or downloading the skill:

```bash
./setup-skill.sh
```

The setup flow:

1. Resolves a Python interpreter compatible with `python>=3.11`.
2. Verifies `make` is available.
3. Creates or reuses `.venv`.
4. Installs the local CLI into `.venv`.
5. Bootstraps `.env` and `config.yaml` from tracked examples.
6. Runs `doctor`.
7. Runs validation and compile checks when `--with-tests` is used.

The setup flow never installs into the global Python environment.

## PEP 668

PEP 668 marks some Python installations as externally managed.
This skill avoids that failure mode by using `.venv` for local installation.

## Binaries

Missing binaries are reported as host prerequisites.
They are intentionally not committed to the repo.

