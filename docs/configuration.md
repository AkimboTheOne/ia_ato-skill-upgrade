# Configuration

Local configuration files are created by:

```bash
make bootstrap
```

Generated local files:

- `.env`
- `config.yaml`

Tracked templates:

- `.env.example`
- `config.example.yaml`

## Dependency Boundary

Python package dependencies belong in `pyproject.toml`.
System binaries and compilers do not belong in the repository.

Setup scripts may check for required tools and provide installation hints, but they must not vendor binaries, commit generated virtual environments, or assume writes to the global Python installation.

