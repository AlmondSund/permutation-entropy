# permutation-entropy

Permutation-entropy is a prototype toolkit for volcanic eruption forecasting that turns continuous seismic waveforms into information-theoretic features (Permutation Entropy, Multiscale Permutation Entropy, Weighted Permutation Entropy) and feeds them to lightweight machine-learning forecasters. The goal is to provide an open, reproducible baseline for PE-driven eruption alerting.

## What’s inside
- Rigorous PE/MPE/WPE implementations with configurable embedding dimension, delay, log base, and normalization.
- Seismic-centric feature extraction (windowing, detrending/normalisation) returning tidy pandas DataFrames.
- Baseline forecasting models (logistic regression, random forest, gradient boosting) with Platt calibration and alert thresholds.
- Config-driven pipelines + CLI to compute entropy datasets, train models, and evaluate.
- Theory + usage docs and demo notebooks for exploration.

## Installation
```bash
pip install -e .
# or using requirements
pip install -r requirements.txt
```
Python 3.11+ is recommended.

## Quickstart
Generate a small synthetic trace, compute entropy features, and train a demo model:
```bash
python scripts/download_example_data.py --output-dir data/raw
python scripts/compute_entropy_dataset.py configs/example_compute.yaml
python scripts/train_model.py configs/example_train.yaml
```
Outputs:
- `data/processed/entropy_features.csv` (features per window)
- `experiments/last_run/forecaster.joblib` (trained model)
- `experiments/last_run/metrics.csv` (precision/recall curve)

For more details see `docs/usage/` and the demo notebooks in `notebooks/`.
