"""Helper utilities for entropy calculations."""

from __future__ import annotations

from typing import Iterable


def coarse_grain(signal: Iterable[float], scale: int) -> list[float]:
    """Reduce resolution of a sequence by averaging non-overlapping windows."""

    raise NotImplementedError("Coarse graining not implemented yet")
