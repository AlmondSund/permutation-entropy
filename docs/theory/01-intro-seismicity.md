# Introduction to Seismicity and Forecasting

Volcanic systems radiate continuous seismic energy as magma migrates, cracks open, and fluids interact. Prior to eruptions, seismic signals often transition from low-energy background noise to tremor-like, quasi-harmonic, or bursty patterns. Forecasting aims to detect these transitions early enough to trigger mitigations while avoiding excessive false alarms.

## Eruption precursors in seismic data
- **Increased event rates**: more volcano-tectonic earthquakes or long-period events.
- **Emergent tremor**: sustained, narrowband signals linked to fluid resonance.
- **Amplitude growth**: RMS energy rises as gas flux or magma ascent accelerates.
- **Complexity changes**: signals can become more regular (tremor) or more irregular (fracturing) depending on the mechanism.

## Forecasting challenges
- **Non-stationarity**: background noise, weather, and anthropogenic sources vary.
- **Sensor diversity**: different stations, instruments, and site effects.
- **Data volume**: continuous recordings require automated, scalable methods.
- **Uncertainty**: eruptions are rare; labeling is difficult and often retrospective.

Permutation entropy (and variants) provides a compact way to track signal complexity that is robust to amplitude scaling and monotonic transformations, making it attractive for continuous monitoring.
