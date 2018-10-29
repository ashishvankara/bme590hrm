import pytest


def test_csvREAD():
    """" Tests ecg data extraction from .csv.

    """
    from readCSV import readCsv
    [time, volts] = readCsv('testcsvreaddata.csv')
    [timea, voltsa] = readCsv('baddata.csv')
    print(timea)
    correctt = [0., 0.003, 0.006, 0.008, 0.011]
    correctv = [-0.145, -0.145, -0.145, -0.145, -0.145]
    correctva = [-.145, -.145, -.145, -.145, -.145, -.145]
    correctta = [0, 0.003, 0.006, 0.008, .011, 0.014]
    assert pytest.approx(time) == correctt
    assert pytest.approx(volts) == correctv
    assert pytest.approx(timea) == correctta
    assert pytest.approx(voltsa) == correctva


def test_recondtiontv():
    """" Tests user input of time interval
    """
    import numpy as np
    t = np.arange(1, 11)
    v = np.arange(2, 12)
    from readCSV import recondtiontv
    [tadj, vadj] = recondtiontv(3, 7, t, v)
    correctadjt = [4, 5, 6]
    correctadjv = [5, 6, 7]
    assert pytest.approx(tadj) == correctadjt
    assert pytest.approx(vadj) == correctadjv

if __name__ == "__main__":
    test_csvREAD()
    test_recondtiontv()
