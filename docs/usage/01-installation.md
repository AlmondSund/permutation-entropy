# Installation

The toolkit targets Python 3.11+ and depends on NumPy/SciPy, pandas, scikit-learn, and ObsPy (for SAC/miniSEED reading).

## Clone and install
```bash
git clone https://github.com/AlmondSund/permutation-entropy.git
cd permutation-entropy
pip install -e .
```
If you prefer pinned versions, use:
```bash
pip install -r requirements.txt
```

## Optional extras
- **Docs**: `pip install -e .[docs]` installs MkDocs + Material and the PDF plugin to build the HTML/PDF documentation.
- **Dev/testing**: `pip install -e .[dev]` adds formatting, linting, and pytest.

## Environments and data
- A conda environment is described in `environment.yml` if you prefer conda/mamba.
- GPU/CUDA are not required; computations are CPU-only.
- Example configs live in `configs/`; example raw data can be downloaded via `scripts/download_example_data.py` (or swap in your own miniSEED/SAC files).

## Build the docs
```bash
pip install -e .[docs]
mkdocs serve        # live preview at http://127.0.0.1:8000
mkdocs build        # HTML output in site/
```
To render a MathJax-aware PDF, use the separate PDF config and a Chromium installation:
```bash
# needs mkdocs-pdf-export-plugin and a local Chromium/Chrome
mkdocs build -f mkdocs-pdf.yml
```
This writes a combined PDF at `site/pdf/permutation-entropy-docs.pdf`. Set `chromium_executable` in `mkdocs-pdf.yml` if Chromium/Chrome lives elsewhere.

Keep Markdown under `docs/theory/` as the canonical source; copy relevant passages into `docs/paper/main.tex` only when producing a paper-grade PDF.
