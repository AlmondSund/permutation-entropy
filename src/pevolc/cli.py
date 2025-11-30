"""Command-line interface entry points."""

from __future__ import annotations

import argparse
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    """Dispatch CLI commands for entropy computation and model training."""

    parser = argparse.ArgumentParser(description="Permutation entropy eruption forecasting")
    parser.add_argument("command", choices=["compute-entropy", "train"], help="Action to run")
    parser.add_argument("config", type=Path, help="Path to configuration file")
    args = parser.parse_args(argv)

    raise NotImplementedError(f"Command '{args.command}' not implemented yet")


if __name__ == "__main__":
    raise SystemExit(main())
