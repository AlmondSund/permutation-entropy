"""Weighted Permutation Entropy utilities."""

from __future__ import annotations

import math
from typing import Sequence

import numpy as np

from .utils import _embed, pattern_distribution


def compute_wpe(
    signal: Sequence[float],
    order: int = 3,
    delay: int = 1,
    *,
    base: float = math.e,
    normalize: bool = True,
    weights: Sequence[float] | None = None,
    weight_strategy: str = "variance",
) -> float:
    """Compute weighted permutation entropy for a 1D sequence.

    Parameters
    ----------
    signal:
        Input time series.
    order, delay, base, normalize:
        As in :func:`pevolc.entropy.pe.compute_pe`.
    weights:
        Optional external weights per embedded window (length ``n_windows``).
    weight_strategy:
        If ``weights`` is None, compute weights internally. Supported:
        ``"variance"`` (variance of each embedded window) or ``"energy"`` (sum
        of squared amplitude).
    """

    x = np.asarray(signal, dtype=float)
    if weights is None:
        emb = _embed(x, order, delay)
        if weight_strategy == "variance":
            weights_arr = emb.var(axis=1)
        elif weight_strategy == "energy":
            weights_arr = np.sum(emb**2, axis=1)
        else:
            raise ValueError(f"Unknown weight_strategy '{weight_strategy}'")
        weights_arr = np.where(weights_arr == 0, 1e-12, weights_arr)
    else:
        weights_arr = np.asarray(weights, dtype=float)
    probs, _ = pattern_distribution(x, order, delay, weights=weights_arr)
    nonzero = probs[probs > 0]
    entropy = -np.sum(nonzero * np.log(nonzero) / math.log(base))
    if normalize:
        entropy /= math.log(math.factorial(order), base)
    return float(entropy)
