
def hrCalc(peakind,t):
    """ Determines the average HR over a specified interval

    This function determines average number of beats/minute over
    a specified interval

    Args:
        :peakind (list): List of indices corresponding to peaks of the R wave

    Returns:
        :avghr (float): Average number of beats/minute
    """
    from timeDuration import timeDuration
    timedur = timeDuration(t)
    avghr = (len(peakind) / timedur) * 60
    return avghr

if __name__ == "__main__":
    hrCalc()
