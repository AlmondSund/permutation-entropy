# Entropy API

## `pevolc.entropy.compute_pe`
`compute_pe(signal, order=3, delay=1, base=e, normalize=True)`  
Returns permutation entropy of a 1D sequence. Normalised to `[0,1]` if `normalize=True`.

## `pevolc.entropy.compute_mpe`
`compute_mpe(signal, scales=5, order=3, delay=1, base=e, normalize=True)`  
Coarse-grains the series for each scale then computes PE. Returns a list of entropies.

## `pevolc.entropy.compute_wpe`
`compute_wpe(signal, order=3, delay=1, base=e, normalize=True, weights=None, weight_strategy="variance")`  
Weighted PE using per-window variance or energy (or user-provided weights).

## Utilities
- `coarse_grain(signal, scale)` – average non-overlapping windows.
- `ordinal_pattern_indices(signal, order, delay)` – pattern ids per window.
- `pattern_distribution(signal, order, delay, weights=None)` – probability mass and counts.
