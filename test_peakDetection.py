
def test_peakDetect():
    """" Tests R wave peak detection from ECG data.

    """
    from peakDetection import peakDetect
    from readCSV import readCsv
    from processECG import movingAverage
    from processECG import subtractDC
    [t, v] = readCsv(r'test_data1.csv')
    svf = subtractDC(v)
    invfssum = 0.0
    for i in range(len(t) - 1):
        invfssum = invfssum + (t[i + 1] - t[i])
    invfs = invfssum / (len(t) - 1)
    movingavgwindow = int(.085 / invfs)
    avgvolt = movingAverage(t, svf, movingavgwindow)
    peaks = peakDetect(t, avgvolt)
    correctbeatnum = 36
    assert len(peaks) == correctbeatnum
