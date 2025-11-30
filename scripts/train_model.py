"""Train a forecasting model from the command line."""

from __future__ import annotations

import argparse
from pathlib import Path
import tempfile
import yaml

from pevolc.pipelines.train_forecaster import run_training


def main() -> None:
    parser = argparse.ArgumentParser(description="Train PE-based eruption forecasting model.")
    parser.add_argument("config", help="Path to YAML configuration file.")
    parser.add_argument("--time-split", action="store_true", help="Force time-ordered split.")
    parser.add_argument("--val-fraction", type=float, help="Override validation fraction.")
    args = parser.parse_args()
    cfg_path = Path(args.config)
    if args.time_split or args.val_fraction is not None:
        with open(cfg_path, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
        split = cfg.get("split", {})
        if args.time_split:
            split["type"] = "time"
        if args.val_fraction is not None:
            split["val_fraction"] = args.val_fraction
        cfg["split"] = split
        with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as tmp:
            yaml.safe_dump(cfg, tmp)
            cfg_path = Path(tmp.name)
    run_training(cfg_path)


if __name__ == "__main__":
    main()
