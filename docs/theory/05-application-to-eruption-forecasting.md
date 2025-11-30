# Applying Entropy Methods to Eruption Forecasting

Entropy features summarise waveform complexity and can signal dynamical shifts. A basic workflow:

1. **Stream & preprocess**: detrend, bandpass, resample, and standardise continuous traces.
2. **Window & compute**: run PE/WPE/MPE on overlapping windows (e.g., 10–60 s).
3. **Aggregate features**: combine recent windows (last few minutes) as inputs.
4. **Forecast**: train a probabilistic classifier to estimate eruption likelihood over a horizon (e.g., 10–60 minutes ahead).

## Physical interpretations
- Rising entropy with rising energy may indicate fracturing or turbulent degassing.
- Falling entropy with rising energy often corresponds to emergent, quasi-harmonic tremor.
- Divergence across scales (MPE) highlights simultaneous tremor and transient bursts.

## Alerting and calibration
- Map calibrated probabilities to alert levels (green/yellow/red) with adjustable thresholds.
- Use Platt scaling or isotonic regression to align probabilities with observed frequencies.

## Validation
- Employ time-based splits (train on early data, validate on later) to respect causality.
- Report ROC/PR curves, reliability diagrams, and lead-time metrics (how early alerts arrive before eruptions).
- Track false-alarm rate per day/week to reflect operational costs.

## Limitations and caveats
- Eruptions are rare; labels are uncertain. Bootstrapping and transfer learning can help.
- Site effects are strong; per-station tuning of :math:`m`, :math:`\\tau`, and scale ranges is expected.
- Entropy should complement, not replace, amplitude- or rate-based indicators and multi-parameter monitoring.
