"""Calibration and evaluation utilities for forecasting models."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np
from sklearn.linear_model import LogisticRegression


@dataclass
class PlattCalibrator:
    """Simple Platt scaling calibrator."""

    max_iter: int = 200

    def __post_init__(self) -> None:
        self._lr = LogisticRegression(max_iter=self.max_iter)
        self._fitted = False

    def fit(self, probs: Sequence[float], labels: Sequence[int]) -> "PlattCalibrator":
        X = np.asarray(probs, dtype=float).reshape(-1, 1)
        y = np.asarray(labels, dtype=int)
        self._lr.fit(X, y)
        self._fitted = True
        return self

    def transform(self, probs: Sequence[float]) -> np.ndarray:
        if not self._fitted:
            raise RuntimeError("Calibrator must be fitted before calling transform.")
        X = np.asarray(probs, dtype=float).reshape(-1, 1)
        return self._lr.predict_proba(X)[:, 1]


def calibrate_probabilities(probs: Sequence[float], labels: Sequence[int]) -> Sequence[float]:
    """Calibrate raw model probabilities against observed labels using Platt scaling."""

    calibrator = PlattCalibrator().fit(probs, labels)
    return calibrator.transform(probs)
