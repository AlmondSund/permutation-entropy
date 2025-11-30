"""Run a small hyperparameter sweep over entropy parameters and models."""

from __future__ import annotations

import itertools
import tempfile
from pathlib import Path

import pandas as pd
import yaml

from pevolc.pipelines.compute_entropy import compute_entropy_dataset
from pevolc.pipelines.train_forecaster import run_training


def main() -> None:
    grid_path = Path("configs/experiment_grid.yaml")
    with open(grid_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    base = cfg.get("base", {})
    data_glob = base.get("data_glob", "data/raw/*.npy")
    paths = [Path(p) for p in Path().glob(data_glob)]
    if not paths:
        raise FileNotFoundError(f"No data files matched {data_glob}")

    orders = cfg.get("orders", [3])
    delays = cfg.get("delays", [1])
    scales_list = cfg.get("scales", [3])
    model_types = cfg.get("model_types", ["logreg"])
    results = []

    for order, delay, scales, model_type in itertools.product(orders, delays, scales_list, model_types):
        run_name = f"m{order}_tau{delay}_s{scales}_{model_type}"
        run_dir = Path("experiments") / "grid" / run_name
        run_dir.mkdir(parents=True, exist_ok=True)

        entropy_cfg = base | {
            "order": order,
            "delay": delay,
            "scales": scales,
            "output_path": str(run_dir / "features.csv"),
        }
        dataset = compute_entropy_dataset(paths, Path(entropy_cfg["output_path"]), entropy_cfg)

        train_cfg = {
            "dataset_path": entropy_cfg["output_path"],
            "label_column": base.get("label_column", "label"),
            "feature_columns": None,
            "model_type": model_type,
            "model_path": str(run_dir / "forecaster.joblib"),
            "metrics_path": str(run_dir / "metrics.csv"),
            "split": base.get("split", {"type": "time", "val_fraction": 0.2, "time_column": "start_s"}),
        }
        with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as tmp:
            yaml.safe_dump(train_cfg, tmp)
            tmp_path = Path(tmp.name)
        metrics = run_training(tmp_path)
        results.append({"run": run_name, **metrics})

    pd.DataFrame(results).to_csv(Path("experiments/grid/summary.csv"), index=False)
    print("Grid results written to experiments/grid/summary.csv")


if __name__ == "__main__":
    main()
