import numpy as np

from pevolc.entropy import pe


def test_compute_pe_constant_signal_zero_entropy():
    signal = np.ones(20)
    value = pe.compute_pe(signal, order=3, delay=1, base=2)
    assert value == 0.0


def test_compute_pe_noise_high_entropy():
    rng = np.random.default_rng(42)
    signal = rng.normal(size=2000)
    value = pe.compute_pe(signal, order=3, delay=1, base=2)
    assert 0.8 < value <= 1.0

def test_compute_pe_placeholder():
    assert callable(pe.compute_pe)
