# CLI and Pipelines

The CLI wraps the reproducible pipelines for entropy computation and forecasting. All configs are YAML so you can version control experiment settings.

## Compute an entropy feature set
```bash
python scripts/compute_entropy_dataset.py configs/example_compute.yaml
# or via the package entry point
python -m pevolc.cli compute-entropy configs/example_compute.yaml
```
Key config fields (see `configs/example_compute.yaml`):
```yaml
data_glob: "data/raw/*.mseed"     # paths to raw waveforms (miniSEED/SAC or plain text/npy)
sampling_rate_hz: 100             # used when data are generic text/npy
window_seconds: 10
step_seconds: 5
order: 4
delay: 1
scales: 3
bandpass_low: 1.0                 # optional Butterworth band-pass (Hz)
bandpass_high: 15.0
detrend: true
zscore: true
output_path: "data/processed/entropy_features.csv"
label_mapping:
  eruption: 1
  background: 0
  default: 0
label_shift_windows: 1            # shift labels earlier to simulate forecast horizon
```
Outputs: a tidy CSV with `start_s`, `end_s`, `pe`, `wpe`, `mpe_scale_k`, basic stats, and optional labels inferred from filenames or `label_value`.

## Train a forecaster
```bash
python scripts/train_model.py configs/example_train.yaml
# or
python -m pevolc.cli train configs/example_train.yaml
```
Example training config:
```yaml
dataset_path: "data/processed/entropy_features.csv"
label_column: "label"
feature_columns: null   # auto-select numeric columns except label
model_type: "logreg"    # or "random_forest", "gradient_boosting"
split:
  type: "time"          # "time" respects chronology; "random" for quick checks
  val_fraction: 0.2
  time_column: "start_s"
model_path: "experiments/last_run/forecaster.joblib"
metrics_path: "experiments/last_run/metrics.csv"
reliability_bins: 10
```
The pipeline trains, calibrates probabilities with Platt scaling, writes metrics and reliability curves to `experiments/last_run/`.

## Evaluate a saved model
```bash
python scripts/evaluate_model.py experiments/last_run/forecaster.joblib data/processed/entropy_features.csv --label-column label
```
This prints ROC/PR scores and can be adapted for continuous monitoring hooks.

These pipelines are intentionally lightweight; duplicate a config in `configs/` to tune per station, change embedding parameters, or adjust alert thresholds.
