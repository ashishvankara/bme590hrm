
def extremeVolt(volts):
    """ Determines the min and max of a list

    This function determines the min and max voltages of an ECG data
    set

    Args:
        :volts (list): List of voltages containing floats

    Returns:
        :min (float): minimum ECG voltage
        :max (float): maximum ECG voltage
    """
    volts.sort()
    print(volts)
    max = volts[-1]
    min = volts[0]
    return [min, max]

if __name__ == "__main__":
    extremeVolt([5, 8, -13, 8, 79, -.89])
