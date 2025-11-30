"""Evaluate a forecasting model from the command line."""

from __future__ import annotations

import argparse
from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import average_precision_score, roc_auc_score

def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate a trained PE-based forecasting model.")
    parser.add_argument("model", type=Path, help="Path to joblib model.")
    parser.add_argument("dataset", type=Path, help="CSV with features and labels.")
    parser.add_argument("--label-column", default="label", help="Name of label column.")
    args = parser.parse_args()

    model = joblib.load(args.model)
    df = pd.read_csv(args.dataset)
    y = df[args.label_column]
    X = df.drop(columns=[args.label_column])
    probs = model.predict_proba(X)
    auc = roc_auc_score(y, probs)
    pr_auc = average_precision_score(y, probs)
    print(f"ROC-AUC: {auc:.3f}  PR-AUC: {pr_auc:.3f}")


if __name__ == "__main__":
    main()
