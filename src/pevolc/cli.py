"""Command-line interface entry points."""

from __future__ import annotations

import argparse
from pathlib import Path

from pevolc.pipelines.compute_entropy import run_from_config as run_entropy
from pevolc.pipelines.train_forecaster import run_training

def main(argv: list[str] | None = None) -> int:
    """Dispatch CLI commands for entropy computation and model training."""

    parser = argparse.ArgumentParser(description="Permutation entropy eruption forecasting")
    parser.add_argument("command", choices=["compute-entropy", "train"], help="Action to run")
    parser.add_argument("config", type=Path, help="Path to configuration file")
    args = parser.parse_args(argv)

    if args.command == "compute-entropy":
        run_entropy(args.config)
    elif args.command == "train":
        run_training(args.config)
    else:  # pragma: no cover - guarded by argparse
        raise ValueError(f"Unknown command {args.command}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
