import matplotlib


def visualizeSignal(t,v):
    """ Determines the min and max elements of a list

    This function determines the min and max voltages of an ECG data
    set

    Args:
        :volts (list): List of voltages containing floats

    Returns:
        :min (float): minimum ECG voltage
        :max (float): maximum ECG voltage
    """
    import matplotlib.pyplot as plt
    plt.plot(t, v)
    plt.show()

def subtractDC(volt):
    """ Determines the min and max elements of a list

    This function determines the min and max voltages of an ECG data
    set

    Args:
        :volts (list): List of voltages containing floats

    Returns:
        :min (float): minimum ECG voltage
        :max (float): maximum ECG voltage
    """
    import numpy as np
    import matplotlib.pyplot as plt
    DCVolt = np.mean(volt)
    subvolt = np.array(volt) - DCVolt
    return subvolt

def savgolFilter(volt):
    """Smooths the signal by applying a Savitsky Golay filter

     Args:
        :param self: hrmData Object
        :param data: voltage with DC subtracted
     Returns:
        list of voltage values, filter applied
    """
    from scipy.signal import savgol_filter
    return savgol_filter(volt, 19, 7)


if __name__ == "__main__":
    from readCSV import readCsv
    [t,v] = readCsv(r'test_data\test_data25.csv')
    visualizeSignal(t,v)
    sv = subtractDC(v)
    visualizeSignal(t, sv)
    svf = savgolFilter(sv)
    visualizeSignal(t, svf)


