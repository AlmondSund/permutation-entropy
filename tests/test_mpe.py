import numpy as np

from pevolc.entropy import mpe, pe


def test_compute_mpe_returns_per_scale():
    signal = np.linspace(0, 1, 50)
    entropies = mpe.compute_mpe(signal, scales=3, order=3, delay=1, base=2)
    assert len(entropies) == 3
    assert entropies[0] == pe.compute_pe(signal, order=3, delay=1, base=2)

def test_compute_mpe_placeholder():
    assert callable(mpe.compute_mpe)
