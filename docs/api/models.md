# Models API

## `PermutationEntropyForecaster`
- `fit(X, y)` – trains a classifier (logreg, random_forest, gradient_boosting) with optional Platt calibration.
- `predict_proba(X)` – calibrated eruption probabilities.
- `predict_alert_level(X, thresholds=(0.33,0.66))` – green/yellow/red mapping.

## Calibration
- `PlattCalibrator` – logistic regression on raw probabilities.
- `calibrate_probabilities(probs, labels)` – convenience helper.

## Metrics
- `evaluate_auc(model, X, y)` – ROC-AUC on provided data.
