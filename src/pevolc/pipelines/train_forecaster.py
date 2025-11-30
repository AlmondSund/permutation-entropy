"""Training pipeline for eruption forecasting models."""

from __future__ import annotations

from pathlib import Path
from typing import Sequence

import joblib
import pandas as pd
import yaml
from sklearn.metrics import average_precision_score, precision_recall_curve, roc_auc_score

from pevolc.models import PermutationEntropyForecaster, evaluate_auc


def _select_features(df: pd.DataFrame, feature_columns: Sequence[str] | None, label_column: str) -> pd.DataFrame:
    if feature_columns is None:
        # Auto-select numeric columns excluding the label
        feature_columns = [c for c in df.columns if c != label_column and pd.api.types.is_numeric_dtype(df[c])]
    return df[feature_columns]


def run_training(config_path: Path) -> dict:
    """Run the full training workflow using the provided config file."""

    with open(config_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    dataset_path = Path(cfg["dataset_path"])
    df = pd.read_csv(dataset_path)
    label_column = cfg.get("label_column", "label")
    if label_column not in df.columns:
        raise ValueError(f"Label column '{label_column}' not found in dataset")
    feature_columns = cfg.get("feature_columns")
    X = _select_features(df, feature_columns, label_column)
    y = df[label_column].astype(int)

    model_type = cfg.get("model_type", "logreg")
    forecaster = PermutationEntropyForecaster(model_type=model_type, calibrate=True)
    forecaster.fit(X, y)

    # Simple evaluation on training set (for prototype)
    probs = forecaster.predict_proba(X)
    metrics = {
        "roc_auc": float(roc_auc_score(y, probs)),
        "pr_auc": float(average_precision_score(y, probs)),
    }
    precision, recall, thresholds = precision_recall_curve(y, probs)
    eval_path = Path(cfg.get("metrics_path", "experiments/last_run/metrics.csv"))
    eval_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame({"precision": precision[:-1], "recall": recall[:-1], "threshold": thresholds}).to_csv(
        eval_path, index=False
    )

    model_path = Path(cfg.get("model_path", "experiments/last_run/forecaster.joblib"))
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(forecaster, model_path)

    return {"model_path": str(model_path), "metrics_path": str(eval_path), **metrics}
