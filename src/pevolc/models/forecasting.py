"""Forecasting models for eruption prediction."""

from __future__ import annotations

from typing import Any, Sequence


def train_forecasting_model(features: Sequence[Sequence[float]], labels: Sequence[int]) -> Any:
    """Train a forecasting model using provided features and labels."""

    raise NotImplementedError("Forecasting model training not implemented yet")


def predict_proba(model: Any, features: Sequence[Sequence[float]]) -> list[float]:
    """Return eruption probabilities for the given feature matrix."""

    raise NotImplementedError("Forecasting prediction not implemented yet")
