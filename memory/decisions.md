# Decisions

- Use stdlib `argparse` for the first implementation cut to avoid dependency installation as a blocker.
- Keep `analyze`, `plan`, `charter`, and `document change` scaffolded until the core logic lands.
- Follow the local `.venv` setup pattern observed in `ia_ato-skill-ado-cli`.
- Add root `setup-skill.sh` as the preferred onboarding command after clone/download.
- Treat installation robustness as a maturity concern: detect host prerequisites, install into `.venv`, and never vendor binaries or compilers.
