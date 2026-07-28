#!/usr/bin/env bash
set -euo pipefail

version="$(python3 - <<'PY'
try:
    import tomllib
except ModuleNotFoundError:
    import toml as tomllib

with open("pyproject.toml", "r", encoding="utf-8") as handle:
    print(tomllib.loads(handle.read())["project"]["version"])
PY
)"

python3 -m build
python3 -m twine check "dist/torbot-${version}"*
if [[ "${1:-}" == "--upload" ]]; then
    python3 -m twine upload "dist/torbot-${version}"*
else
    echo "Publishing is ready. Run the following when you have your PyPI token:"
    echo "python3 -m twine upload dist/torbot-${version}*"
    echo "Or run: scripts/publish.sh --upload"
fi
