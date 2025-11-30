"""Feature extraction for seismic signals."""

from __future__ import annotations

from typing import Sequence


def extract_basic_features(signal: Sequence[float]) -> dict[str, float]:
    """Return a dictionary of basic seismic features for a time series."""

    raise NotImplementedError("Seismic feature extraction not implemented yet")
