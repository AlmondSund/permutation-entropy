# Experiment exp002_mpe_multiband

Goal: test whether multiscale PE across coarse-grained levels improves discrimination between tremor-like signals and broadband noise.

- Vary scales: 1–7
- Embedding: m=4, tau=1
- Features: `mpe_scale_*` plus PE/WPE
- Model: gradient boosting

Run:
```bash
python scripts/compute_entropy_dataset.py configs/example_compute.yaml
python scripts/train_model.py configs/example_train.yaml
```
Store metrics and plots under this directory (figures/).
