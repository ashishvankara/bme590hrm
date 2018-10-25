import logging


def readCsv(name):
    """ Read ECG data from .csv

    This function extracts ECG data from a csv and stores
    it in the appropriate lists.


    Args:
        :name (string): .csv filename
    Returns:
        :t (list): list containing time data from csv file
        :v (list): list containing voltage data from csv file
    """

    import numpy as np
    t = np.genfromtxt(name, delimiter=",", usecols=0, dtype=None)
    logging.info('Time extraction from CSV successful')
    v = np.genfromtxt(name, delimiter=",", usecols=1, dtype=None)
    logging.info('Voltage extraction from CSV successful')
    if len(t) != len(v):
        logging.error("Length of time column is unequal to the"
                      "length of the voltage column")

        raise TypeError("Length of time column is unequal"
                        "to the length of the voltage column")
    print(t)
    print(v)
    return [t, v]


if __name__ == "__main__":
    readCsv('testcsvreaddata.csv')