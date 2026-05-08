#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUN_TESTS=0

usage() {
  cat <<'EOF'
Usage: ./scripts/setup.sh [options]

Options:
  --with-tests   Run validation and bytecode checks after install
  -h, --help     Show this help
EOF
}

for arg in "$@"; do
  case "${arg}" in
    --with-tests) RUN_TESTS=1 ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "[ERROR] Unknown option: ${arg}" >&2
      usage
      exit 2
      ;;
  esac
done

echo "[STEP] Install local package"
"${ROOT_DIR}/scripts/install.sh"

echo "[STEP] Bootstrap local config"
make -C "${ROOT_DIR}" bootstrap

echo "[STEP] Run doctor"
"${ROOT_DIR}/scripts/doctor.sh"

if [ "${RUN_TESTS}" -eq 1 ]; then
  echo "[STEP] Run validation"
  "${ROOT_DIR}/.venv/bin/ato-skill-upgrade" validate --format json
  echo "[STEP] Compile Python sources"
  "${ROOT_DIR}/.venv/bin/python" -m compileall -q "${ROOT_DIR}/cli"
  echo "[STEP] Run unit tests"
  PYTHONPATH="${ROOT_DIR}/cli" "${ROOT_DIR}/.venv/bin/python" -m unittest discover -s "${ROOT_DIR}/tests" -q
fi

echo "[DONE] Setup completed"
