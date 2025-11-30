# Permutation Entropy

Permutation Entropy (PE) measures the diversity of ordinal patterns in a time series and is invariant to monotonic transformations. It compresses local temporal structure into a scalar complexity index.

## Ordinal patterns and embedding
For a series $x_t$, choose an embedding dimension $m$ and delay $\tau$. Form delayed vectors
$$
\mathbf{x}_t = \big(x_t, x_{t+\tau}, \ldots, x_{t+(m-1)\tau}\big).
$$
Replace each $\mathbf{x}_t$ with the permutation $\pi_t$ that sorts its elements. A stable sort breaks ties by time order, so equal values retain their temporal ordering. There are $m!$ possible patterns.

## Probability distribution over permutations
Let $n$ be the number of windows. The empirical frequency of permutation $\pi_i$ is
$$
p(\pi_i) = \frac{1}{n} \sum_{t} \mathbf{1}[\pi_t = \pi_i],
$$
optionally replaced by a weighted count in WPE (see below). The set $\{p(\pi_i)\}$ is a probability mass function over ordinal patterns.

## Entropy definition
The permutation entropy with logarithm base $b$ is
$$
H_{\mathrm{PE}} = - \sum_{i=1}^{m!} p(\pi_i) \log_b p(\pi_i).
$$
Normalising by $\log_b m!$ yields $H_{\mathrm{PE}} \in [0, 1]$.

- Low PE: highly regular signals (pure tone, clipped sensor, quasi-harmonic tremor).
- High PE: irregular or noisy signals (fracturing, turbulent degassing, cultural noise).

## Practical guidance for seismic traces
- **Embedding dimension**: $m \in [3, 7]$ is typical. Require at least $5$–$10$ times $m!$ windows to populate permutations.
- **Delay $\tau$**: $\tau=1$ is broadband; larger $\tau$ emphasises lower-frequency ordering (useful when tremor dominates).
- **Window length**: choose windows long enough to gather permutations yet short enough to track transients (tens of seconds for many volcanoes).
- **Ties and quantisation**: strong quantisation or clipping lowers PE artificially; break ties by time as implemented here.
- **Interpretation**: a drop in PE with rising RMS often signals emergent, organised tremor; rising PE with rising RMS can reflect chaotic cracking or gas slug break-up.
