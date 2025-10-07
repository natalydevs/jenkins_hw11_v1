#!/usr/bin/env bash
set -euxo pipefail

python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# ключевая строка — добавляем корень проекта в путь
PYTHONPATH="$WORKSPACE" pytest -q
