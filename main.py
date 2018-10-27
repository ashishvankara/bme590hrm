import logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG)

def main():
    from readCSV import readCsv
    import json
    from processECG import subtractDC
    from processECG import savgolFilter
    from processECG import movingAverage
    from extVolt import extremeVolt
    from timeDuration import timeDuration
    [t,v] = readCsv(r'test_data\test_data1.csv')
    sv = subtractDC(v)
    svf = savgolFilter(sv)
    avgvolt = movingAverage(t, svf, 30)
    peaks = peakDetect(t, avgvolt)
    plt.plot(t, avgvolt)
    plt.plot(t[peaks], avgvolt[peaks], 'o')
    plt.show()
    #visualizeSignal(t,v)


if __name__ == "__main__":
    main()