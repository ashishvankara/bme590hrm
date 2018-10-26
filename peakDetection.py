from scipy import signal
import numpy as np

def peakDetect(t, v):
    invfssum = 0.0
    for i in range(len(t) - 1):
        invfssum = invfssum + (t[i + 1] - t[i])
    invfs = invfssum / (len(t) - 1)
    width = 1.4/invfs
    peakind = signal.find_peaks_cwt(v, np.arange(1,width))
    print(peakind)
    print(t[peakind])
    print(v[peakind])

if __name__ == "__main__":

    from readCSV import readCsv
    from processECG import
    [t, v] = readCsv(r'test_data\test_data10.csv')
    xs = np.arange(0, 10*np.pi, 0.05)
    data = np.sin(xs)
    import matplotlib.pyplot as plt
    fun(t, v)
    plt.plot(t, v)
    plt.show()