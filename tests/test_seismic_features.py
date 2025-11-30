import numpy as np

from pevolc.features import WindowConfig, extract_basic_features, extract_entropy_features


def test_extract_basic_features_placeholder():
    features = extract_basic_features([1, 2, 3])
    assert set(features.keys()) == {"mean", "std", "rms", "max", "min"}


def test_extract_entropy_features_dataframe_shape():
    sampling_rate = 10.0
    t = np.arange(0, 30, 1 / sampling_rate)
    signal = np.sin(2 * np.pi * 0.5 * t)
    cfg = WindowConfig(window_seconds=5.0, step_seconds=5.0, order=3, scales=2)
    df = extract_entropy_features(signal, sampling_rate, cfg)
    assert not df.empty
    assert {"pe", "wpe", "mpe_scale_1", "mpe_scale_2"}.issubset(df.columns)
