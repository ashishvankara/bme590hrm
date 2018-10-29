import logging


def readCsv(name):
    """ Reads ECG data from .csv.

    This function extracts ECG data from a csv and stores
    it in the appropriate lists.

    Args:
        :name (string): .csv filename

    Returns:
        t (list): list containing time data from csv file
        v (list): list containing voltage data from csv file

    """

    import numpy as np
    t = np.genfromtxt(name, delimiter=",", usecols=0, dtype=float,
                      missing_values=np.nan)
    logging.debug('Time extraction from CSV successful')
    v = np.genfromtxt(name, delimiter=",", usecols=1, dtype=float,
                      missing_values=np.nan)
    logging.debug('Voltage extraction from CSV successful')
    if len(t) != len(v):
        logging.error("Length of time column is unequal to the"
                      "length of the voltage column")
        raise TypeError("Length of time column is unequal"
                        "to the length of the voltage column")
    for a, val in enumerate(t):
        if np.isnan(t[a]):
            t[a] = (float(t[a - 1]) + float(t[a + 1])) / 2
            logging.warning("Bad time data at index #:%f", a)
    for b, val in enumerate(v):
        if np.isnan(v[b]):
            v[b] = (float(v[b - 1]) + float(v[b + 1])) / 2
            logging.warning("Bad voltage data at index #:%f", b)
    return [t, v]


def recondtiontv(bottombnd, upperbnd, t, v):
    if bottombnd > upperbnd:
        logging.error("Bottom bound must be smaller than upper bound")
        raise TypeError("Bottom bound must be smaller than upper bound")
    nbottom = (t > bottombnd).nonzero()
    tbot = t[nbottom]
    vbot = v[nbottom]
    nupper = (tbot < upperbnd).nonzero()
    adjustedtime = tbot[nupper]
    adjustedvolt = vbot[nupper]
#    if len(adjustedtime) < 100:
#        raise ValueError("Length of data is too short, please modify bounds"
#                         " or pass longer .csv")
#    if len(adjustedtime) != len(t):
#        logging.debug("Partial ECG data is being analyzed")
    return [adjustedtime, adjustedvolt]

if __name__ == "__main__":
    readCsv('baddata.csv')
