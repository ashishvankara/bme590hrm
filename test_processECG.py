import pytest

def test_subtractDC():
    """" Tests subtraction of the average of a list from all the values in the list
    """
    from processECG import subtractDC
    import numpy as np
    a = np.arange(1,11)
    dc_offset = a.mean()
    b = a - dc_offset
    assert pytest.approx(b) == subtractDC(a)

def test_movingAverage():
    """ Tests the application of a moving average window
    """
    from processECG import movingAverage
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [3, 5, 2, 4, 9, 1, 7, 5, 9, 1]
    ymovavg = [3, 4, 3.5, 3., 6.5, 5., 4., 6., 7., 5.]
    assert pytest.approx(movingAverage(x, y, 2)) == ymovavg


if __name__ == "__main__":
    test_subtractDC()
    test_movingAverage()
