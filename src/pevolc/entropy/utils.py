"""Helper utilities for entropy calculations.

The utilities here focus on ordinal pattern extraction, coarse graining, and
lightweight validation used across PE/MPE/WPE implementations.
"""

from __future__ import annotations

import math
import itertools
from functools import lru_cache
from typing import Iterable, Sequence, Tuple

import numpy as np


def coarse_grain(signal: Sequence[float], scale: int) -> np.ndarray:
    """Coarse-grain a time series by averaging non-overlapping windows.

    Parameters
    ----------
    signal:
        Input 1D series.
    scale:
        Coarse-graining factor. A scale of ``k`` averages blocks of length ``k``.

    Returns
    -------
    np.ndarray
        Coarse-grained series of length ``floor(len(signal) / scale)``.
    """

    if scale < 1:
        raise ValueError("scale must be >= 1")
    x = np.asarray(signal, dtype=float)
    usable = (len(x) // scale) * scale
    if usable == 0:
        raise ValueError("signal too short for requested scale")
    trimmed = x[:usable]
    reshaped = trimmed.reshape(-1, scale)
    return reshaped.mean(axis=1)


def _embed(signal: np.ndarray, order: int, delay: int) -> np.ndarray:
    """Return delayed embedding matrix of shape (n_windows, order)."""

    n = signal.shape[0]
    window = (order - 1) * delay
    n_windows = n - window
    if n_windows <= 0:
        raise ValueError("Signal too short for requested order and delay")
    strides = signal.strides[0]
    # Use as_strided to avoid copies; inputs are small in tests and typical use.
    return np.lib.stride_tricks.as_strided(
        signal,
        shape=(n_windows, order),
        strides=(strides, delay * strides),
        writeable=False,
    )


@lru_cache(maxsize=16)
def _pattern_lookup(order: int) -> dict[tuple[int, ...], int]:
    """Cached mapping from permutation tuple to dense index."""
    permutations = list(itertools.permutations(range(order)))
    return {perm: idx for idx, perm in enumerate(permutations)}


def ordinal_pattern_indices(signal: Sequence[float], order: int, delay: int) -> np.ndarray:
    """Return ordinal pattern indices for each embedded window.

    The ordinal pattern is the permutation that sorts the values in the window.
    Ties are broken by stable argsort, matching common PE practice.
    """

    x = np.asarray(signal, dtype=float)
    emb = _embed(x, order, delay)
    argsorted = np.argsort(emb, axis=1, kind="mergesort")

    lookup = _pattern_lookup(order)
    pattern_ids = np.fromiter(
        (lookup[tuple(row)] for row in argsorted),
        count=argsorted.shape[0],
        dtype=int,
    )
    return pattern_ids


def pattern_distribution(
    signal: Sequence[float],
    order: int,
    delay: int,
    weights: Sequence[float] | None = None,
) -> Tuple[np.ndarray, np.ndarray]:
    """Compute ordinal pattern probabilities (optionally weighted).

    Returns
    -------
    probs: np.ndarray
        Probability mass over all ``order!`` patterns.
    counts: np.ndarray
        Raw (weighted) counts per pattern.
    """

    pattern_ids = ordinal_pattern_indices(signal, order, delay)
    n_patterns = math.factorial(order)
    if weights is not None:
        w = np.asarray(weights, dtype=float)
        if w.shape[0] != pattern_ids.shape[0]:
            raise ValueError("weights length must match number of windows")
        counts = np.bincount(pattern_ids, weights=w, minlength=n_patterns)
    else:
        counts = np.bincount(pattern_ids, minlength=n_patterns).astype(float)
    total = counts.sum()
    if total == 0:
        probs = np.zeros_like(counts)
    else:
        probs = counts / total
    return probs, counts
