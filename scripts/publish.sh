#!/usr/bin/env bash
set -euo pipefail

python3 -m build
python3 -m twine check dist/*
echo "Publishing is ready. Run the following when you have your PyPI token:"
echo "python3 -m twine upload dist/*"
