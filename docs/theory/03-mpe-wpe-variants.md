# Multiscale and Weighted Permutation Entropy

## Multiscale Permutation Entropy (MPE)
MPE applies PE to coarse-grained versions of the signal. For scale :math:`s`, the series is averaged over non-overlapping blocks of length :math:`s`, then PE is computed. The curve :math:`H_{PE}(s)` reveals structure across scales.

- **Interpretation**: Rising entropy with scale indicates additional complexity at slower trends; falling curves suggest dominant low-frequency order.
- **Setup**: choose scales (e.g., 1–5), reuse :math:`m,\\tau`, and ensure sufficient samples per coarse-grained series.

## Weighted Permutation Entropy (WPE)
WPE weights each ordinal pattern by a local statistic, altering the probability mass function:

- **Variance weighting**: :math:`w_t = \\mathrm{Var}(x_t, \\ldots, x_{t+(m-1)\\tau})`
- **Energy weighting**: :math:`w_t = \\sum x_i^2`

High-energy or high-variance windows influence the entropy more strongly, reducing the impact of low-amplitude background noise.

## Relevance to volcanic seismicity
- Emergent tremor tends to be energetic and quasi-periodic: WPE highlights these intervals while downweighting quiet background.
- Precursory changes manifest over seconds-to-minutes: MPE tracks entropy evolution as the signal is smoothed.
- Using PE, MPE, and WPE together provides complementary descriptors for forecasting models.
