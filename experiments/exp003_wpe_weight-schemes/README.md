# Experiment exp003_wpe_weight-schemes

Goal: compare variance vs. energy weighting (and unweighted PE) for detecting energetic tremor bursts.

- Fix m=4, tau=1; vary weight_strategy in {"variance", "energy"}.
- Evaluate ROC/PR and reliability for each strategy.
- Expected outcome: variance weighting suppresses quiet background, improving precision at low false-alarm rates.

Use the standard pipelines with modified configs; store resulting metrics/figures here.
