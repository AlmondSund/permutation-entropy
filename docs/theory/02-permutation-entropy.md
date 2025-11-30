# Permutation Entropy

Permutation Entropy (PE) measures the diversity of ordinal patterns in a time series and is invariant to monotonic transformations. It compresses local temporal structure into a scalar complexity index.

## Ordinal patterns and embedding
For a series :math:`x_t`, choose embedding dimension :math:`m` and delay :math:`\\tau`. Form vectors
:math:`(x_t, x_{t+\\tau}, \\ldots, x_{t+(m-1)\\tau})` and replace them with the permutation that sorts the values (ties broken by time order). There are :math:`m!` possible patterns.

## Probability distribution
Let :math:`p(\\pi_i)` be the relative frequency of permutation :math:`\\pi_i` across all windows. Weighted variants modify these frequencies; plain PE counts each window equally.

## Entropy definition
.. math::

   H_{PE} = - \\sum_{i=1}^{m!} p(\\pi_i) \\log_b p(\\pi_i)

Normalising by :math:`\\log_b m!` gives :math:`H_{PE} \\in [0,1]`.

- Low PE: highly regular signals (pure tone, periodic tremor).
- High PE: irregular or noisy signals (fracturing, turbulent flow, cultural noise).

## Practical guidance
- **Embedding dimension**: :math:`m=3..7` is common; require at least :math:`5-10` times :math:`m!` windows.
- **Delay**: :math:`\\tau=1` for broadband sensitivity; larger :math:`\\tau` focuses on lower frequencies.
- **Window length**: pick windows long enough to gather sufficient patterns but short enough to track transients (tens of seconds for many volcanoes).
