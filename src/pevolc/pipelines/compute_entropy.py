"""Pipeline to compute entropy-based features from seismic data."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable


def compute_entropy_dataset(data_paths: Iterable[Path], output_path: Path) -> None:
    """Compute permutation-entropy variants for provided data files and save results."""

    raise NotImplementedError("Entropy dataset computation not implemented yet")
