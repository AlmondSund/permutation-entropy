# Applying Entropy Methods to Eruption Forecasting

Entropy features summarise waveform complexity and can signal dynamical shifts. The toolkit provides a lightweight pipeline aligned with the following conceptual workflow.

1. **Stream & preprocess**: detrend, band-pass, resample, and optionally z-score continuous traces; drop gross gaps.
2. **Window & compute**: run PE/WPE/MPE on overlapping windows (e.g., 10–60 s) with embedding $(m, \tau)$ chosen per station.
3. **Aggregate features**: combine entropy and basic amplitude statistics across recent windows to describe short-term evolution.
4. **Forecast**: train a probabilistic classifier to estimate eruption likelihood over a horizon (e.g., 10–60 minutes ahead); calibrate probabilities.

## Physical interpretations
- Rising entropy with rising energy may indicate fracturing or turbulent degassing.
- Falling entropy with rising energy often corresponds to emergent, quasi-harmonic tremor.
- Divergence across scales (MPE) highlights simultaneous tremor (ordered at low frequencies) and transient bursts (irregular at high frequencies).

## Alerting and calibration
- Map calibrated probabilities to alert levels (green/yellow/red) with adjustable thresholds reflecting local risk tolerance.
- Use Platt scaling (implemented) or isotonic regression to align probabilities with observed frequencies and avoid overconfident alarms.

## Validation
- Prefer time-based splits (train early, validate late) to respect causality; random splits are acceptable only for quick checks.
- Report ROC/PR curves, reliability diagrams, alert lead time (how early an alert fires before eruption), and false-alarm rate per day/week.
- Track station-specific performance; strong site effects often require per-station tuning of $(m, \tau)$ and MPE scales.

## Limitations and caveats
- Eruptions are rare and labels uncertain. Bootstrapping, transfer learning between stations, and ensembling with rate/energy features can help.
- Entropy should complement, not replace, amplitude- or rate-based indicators and multi-parameter monitoring (deformation, gas, thermal).
