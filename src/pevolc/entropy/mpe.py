"""Multiscale Permutation Entropy utilities."""

from __future__ import annotations

import math
from typing import Sequence

from .pe import compute_pe
from .utils import coarse_grain


def compute_mpe(
    signal: Sequence[float],
    scales: int | Sequence[int] = 5,
    order: int = 3,
    delay: int = 1,
    *,
    base: float = math.e,
    normalize: bool = True,
) -> list[float]:
    """Compute multiscale permutation entropy over multiple coarse-grained scales.

    Parameters
    ----------
    signal:
        Input time series.
    scales:
        Number of scales (1..scales inclusive) or explicit iterable of scales.
    order, delay, base, normalize:
        Passed to :func:`compute_pe`.
    """

    if isinstance(scales, int):
        scale_list = list(range(1, scales + 1))
    else:
        scale_list = list(scales)
    entropies: list[float] = []
    for scale in scale_list:
        coarse = coarse_grain(signal, scale)
        entropies.append(
            compute_pe(coarse, order=order, delay=delay, base=base, normalize=normalize)
        )
    return entropies
