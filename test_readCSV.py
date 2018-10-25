import pytest


def test_csvREAD():
    """ Tests ecg data extraction from .csv

    Args:

    Returns:

    """
    from readCSV import readCsv
    [time, volts] = readCsv('testcsvreaddata.csv')
    correctT = [0., 0.003, 0.006, 0.008, 0.011]
    correctV = [-0.145, -0.145, -0.145, -0.145, -0.145]
    assert pytest.approx(time) == correctT
    assert pytest.approx(volts) == correctV



if __name__ == "__main__":
    test_csvREAD()























