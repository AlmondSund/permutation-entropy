"""Download example seismic data for demos and tests."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np

def main() -> None:
    parser = argparse.ArgumentParser(description="Generate lightweight synthetic seismic examples.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/raw"),
        help="Directory to store generated example traces.",
    )
    parser.add_argument("--duration", type=float, default=300.0, help="Trace duration (s).")
    parser.add_argument("--sampling-rate", type=float, default=100.0, help="Sampling rate (Hz).")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    t = np.arange(0, args.duration, 1 / args.sampling_rate)
    rng = np.random.default_rng(1)

    # Background: low-amplitude noise + weak harmonic
    noise = rng.normal(scale=0.1, size=t.shape)
    harmonic = 0.2 * np.sin(2 * np.pi * 0.5 * t)
    background = noise + harmonic

    # Eruption-like: stronger tremor burst with added noise
    tremor_env = np.exp(-((t - args.duration / 2) ** 2) / (2 * (args.duration / 10) ** 2))
    tremor = 0.8 * tremor_env * np.sin(2 * np.pi * 3 * t)
    eruption = background + tremor + rng.normal(scale=0.05, size=t.shape)

    np.save(args.output_dir / "background.npy", background)
    np.save(args.output_dir / "eruption.npy", eruption)
    print(f"Wrote synthetic traces to {args.output_dir} (background.npy, eruption.npy)")


if __name__ == "__main__":
    main()
