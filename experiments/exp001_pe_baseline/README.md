# exp001 – PE baseline

- Objective: evaluate plain PE features (order=3, delay=1) on synthetic tremor vs. noise.
- Config: `experiments/exp001_pe_baseline/config.yaml`
- Steps:
  1. Generate synthetic data: `python scripts/download_example_data.py`
  2. Compute features: `python scripts/compute_entropy_dataset.py configs/example_compute.yaml`
  3. Train model: `python scripts/train_model.py configs/example_train.yaml`
- Results are stored in `results.csv` (ROC/PR metrics) and figures can be added under `figures/`.
