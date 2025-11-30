# Multiscale and Weighted Permutation Entropy

Permutation entropy can be extended to capture structure across scales (MPE) and to emphasise energetic windows (WPE). Both reuse the ordinal-pattern machinery from plain PE.

## Multiscale Permutation Entropy (MPE)
For a chosen scale $s$, coarse-grain the signal by averaging non-overlapping blocks:
$$
y^{(s)}_k = \frac{1}{s} \sum_{i=0}^{s-1} x_{ks+i}.
$$
Compute $H_{\mathrm{PE}}$ on $y^{(s)}$ for each $s$ in a scale set $\mathcal{S}$. The resulting curve $H_{\mathrm{PE}}(s)$ reveals how ordering changes when fast fluctuations are smoothed.

- Rising entropy with increasing $s$ indicates additional irregularity at slower trends.
- Falling entropy suggests a dominant low-frequency order (e.g., tremor that becomes clearer once high-frequency noise is removed).
- Choose scales (e.g., $s=1\ldots5$) such that each coarse-grained series still has enough windows to populate permutations.

## Weighted Permutation Entropy (WPE)
WPE modifies the empirical distribution with per-window weights $w_t$:
$$
p_w(\pi_i) = \frac{\sum_t w_t \,\mathbf{1}[\pi_t = \pi_i]}{\sum_t w_t}, \qquad
H_{\mathrm{WPE}} = - \sum_{i=1}^{m!} p_w(\pi_i) \log_b p_w(\pi_i).
$$
Common choices are:

- **Variance weighting**: $w_t = \operatorname{Var}(x_t, \ldots, x_{t+(m-1)\tau})$.
- **Energy weighting**: $w_t = \sum_j x_j^2$ within the embedded window.

Weights reduce the influence of low-amplitude background and amplify windows where the signal is energetic or rapidly varying.

## Relevance to volcanic seismicity
- Emergent tremor is often energetic and quasi-periodic: WPE highlights these intervals while downweighting quiet background.
- Precursory changes can span seconds to minutes: MPE tracks how entropy evolves when short-period transients are smoothed.
- Using PE, MPE, and WPE together provides complementary descriptors that separate ordered tremor from bursty cracking and assess whether complexity sits at fast or slow scales.
