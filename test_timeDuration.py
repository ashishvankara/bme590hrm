import pytest


def test_timeDuration():
    """" Tests ecg data extraction of last time point

    Args:

    Returns:

    """
    from readCSV import readCsv
    from timeDuration import timeDuration
    [time, volts] = readCsv('testcsvreaddata.csv')
    t = [0., 0.003, 0.006, 0.008, 0.011]
    v = [-0.145, -0.145, -0.145, -0.145, -0.145]
    assert pytest.approx(timeDuration(time)) == .011


if __name__ == "__main__":
    test_timeDuration()