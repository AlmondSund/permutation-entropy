"""Forecasting models for eruption prediction."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Sequence

import numpy as np
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

from .calibration import PlattCalibrator


def _build_model(model_type: str) -> Any:
    if model_type == "logreg":
        return LogisticRegression(max_iter=200)
    if model_type == "random_forest":
        return RandomForestClassifier(
            n_estimators=200, max_depth=None, min_samples_leaf=2, random_state=42
        )
    if model_type == "gradient_boosting":
        return GradientBoostingClassifier(random_state=42)
    raise ValueError(f"Unsupported model_type '{model_type}'")


@dataclass
class PermutationEntropyForecaster:
    """Wrapper around a scikit-learn classifier with optional Platt calibration."""

    model_type: str = "logreg"
    calibrate: bool = True

    def __post_init__(self) -> None:
        self.model = _build_model(self.model_type)
        self.calibrator: PlattCalibrator | None = None

    def fit(self, features: Sequence[Sequence[float]], labels: Sequence[int]) -> "PermutationEntropyForecaster":
        X = np.asarray(features, dtype=float)
        y = np.asarray(labels, dtype=int)
        if self.calibrate:
            X_train, X_cal, y_train, y_cal = train_test_split(
                X, y, test_size=0.2, random_state=42, stratify=y
            )
            self.model.fit(X_train, y_train)
            raw_probs = self.model.predict_proba(X_cal)[:, 1]
            self.calibrator = PlattCalibrator().fit(raw_probs, y_cal)
        else:
            self.model.fit(X, y)
        return self

    def predict_proba(self, features: Sequence[Sequence[float]]) -> np.ndarray:
        X = np.asarray(features, dtype=float)
        probs = self.model.predict_proba(X)[:, 1]
        if self.calibrator is not None:
            probs = self.calibrator.transform(probs)
        return probs

    def predict_alert_level(
        self, features: Sequence[Sequence[float]], thresholds: tuple[float, float] = (0.33, 0.66)
    ) -> list[str]:
        """Return alert levels (green/yellow/red) for given features."""

        probs = self.predict_proba(features)
        levels = []
        low, high = thresholds
        for p in probs:
            if p < low:
                levels.append("green")
            elif p < high:
                levels.append("yellow")
            else:
                levels.append("red")
        return levels


def train_forecasting_model(
    features: Sequence[Sequence[float]], labels: Sequence[int], model_type: str = "logreg"
) -> PermutationEntropyForecaster:
    """Train a forecasting model using provided features and labels."""

    forecaster = PermutationEntropyForecaster(model_type=model_type, calibrate=True)
    forecaster.fit(features, labels)
    return forecaster


def predict_proba(model: Any, features: Sequence[Sequence[float]]) -> list[float]:
    """Return eruption probabilities for the given feature matrix."""

    return list(model.predict_proba(features))


def evaluate_auc(model: PermutationEntropyForecaster, features: Sequence[Sequence[float]], labels: Sequence[int]) -> float:
    """Compute ROC-AUC for quick sanity checks."""

    probs = model.predict_proba(features)
    return float(roc_auc_score(labels, probs))
