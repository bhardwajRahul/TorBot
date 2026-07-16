import os
import sys

import toml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from main import run as run_cli, set_arguments  # noqa: E402


def main() -> None:
    """Run the TorBot CLI from an installed entry point."""
    arg_parser = set_arguments()
    config_file_path = os.path.join(REPO_ROOT, "pyproject.toml")
    try:
        with open(config_file_path, "r", encoding="utf-8") as handle:
            data = toml.load(handle)
            version = data["project"]["version"]
    except Exception as exc:
        raise RuntimeError("unable to find version from pyproject.toml.") from exc

    run_cli(arg_parser, version)


if __name__ == "__main__":
    main()
