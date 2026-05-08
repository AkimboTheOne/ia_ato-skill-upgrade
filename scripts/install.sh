#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${ROOT_DIR}/.venv"
cd "${ROOT_DIR}"

info() { echo "[INFO] $*"; }
warn() { echo "[WARN] $*"; }
err() { echo "[ERROR] $*" >&2; }

has_cmd() {
  command -v "$1" >/dev/null 2>&1
}

resolve_python() {
  local candidates=(
    "${PYTHON:-}"
    python3.13
    python3.12
    python3.11
    python3
  )
  local candidate
  for candidate in "${candidates[@]}"; do
    if [ -n "${candidate}" ] && has_cmd "${candidate}" && "${candidate}" -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 11) else 1)'; then
      echo "${candidate}"
      return 0
    fi
  done
  return 1
}

install_hint() {
  local package="$1"
  if has_cmd brew; then
    echo "Try: brew install ${package}"
  else
    echo "Install '${package}' with your OS package manager."
  fi
}

if ! has_cmd make; then
  err "make is required but was not found."
  err "$(install_hint make)"
  exit 1
fi

if ! PYTHON_BIN="$(resolve_python)"; then
  found_version="not-found"
  if has_cmd python3; then
    found_version="$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
  fi
  err "python>=3.11 is required. Found python3=${found_version}."
  err "$(install_hint python)"
  exit 1
fi

PYTHON_VERSION="$("${PYTHON_BIN}" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
info "Using ${PYTHON_BIN} (version ${PYTHON_VERSION})"

if [ -d "${VENV_DIR}" ]; then
  info "Reusing virtual environment at ${VENV_DIR}"
else
  info "Creating virtual environment at ${VENV_DIR}"
  "${PYTHON_BIN}" -m venv "${VENV_DIR}"
fi

VENV_PYTHON="${VENV_DIR}/bin/python"
VENV_CLI="${VENV_DIR}/bin/ato-skill-upgrade"
VENV_VERSION="$("${VENV_PYTHON}" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
if ! "${VENV_PYTHON}" -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 11) else 1)'; then
  err "Existing .venv uses python ${VENV_VERSION}, but python>=3.11 is required."
  err "Remove .venv and rerun ./setup-skill.sh after installing a compatible Python."
  exit 1
fi
info "Using virtual environment Python ${VENV_VERSION}"

DEPENDENCY_COUNT="$("${VENV_PYTHON}" - <<'PY'
import sys
try:
    import tomllib
except ModuleNotFoundError:
    print("0")
    raise SystemExit(0)
from pathlib import Path
data = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))
print(len(data.get("project", {}).get("dependencies", [])))
PY
)"

if [ "${DEPENDENCY_COUNT}" -gt 0 ]; then
  info "Installing declared Python dependencies inside .venv"
  "${VENV_PYTHON}" -m pip install -e "${ROOT_DIR}"
else
  info "No third-party Python dependencies declared; installing local CLI shim"
fi

SITE_PACKAGES="$("${VENV_PYTHON}" -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')"
mkdir -p "${SITE_PACKAGES}"
printf '%s\n' "${ROOT_DIR}/cli" > "${SITE_PACKAGES}/ato_skill_upgrade_local.pth"

cat > "${VENV_CLI}" <<EOF
#!/usr/bin/env bash
set -euo pipefail
PYTHONPATH="${ROOT_DIR}/cli\${PYTHONPATH:+:\${PYTHONPATH}}" exec "${VENV_PYTHON}" -m ato_skill_upgrade.main "\$@"
EOF
chmod +x "${VENV_CLI}"

info "Install completed."
info "Use '. .venv/bin/activate' to activate the environment."
