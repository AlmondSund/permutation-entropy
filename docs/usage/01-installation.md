# Installation

## Requirements
- Python 3.11+
- numpy, scipy, pandas, scikit-learn
- ObsPy (for SAC/miniSEED reading)

## Quick setup
```bash
git clone https://github.com/AlmondSund/permutation-entropy.git
cd permutation-entropy
pip install -r requirements.txt
```
Or install in editable mode:
```bash
pip install -e .
```

For reproducible environments, use the provided `environment.yml` or create a fresh virtualenv. GPU/CUDA are not required; computations are CPU-only.
