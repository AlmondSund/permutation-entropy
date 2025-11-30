import yaml
import numpy as np
import pandas as pd

from pevolc.pipelines import train_forecaster


def test_training_pipeline_placeholder(tmp_path):
    # Create synthetic dataset
    rng = np.random.default_rng(0)
    n = 50
    pe_feature = rng.normal(size=n)
    wpe_feature = pe_feature + rng.normal(scale=0.1, size=n)
    label = (pe_feature > 0).astype(int)
    df = pd.DataFrame({"pe": pe_feature, "wpe": wpe_feature, "label": label})
    dataset_path = tmp_path / "dataset.csv"
    df.to_csv(dataset_path, index=False)

    cfg = {
        "dataset_path": str(dataset_path),
        "label_column": "label",
        "model_type": "logreg",
        "model_path": str(tmp_path / "model.joblib"),
        "metrics_path": str(tmp_path / "metrics.csv"),
    }
    cfg_path = tmp_path / "config.yaml"
    cfg_path.write_text(yaml.safe_dump(cfg))

    result = train_forecaster.run_training(cfg_path)
    assert "roc_auc" in result
    assert (tmp_path / "model.joblib").exists()
    assert (tmp_path / "metrics.csv").exists()
