# Introduction to Seismicity and Forecasting

Volcanic systems radiate continuous seismic energy as magma migrates, cracks open, and fluids interact with gas or groundwater. As eruptions approach, seismic waveforms often drift from low-energy background noise to tremor-like, quasi-harmonic, or bursty patterns. The goal of forecasting is to detect these transitions early enough to trigger mitigations while keeping false alarms manageable.

## Eruption precursors in seismic data
- **Event-rate changes**: volcano-tectonic or long-period earthquakes may cluster or accelerate.
- **Emergent tremor**: sustained, narrowband signals linked to fluid resonance or conduit oscillations.
- **Amplitude growth**: RMS energy rises as gas flux or magma ascent accelerates.
- **Complexity swings**: signals can become more regular (harmonic tremor) or more irregular (fracturing or turbulent degassing) depending on the underlying physics.

## Forecasting challenges
- **Non-stationarity** from weather, seasonality, or cultural noise complicates baselines.
- **Sensor diversity** (station geometry, instrument response, site effects) changes waveform character.
- **Data volume** demands automated summarisation of long continuous streams.
- **Label uncertainty** arises because eruptions are rare, and onset times may be defined retroactively.

Ordinal-pattern-based entropies offer a compact, interpretable descriptor of dynamical state that is invariant under monotonic transformations and tolerant of mild noise. They suit continuous monitoring where a handful of tuned parameters can track complexity shifts that accompany eruptive transitions.
