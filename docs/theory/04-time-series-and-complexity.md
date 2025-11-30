# Time-Series Complexity and Interpretation

Permutation-based entropies sit between spectral measures and nonlinear dynamical metrics. They capture ordinal structure without requiring phase-space reconstruction beyond rank ordering.

## Relationship to other measures
- **Shannon entropy of amplitudes**: sensitive to amplitude distribution, not ordering.
- **Spectral metrics**: target frequency content but miss phase/order information.
- **Lyapunov exponents**: require continuous state-space trajectories and are fragile under noise.
PE focuses on the ordering of samples, providing robustness to monotonic transformations and mild noise.

## Practical interpretation
- **High entropy**: resembles white noise or highly irregular cracking/turbulence.
- **Low entropy**: regular oscillations (harmonic tremor), clipping, or instrument saturation.
- **Trends over time**: changes in entropy often precede energy increases as the system reorganises.

## Caveats
- Requires enough samples to populate permutations; very short windows bias toward low entropy.
- Sensitive to ties: rank ties are broken by time order; heavy quantisation can distort results.
- Should be combined with amplitude/energy features for context.

In eruption forecasting, entropy acts as a low-cost monitor of dynamical state, complementing rate/energy-based indicators.
