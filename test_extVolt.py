import pytest


def test_extVolt():
    """" Tests extraction of maxima and minima from a list.

    """
    from extVolt import extremeVolt
    testvoltage = [95.-.0034, -67, 420, 689, .089, .04689, -.002, 0, 432, 10,
                   1, -34, -51, 10]
    [min, max] = extremeVolt(testvoltage)

    assert pytest.approx(min) == -67
    assert pytest.approx(max) == 689


if __name__ == "__main__":
    test_extVolt()
