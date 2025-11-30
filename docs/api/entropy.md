# Entropy API

Core functions live in `pevolc.entropy` and operate on 1D sequences (NumPy arrays or array-like).

## `compute_pe(signal, order=3, delay=1, base=e, normalize=True)`
Permutation entropy of a 1D sequence.
- `order`: embedding dimension $m$ (number of samples per permutation).
- `delay`: lag $\tau$ between embedded samples.
- `base`: logarithm base for entropy (e, 2, or 10).
- `normalize`: divide by $\log_b m!$ to constrain output to `[0, 1]`.
Returns a single `float`.

## `compute_wpe(signal, order=3, delay=1, base=e, normalize=True, weights=None, weight_strategy="variance")`
Weighted permutation entropy; identical interface to `compute_pe` with additional weighting.
- `weights`: optional array of length `n_windows` to weight each ordinal pattern.
- `weight_strategy`: if `weights` is not provided, choose `"variance"` or `"energy"` to compute per-window weights internally.
Returns a single `float`.

## `compute_mpe(signal, scales=5, order=3, delay=1, base=e, normalize=True)`
Multiscale permutation entropy computed after coarse-graining.
- `scales`: integer `k` to use scales `1..k` or an explicit iterable of scales.
Returns a `list[float]` of length equal to the number of requested scales.

## Utilities
- `coarse_grain(signal, scale)` – average non-overlapping blocks of length `scale`; raises if the signal is too short.
- `ordinal_pattern_indices(signal, order, delay)` – return dense indices (`0..m!-1`) for each embedded window using stable sorting to break ties.
- `pattern_distribution(signal, order, delay, weights=None)` – return `(probs, counts)` arrays with optional weights applied; `probs` sums to 1 when patterns exist.
