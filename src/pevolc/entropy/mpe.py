"""Multiscale Permutation Entropy utilities."""

from __future__ import annotations

from typing import Sequence


def compute_mpe(signal: Sequence[float], scales: int = 5, order: int = 3, delay: int = 1) -> list[float]:
    """Compute multiscale permutation entropy over multiple scales.

    Returns a list of entropy values, one per scale.
    """

    raise NotImplementedError("Multiscale permutation entropy computation not implemented yet")
