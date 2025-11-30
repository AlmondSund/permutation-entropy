# Time-Series Complexity and Interpretation

Permutation-based entropies sit between spectral measures and nonlinear dynamical metrics. They capture ordinal structure without needing full phase-space reconstruction, making them robust to monotonic transformations and modest noise.

## Relationship to other measures
- **Amplitude-only entropy**: Shannon entropy of amplitudes ignores ordering, so two signals with identical histograms but different dynamics look the same.
- **Spectral metrics**: periodograms or spectral slopes capture frequency content but lose phase/order information that distinguishes tremor from noise.
- **Lyapunov exponents**: probe divergence in reconstructed phase space but require long, clean trajectories and are fragile under noise or non-stationarity.
PE focuses solely on the ordering of samples, providing a low-parameter view of dynamical structure.

## Practical interpretation
- **High entropy**: resembles white noise or highly irregular cracking/turbulence; pattern counts are nearly uniform.
- **Low entropy**: regular oscillations (harmonic tremor), clipped instruments, or quantised telemetry; a few permutations dominate.
- **Temporal trends**: a drop in entropy preceding an energy rise can indicate the system settling into a stable oscillatory regime; the opposite suggests chaotic activity or changing source processes.

## Caveats
- Ensure enough windows: very short windows bias toward low entropy because many permutations never occur.
- Ties and quantisation: rank ties are broken by time order; strong quantisation or clipping depresses entropy.
- Context matters: combine entropy with amplitude/energy statistics and station metadata to avoid misinterpreting cultural noise as volcanic change.

In eruption forecasting, entropy acts as a low-cost monitor of dynamical state that complements rate- and energy-based indicators and integrates naturally into sliding-window pipelines.
