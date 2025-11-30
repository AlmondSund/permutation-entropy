from pevolc.features import seismic_features

def test_extract_basic_features_placeholder():
    assert callable(seismic_features.extract_basic_features)
