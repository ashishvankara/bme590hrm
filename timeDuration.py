def timeDuration(times):
    """ Subtracts the first element of a list from the last.

    This function determines the duration of time that the ECG data was taken.

    Args:
        times (list): List containing floats corresponding to the time of
        each ECG voltage data point

    Returns:
        duration (float): the length of time the ECG data was taken

    """
    duration = times[-1] - times[0]
    return duration

if __name__ == "__main__":
    timeDuration([1, 2, 3, 4, 5])
