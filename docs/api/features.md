# Features API

## `WindowConfig`
Dataclass configuring window length, step, embedding order/delay, scales, detrending, and z-scoring.

## `extract_basic_features(signal)`
Returns mean, std, rms, min, and max for a 1D sequence.

## `extract_entropy_features(signal, sampling_rate_hz, cfg)`
Computes PE/WPE/MPE over sliding windows defined by `cfg`, returning a tidy `pandas.DataFrame` with start/end times and entropy features per window.
