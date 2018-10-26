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

def splineInterp(t, v):
    from scipy.interpolate import CubicSpline
    import matplotlib.pyplot as plt
    cs = CubicSpline(t, v)
    plt.plot(t, v, label="Original")
    plt.plot(t, cs(t,1), label="Spline")
   # plt.plot(t, cs(t, 1), label="S'")
   # plt.plot(t, cs(t, 2), label="S''")
   # plt.plot(t, cs(t, 3), label="S'''")
    plt.legend(loc='lower left', ncol=2)
    plt.show()


if __name__ == "__main__":
    from readCSV import readCsv
    [t,v] = readCsv(r'test_data\test_data10.csv')
    visualizeSignal(t,v)
#    sv = subtractDC(v)
#    visualizeSignal(t, sv)
#    svf = savgolFilter(sv)
#    visualizeSignal(t, svf)
    splineInterp(t,v)


