# Basic Examples

## Compute PE on a single trace
```python
import numpy as np
from pevolc.entropy import compute_pe

trace = np.sin(2*np.pi*1*np.linspace(0, 10, 1000))
pe_value = compute_pe(trace, order=3, delay=1, base=2)
print(f"PE: {pe_value:.3f}")
```

## Sliding-window features for a seismic trace
```python
from pevolc.features import WindowConfig, extract_entropy_features
from pevolc.io import read_waveform

data, sr = read_waveform("data/raw/example.mseed")
cfg = WindowConfig(window_seconds=10, step_seconds=5, order=4, scales=4)
df = extract_entropy_features(data, sr, cfg)
print(df.head())
```

## Train a simple forecaster
```python
from pevolc.models import PermutationEntropyForecaster

X = df[[c for c in df.columns if c.startswith("mpe") or c in {"pe","wpe"}]]
y = df["label"]  # binary eruption indicator aligned with windows
model = PermutationEntropyForecaster(model_type="logreg").fit(X, y)
probs = model.predict_proba(X[-5:])
```
