import matplotlib


def visualizeSignal(t,v):
    """ Plots voltage vs. time

    This function plots the ECG data as voltage vs. time

    Args:
        :volts (list): List of voltages containing floats

    Returns:
    """
    import matplotlib.pyplot as plt
    plt.plot(t, v)
    plt.show()

def subtractDC(volt):
    """ Subtracts the average of an array from all the values in the array

    This function subtracts the DCoffset within ECG data.

    Args:
        :volts (list): List of voltages containing floats

    Returns:
        :subvolt (list): List with DC average subtracted

    """
    import numpy as np
    DCVolt = np.mean(volt)
    subvolt = np.array(volt) - DCVolt
    return subvolt

def savgolFilter(volt):
    """ Smooths the input signal by applying a Savitsky Golay filter

     Args:
        :volt (list): List of ECG voltage floats
     Returns:
        :filtereddata (list): List of filtered voltage floats
    """
    from scipy.signal import savgol_filter
    filtereddata = savgol_filter(volt, 19, 7)
    return filtereddata

def movingAverage(t,volts, window):
    """ Reduces noise by applying a moving average

     Args:
        :t (list): List of ECG time floats
        :volts (list): List of ECG voltage floats
        :window (int): Size of moving average window
     Returns:
        :lengthenedavg (list): List of moving average voltage floats
    """
    import numpy as np
    from numpy import convolve
    bleh = np.repeat(1.0, window) / window
    movingavg = np.convolve(volts, bleh, 'valid')
    lengthenedavg = np.append(volts[:len(t) - len(movingavg)], movingavg)
    return lengthenedavg

if __name__ == "__main__":
    from readCSV import readCsv
    import numpy as np
    [t,v] = readCsv(r'test_data\test_data10.csv')
#    visualizeSignal(t,v)
    sv = subtractDC(v)
    svf = savgolFilter(sv)
    avgvolt =movingAverage(t, svf, 40)
#    visualizeSignal(t, avgvolt)
    splineInterp(t, avgvolt, 1)




