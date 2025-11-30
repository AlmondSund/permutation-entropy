"""Train a forecasting model from the command line."""

from __future__ import annotations

import argparse

from pevolc.pipelines.train_forecaster import run_training


def main() -> None:
    parser = argparse.ArgumentParser(description="Train PE-based eruption forecasting model.")
    parser.add_argument("config", help="Path to YAML configuration file.")
    args = parser.parse_args()
    run_training(args.config)


if __name__ == "__main__":
    main()
