#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/.venv/bin/activate"

echo "Iniciando Orange Canvas..."
python -m Orange.canvas "$@"
