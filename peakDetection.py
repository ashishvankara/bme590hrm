from scipy import signal
import numpy as np


def peakDetect(t, v):
    """ Detects R wave peaks from processed ECG data

    This function identifies R wave peaks using the continuous
    wavelet transform

    Args:
        :t (list): List of ECG time floats
        :v (list): List of processed ECG voltage floats.

    Returns:
        :peakind (list): List of integer indices corresponding to peaks
         in input lists.
    """
    peakind = signal.find_peaks_cwt(v, np.arange(20, 40, .1))
    return peakind

if __name__ == "__main__":
    from readCSV import readCsv
    from processECG import subtractDC
    from processECG import savgolFilter
    from processECG import movingAverage
    import matplotlib.pyplot as plt
    [t, v] = readCsv(r'test_data4.csv')
    sv = subtractDC(v)
    svf = savgolFilter(sv)
    avgvolt = movingAverage(t, svf, 30)
    peaks = peakDetect(t, avgvolt)
    plt.plot(t, avgvolt)
    plt.plot(t[peaks], avgvolt[peaks], 'o')
    plt.show()
