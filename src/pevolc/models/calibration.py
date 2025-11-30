"""Calibration and evaluation utilities for forecasting models."""

from __future__ import annotations

from typing import Sequence


def calibrate_probabilities(probs: Sequence[float], labels: Sequence[int]) -> Sequence[float]:
    """Calibrate raw model probabilities against observed labels."""

    raise NotImplementedError("Probability calibration not implemented yet")
