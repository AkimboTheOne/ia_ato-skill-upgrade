#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CLI="${ROOT_DIR}/.venv/bin/ato-skill-upgrade"

if [ -x "${CLI}" ]; then
  "${CLI}" doctor --json
else
  echo "[FAIL] CLI not installed at ${CLI}. Run 'make install'." >&2
  exit 1
fi

