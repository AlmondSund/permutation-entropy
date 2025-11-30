"""Pipeline to compute entropy-based features from seismic data."""

from __future__ import annotations

import glob
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd
import yaml

from pevolc.features import WindowConfig, extract_entropy_features
from pevolc.io import read_waveform


def _load_signal(path: Path, sampling_rate: float | None = None) -> tuple[np.ndarray, float]:
    try:
        data, sr = read_waveform(path)
        return data, sr
    except Exception:
        # Fallback to generic text/npy with provided sampling rate
        if sampling_rate is None:
            raise
        if path.suffix == ".npy":
            data = np.load(path)
        else:
            data = np.loadtxt(path)
        return data.astype(float), sampling_rate


def _infer_label(path: Path, cfg: dict) -> float | None:
    if "label_value" in cfg:
        return float(cfg["label_value"])
    mapping = cfg.get("label_mapping")
    if mapping:
        for key, value in mapping.items():
            if key in path.name:
                return float(value)
        return float(mapping.get("default", 0))
    return None


def compute_entropy_dataset(
    data_paths: Iterable[Path], output_path: Path, cfg: dict
) -> pd.DataFrame:
    """Compute permutation-entropy variants for provided data files and save results."""

    sampling_rate = float(cfg["sampling_rate_hz"])
    window_cfg = WindowConfig(
        window_seconds=float(cfg.get("window_seconds", 10.0)),
        step_seconds=float(cfg.get("step_seconds", 5.0)),
        order=int(cfg.get("order", 3)),
        delay=int(cfg.get("delay", 1)),
        scales=int(cfg.get("scales", 3)),
        detrend_signal=bool(cfg.get("detrend", False)),
        zscore=bool(cfg.get("zscore", False)),
    )
    frames = []
    for path in data_paths:
        data, sr = _load_signal(path, sampling_rate)
        features = extract_entropy_features(data, sr, window_cfg)
        features.insert(0, "source_file", path.name)
        label = _infer_label(path, cfg)
        if label is not None:
            features["label"] = label
        frames.append(features)
    dataset = pd.concat(frames, ignore_index=True)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    dataset.to_csv(output_path, index=False)
    return dataset


def run_from_config(config_path: Path) -> pd.DataFrame:
    """Load YAML config and run the entropy computation pipeline."""

    with open(config_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    data_glob = cfg.get("data_glob")
    if not data_glob:
        raise ValueError("Config must include data_glob")
    paths = [Path(p) for p in glob.glob(data_glob)]
    if not paths:
        raise FileNotFoundError(f"No files matched {data_glob}")
    output = Path(cfg.get("output_path", "data/processed/entropy_features.csv"))
    return compute_entropy_dataset(paths, output, cfg)
