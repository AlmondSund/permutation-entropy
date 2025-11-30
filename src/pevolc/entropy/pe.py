"""Permutation Entropy computation utilities."""

from __future__ import annotations

from typing import Sequence


def compute_pe(signal: Sequence[float], order: int = 3, delay: int = 1) -> float:
    """Compute permutation entropy for a 1D sequence.

    Parameters
    ----------
    signal: Sequence[float]
        Input time series.
    order: int
        Embedding dimension (pattern length).
    delay: int
        Time lag between embedding points.
    """
    raise NotImplementedError("Permutation entropy computation not implemented yet")
