import logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG)

def main():
    from readCSV import readCsv
    csvfile = r'test_data\test_data1.csv'

    [t, v] = readCsv(csvfile)
    bottomtimebnd = 0
    toptimebnd =

    import json
    from processECG import subtractDC
    from processECG import savgolFilter
    from processECG import movingAverage
    from extVolt import extremeVolt
    from timeDuration import timeDuration

    sv = subtractDC(v)
    svf = savgolFilter(sv)
    avgvolt = movingAverage(t, svf, 30)
    peaks = peakDetect(t, avgvolt)
    plt.plot(t, avgvolt)
    plt.plot(t[peaks], avgvolt[peaks], 'o')
    plt.show()

if __name__ == "__main__":
    main()