"""Permutation Entropy computation utilities."""

from __future__ import annotations

import math
from typing import Sequence

import numpy as np

from .utils import pattern_distribution


def compute_pe(
    signal: Sequence[float],
    order: int = 3,
    delay: int = 1,
    *,
    base: float = math.e,
    normalize: bool = True,
) -> float:
    """Compute permutation entropy for a 1D sequence.

    Parameters
    ----------
    signal:
        Input time series.
    order:
        Embedding dimension (pattern length).
    delay:
        Time lag between embedding points.
    base:
        Logarithm base used in the entropy definition.
    normalize:
        If True, divide by ``log(order!)`` so the output lies in ``[0, 1]``.
    """

    probs, _ = pattern_distribution(signal, order, delay)
    nonzero = probs[probs > 0]
    entropy = -np.sum(nonzero * np.log(nonzero) / math.log(base))
    if normalize:
        entropy /= math.log(math.factorial(order), base)
    return float(entropy)
