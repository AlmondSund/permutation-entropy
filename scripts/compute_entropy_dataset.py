"""Compute entropy features for a dataset from the command line."""

from __future__ import annotations

import argparse

from pevolc.pipelines.compute_entropy import run_from_config


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute PE/MPE/WPE features from seismic data.")
    parser.add_argument("config", help="Path to YAML configuration file.")
    args = parser.parse_args()
    run_from_config(args.config)


if __name__ == "__main__":
    main()
