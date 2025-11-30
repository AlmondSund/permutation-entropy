"""Training pipeline for eruption forecasting models."""

from __future__ import annotations

from pathlib import Path
from typing import Sequence

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yaml
from sklearn.metrics import average_precision_score, precision_recall_curve, roc_auc_score

from pevolc.models import PermutationEntropyForecaster


def _select_features(df: pd.DataFrame, feature_columns: Sequence[str] | None, label_column: str) -> pd.DataFrame:
    if feature_columns is None:
        # Auto-select numeric columns excluding the label
        feature_columns = [c for c in df.columns if c != label_column and pd.api.types.is_numeric_dtype(df[c])]
    return df[feature_columns]


def _time_split(df: pd.DataFrame, val_fraction: float, time_column: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    sorted_df = df.sort_values(time_column)
    split_idx = int(len(sorted_df) * (1 - val_fraction))
    return sorted_df.iloc[:split_idx], sorted_df.iloc[split_idx:]


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
    # Split strategy
    split_cfg = cfg.get("split", {"type": "random", "val_fraction": 0.2})
    val_fraction = float(split_cfg.get("val_fraction", 0.2))
    if split_cfg.get("type", "random") == "time":
        time_col = split_cfg.get("time_column", "start_s")
        if time_col not in df.columns:
            raise ValueError(f"time_column '{time_col}' not found in dataset")
        train_df, val_df = _time_split(df, val_fraction, time_col)
        X_train = _select_features(train_df, feature_columns, label_column)
        y_train = train_df[label_column].astype(int)
        X_val = _select_features(val_df, feature_columns, label_column)
        y_val = val_df[label_column].astype(int)
    else:
        X_all = _select_features(df, feature_columns, label_column)
        y_all = df[label_column].astype(int)
        # Forecaster handles calibration split internally; validation uses full set
        X_train, y_train = X_all, y_all
        X_val, y_val = X_all, y_all

    model_type = cfg.get("model_type", "logreg")
    forecaster = PermutationEntropyForecaster(model_type=model_type, calibrate=True)
    forecaster.fit(X_train, y_train)

    probs = forecaster.predict_proba(X_val)
    metrics = {
        "roc_auc": float(roc_auc_score(y_val, probs)),
        "pr_auc": float(average_precision_score(y_val, probs)),
    }
    precision, recall, thresholds = precision_recall_curve(y_val, probs)
    eval_path = Path(cfg.get("metrics_path", "experiments/last_run/metrics.csv"))
    eval_path.parent.mkdir(parents=True, exist_ok=True)
    fig_dir = eval_path.parent / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)
    pd.DataFrame({"precision": precision[:-1], "recall": recall[:-1], "threshold": thresholds}).to_csv(
        eval_path, index=False
    )

    # Reliability diagram
    bins = cfg.get("reliability_bins", 10)
    prob_true, prob_pred = _reliability_curve(y_val, probs, bins=bins)
    reliability_path = fig_dir / "reliability.csv"
    pd.DataFrame({"prob_pred": prob_pred, "prob_true": prob_true}).to_csv(reliability_path, index=False)
    _plot_reliability(prob_true, prob_pred, fig_dir / "reliability.png")

    model_path = Path(cfg.get("model_path", "experiments/last_run/forecaster.joblib"))
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(forecaster, model_path)

    # Alert thresholds table
    thresholds_table = _alert_threshold_table(probs, y_val)
    thresholds_table.to_csv(fig_dir / "alert_thresholds.csv", index=False)

    return {"model_path": str(model_path), "metrics_path": str(eval_path), **metrics}


def _reliability_curve(y_true, y_prob, bins=10):
    """Return observed vs predicted probability per bin."""
    bin_edges = np.linspace(0, 1, bins + 1)
    bin_ids = np.digitize(y_prob, bin_edges) - 1
    prob_true = []
    prob_pred = []
    for b in range(bins):
        mask = bin_ids == b
        if mask.sum() == 0:
            continue
        prob_true.append(y_true[mask].mean())
        prob_pred.append(y_prob[mask].mean())
    return np.array(prob_true), np.array(prob_pred)


def _alert_threshold_table(probs: np.ndarray, labels: np.ndarray) -> pd.DataFrame:
    precision, recall, thresholds = precision_recall_curve(labels, probs)
    return pd.DataFrame(
        {"threshold": thresholds, "precision": precision[:-1], "recall": recall[:-1]}
    )


def _plot_reliability(prob_true: np.ndarray, prob_pred: np.ndarray, path: Path) -> None:
    if len(prob_true) == 0:
        return
    plt.figure(figsize=(4, 4))
    plt.plot([0, 1], [0, 1], "k--", alpha=0.4, label="perfect")
    plt.plot(prob_pred, prob_true, "o-", label="model")
    plt.xlabel("Predicted probability")
    plt.ylabel("Observed frequency")
    plt.title("Reliability diagram")
    plt.legend()
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()
