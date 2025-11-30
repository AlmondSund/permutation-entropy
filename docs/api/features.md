# Features API

Sliding-window feature extraction lives in `pevolc.features`.

## `WindowConfig`
Dataclass configuring entropy computation per window:
- `window_seconds`, `step_seconds`: duration and hop size in seconds.
- `order`, `delay`, `scales`: embedding parameters for PE/WPE/MPE.
- `normalize`, `base`: entropy options.
- `compute_pe`, `compute_mpe`, `compute_wpe`: toggles to enable/disable variants.
- `detrend_signal`, `zscore`: optional preprocessing per trace.

## `extract_basic_features(signal)`
Return descriptive stats for a 1D sequence: mean, std, RMS, min, max.

## `extract_entropy_features(signal, sampling_rate_hz, cfg)`
Compute PE/WPE/MPE (and basic stats) over sliding windows defined by `cfg`.
- Inputs: 1D signal, sampling rate in Hz, and a `WindowConfig`.
- Output: tidy `pandas.DataFrame` with `start_s`, `end_s`, entropy values (`pe`, `wpe`, `mpe_scale_k`), and `basic_*` amplitude stats.

Internal helpers `_sliding_windows` and `_preprocess` are intentionally private; customise behaviour by extending `WindowConfig` or wrapping `extract_entropy_features`.
