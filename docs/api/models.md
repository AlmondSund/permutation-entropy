# Models, I/O, and Pipelines API

## `pevolc.models.PermutationEntropyForecaster`
Wrapper around scikit-learn classifiers with optional Platt calibration.
- `model_type`: `"logreg"`, `"random_forest"`, or `"gradient_boosting"`.
- `fit(X, y)`: trains and, if `calibrate=True`, learns a calibration transform using a held-out split.
- `predict_proba(X)`: calibrated eruption probabilities.
- `predict_alert_level(X, thresholds=(0.33, 0.66))`: green/yellow/red based on probability thresholds.
- Helpers: `train_forecasting_model(features, labels, model_type="logreg")`, `predict_proba(model, features)`, and `evaluate_auc(model, features, labels)`.

## Calibration utilities
- `PlattCalibrator(max_iter=200)`: fit logistic calibration on raw probabilities (`fit`, then `transform`).
- `calibrate_probabilities(probs, labels)`: one-liner to fit and apply `PlattCalibrator`.

## I/O helpers (`pevolc.io`)
- `read_waveform(path) -> (data, sampling_rate)`: load miniSEED/SAC via ObsPy.
- `load_waveforms(paths)`: convenience wrapper to read multiple files.

## Pipelines (`pevolc.pipelines`)
- `compute_entropy_dataset(data_paths, output_path, cfg)`: run sliding-window entropy extraction on multiple files, apply optional band-pass, infer labels, and save a CSV.
- `run_from_config(config_path)`: load YAML and call `compute_entropy_dataset`.
- `run_training(config_path)`: load dataset CSV, split into train/validation (time-aware or random), fit a `PermutationEntropyForecaster`, write metrics, calibration curves, and the model artifact.

The command-line interface in `pevolc.cli` exposes `compute-entropy` and `train` commands that dispatch to these pipeline functions.
