"""Feature extraction for seismic signals."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

import numpy as np
import pandas as pd
from scipy.signal import detrend

from pevolc.entropy.mpe import compute_mpe
from pevolc.entropy.pe import compute_pe
from pevolc.entropy.wpe import compute_wpe


@dataclass
class WindowConfig:
    """Configuration for sliding-window feature extraction."""

    window_seconds: float
    step_seconds: float
    order: int = 3
    delay: int = 1
    scales: int = 3
    normalize: bool = True
    base: float = np.e
    compute_pe: bool = True
    compute_mpe: bool = True
    compute_wpe: bool = True
    detrend_signal: bool = False
    zscore: bool = False


def _sliding_windows(x: np.ndarray, window: int, step: int) -> Iterable[tuple[int, int, np.ndarray]]:
    for start in range(0, len(x) - window + 1, step):
        end = start + window
        yield start, end, x[start:end]


def _preprocess(x: np.ndarray, cfg: WindowConfig) -> np.ndarray:
    if cfg.detrend_signal:
        x = detrend(x)
    if cfg.zscore:
        std = x.std() or 1.0
        x = (x - x.mean()) / std
    return x


def extract_basic_features(signal: Sequence[float]) -> dict[str, float]:
    """Return a small set of descriptive statistics for a time series."""

    x = np.asarray(signal, dtype=float)
    return {
        "mean": float(x.mean()),
        "std": float(x.std()),
        "rms": float(np.sqrt(np.mean(x**2))),
        "max": float(x.max()),
        "min": float(x.min()),
    }


def extract_entropy_features(
    signal: Sequence[float],
    sampling_rate_hz: float,
    cfg: WindowConfig,
) -> pd.DataFrame:
    """Compute PE/MPE/WPE over sliding windows for a seismic trace.

    Returns a tidy DataFrame with one row per window and columns:
    ``start_s``, ``end_s``, ``pe``, ``wpe``, and ``mpe_scale_k``.
    """

    x = np.asarray(signal, dtype=float)
    x = _preprocess(x, cfg)
    window_samples = int(cfg.window_seconds * sampling_rate_hz)
    step_samples = int(cfg.step_seconds * sampling_rate_hz)
    if window_samples <= 0 or step_samples <= 0:
        raise ValueError("window_seconds and step_seconds must be positive")

    records: list[dict[str, float]] = []
    for start_idx, end_idx, segment in _sliding_windows(x, window_samples, step_samples):
        record: dict[str, float] = {
            "start_s": start_idx / sampling_rate_hz,
            "end_s": end_idx / sampling_rate_hz,
        }
        if cfg.compute_pe:
            record["pe"] = compute_pe(
                segment, order=cfg.order, delay=cfg.delay, base=cfg.base, normalize=cfg.normalize
            )
        if cfg.compute_wpe:
            record["wpe"] = compute_wpe(
                segment, order=cfg.order, delay=cfg.delay, base=cfg.base, normalize=cfg.normalize
            )
        if cfg.compute_mpe:
            mpe_vals = compute_mpe(
                segment,
                scales=cfg.scales,
                order=cfg.order,
                delay=cfg.delay,
                base=cfg.base,
                normalize=cfg.normalize,
            )
            for i, val in enumerate(mpe_vals, start=1):
                record[f"mpe_scale_{i}"] = val
        record.update({f"basic_{k}": v for k, v in extract_basic_features(segment).items()})
        records.append(record)
    return pd.DataFrame.from_records(records)
