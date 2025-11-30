import numpy as np

from pevolc.entropy import wpe


def test_compute_wpe_constant_signal_zero_entropy():
    signal = np.ones(20)
    value = wpe.compute_wpe(signal, order=3, delay=1, base=2)
    assert value == 0.0


def test_compute_wpe_energy_weights_matches_range():
    rng = np.random.default_rng(123)
    signal = rng.normal(size=200)
    value = wpe.compute_wpe(signal, order=4, delay=1, base=2, weight_strategy="energy")
    assert 0.0 <= value <= 1.0

def test_compute_wpe_placeholder():
    assert callable(wpe.compute_wpe)
