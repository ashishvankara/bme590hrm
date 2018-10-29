import pytest


def test_hrcalc():
    """" Tests average hr calculation.

    """
    import numpy as np
    from hrcalc import hrCalc
    peakind = np.arange(1, 61)
    t = np.arange(0, 61)
    print(t)
    assert pytest.approx(hrCalc(peakind, t)) == 60

if __name__ == "__main__":
    test_hrcalc()
