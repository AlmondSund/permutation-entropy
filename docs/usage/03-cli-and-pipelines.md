# CLI and Pipelines

The CLI wraps the pipelines for reproducibility.

## Compute entropy dataset
```bash
python scripts/compute_entropy_dataset.py configs/example_compute.yaml
```
`configs/example_compute.yaml` should define:
```yaml
data_glob: "data/raw/*.mseed"
sampling_rate_hz: 100
window_seconds: 10
step_seconds: 5
order: 4
delay: 1
scales: 3
output_path: "data/processed/entropy_features.csv"
label_mapping:
  eruption: 1
  background: 0
  default: 0
```

## Train a forecaster
```bash
python scripts/train_model.py configs/example_train.yaml
```
Example config:
```yaml
dataset_path: "data/processed/entropy_features.csv"
label_column: "label"
feature_columns: null   # auto-select numeric columns except label
model_type: "logreg"
model_path: "experiments/last_run/forecaster.joblib"
metrics_path: "experiments/last_run/metrics.csv"
```

## Evaluate a saved model
```bash
python scripts/evaluate_model.py experiments/last_run/forecaster.joblib data/processed/entropy_features.csv --label-column label
```

These pipelines are intentionally lightweight; adapt them in `configs/` for specific stations or experiments.
