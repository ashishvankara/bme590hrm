import logging


def subtractDC(volt):
    """ Subtracts the average of an array from all the values in the array

    This function subtracts off the DC offset within the ECG data.

    Args:
        :volt (list): List of voltages containing floats

    Returns:
        :subvolt (list): List with DC average subtracted

    """
    import numpy as np
    DCVolt = np.mean(volt)
    subvolt = volt - DCVolt
    logging.debug("DC offset was subtracted form voltage data")
    return subvolt


def movingAverage(t, volts, window):
    """ Reduces noise by applying a moving average window

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
    logging.debug("Moving average was applied with a window of %f values",
                  window)
    return lengthenedavg


if __name__ == "__main__":
    from readCSV import readCsv
    import numpy as np
    [t, v] = readCsv(r'test_data10.csv')
    sv = subtractDC(v)
    avgvolt = movingAverage(t, sv, 40)
