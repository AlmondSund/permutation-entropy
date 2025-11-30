# Basic Examples

These snippets illustrate the core API. You can run them in a Python session or Jupyter notebook once the package is installed.

## Compute PE on a single trace
```python
import numpy as np
from pevolc.entropy import compute_pe, compute_mpe, compute_wpe

t = np.linspace(0, 60, 6000)
trace = np.sin(2 * np.pi * 1.2 * t)  # quasi-harmonic synthetic tremor
pe = compute_pe(trace, order=4, delay=2, base=2)
mpe = compute_mpe(trace, scales=5, order=4, delay=2, base=2)
wpe = compute_wpe(trace, order=4, delay=2, weight_strategy="variance")
print(f"PE={pe:.3f}, WPE={wpe:.3f}, MPE@scale3={mpe[2]:.3f}")
```

## Sliding-window features for a seismic trace
```python
from pathlib import Path
from pevolc.features import WindowConfig, extract_entropy_features
from pevolc.io import read_waveform

data, sr = read_waveform(Path("data/raw/example.mseed"))
cfg = WindowConfig(
    window_seconds=10,
    step_seconds=5,
    order=4,
    scales=4,
    detrend_signal=True,
    zscore=True,
)
df = extract_entropy_features(data, sr, cfg)
print(df.filter(regex="^(start_s|pe|wpe|mpe)").head())
```

## Train a simple forecaster
```python
from pevolc.models import PermutationEntropyForecaster

# Suppose df contains columns: pe, wpe, mpe_scale_1..k, and a binary label column.
feature_cols = [c for c in df.columns if c.startswith("mpe_scale") or c in {"pe", "wpe"}]
X = df[feature_cols]
y = df["label"].astype(int)

forecaster = PermutationEntropyForecaster(model_type="logreg", calibrate=True).fit(X, y)
probs = forecaster.predict_proba(X.tail(5))
alerts = forecaster.predict_alert_level(X.tail(5))
```

## Generate a tiny synthetic dataset
If you do not have local seismic data, you can still exercise the pipeline:
```bash
python scripts/download_example_data.py --output-dir data/raw
python scripts/compute_entropy_dataset.py configs/example_compute.yaml
python scripts/train_model.py configs/example_train.yaml
```
This produces `data/processed/entropy_features.csv` and a calibrated model in `experiments/last_run/`.
