"""I/O helpers for reading seismic datasets."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable


def load_waveforms(paths: Iterable[Path]) -> list[float]:
    """Load seismic waveforms from provided file paths."""

    raise NotImplementedError("Seismic waveform loading not implemented yet")
