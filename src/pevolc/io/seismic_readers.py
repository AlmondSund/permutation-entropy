"""I/O helpers for reading seismic datasets."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, Tuple

import numpy as np

try:
    from obspy import read  # type: ignore
except Exception:  # pragma: no cover - optional dependency path
    read = None


def read_waveform(path: Path) -> Tuple[np.ndarray, float]:
    """Read a waveform file, returning (data, sampling_rate)."""

    if read is None:
        raise ImportError("ObsPy is required to read seismic formats")
    st = read(str(path))
    tr = st[0]
    return tr.data.astype(float), float(tr.stats.sampling_rate)


def load_waveforms(paths: Iterable[Path]) -> list[Tuple[np.ndarray, float]]:
    """Load multiple seismic waveforms."""

    return [read_waveform(Path(p)) for p in paths]
