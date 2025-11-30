# Data Directory

- `data/raw/`: continuous traces (SAC/miniSEED/NPY). Use `scripts/download_example_data.py` to generate small synthetic examples (`background.npy`, `eruption.npy`).
- `data/interim/`: optional filtered or segmented traces.
- `data/processed/`: tabular PE/MPE/WPE feature datasets (CSV/Parquet) produced by `scripts/compute_entropy_dataset.py`.

Real observatory data is not included; point the `data_glob` in configs to your own files. These folders are git-ignored by default to avoid committing large binaries.
