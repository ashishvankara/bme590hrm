import logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG)

def main():
    from readCSV import readCsv
    from readCSV import recondtiontv
    from processECG import subtractDC
    from processECG import movingAverage
    from peakDetection import peakDetect
    from timeDuration import timeDuration
    from extVolt import extremeVolt
    from hrcalc import hrCalc
    import matplotlib.pyplot as plt
    import json
    csvfile = r'test_data\test_data1.csv'
    [traw, vraw] = readCsv(csvfile)
    bottomtimebnd = 0
    toptimebnd = 100
    [t, v] = recondtiontv(bottomtimebnd, toptimebnd, traw, vraw)
    svf = subtractDC(v)
    invfssum = 0.0
    for i in range(len(t) - 1):
        invfssum = invfssum + (t[i + 1] - t[i])
    invfs = invfssum / (len(t) - 1)
    movingavgwindow = int(.085/invfs)
    avgvolt = movingAverage(t, svf, movingavgwindow)
    peakindices = peakDetect(t, avgvolt)
    heartbeattimes = t[peakindices].tolist()
    [min, max] = extremeVolt(v)
    voltextremes = (min, max)
    duration = timeDuration(t)
    beatnum = len(peakindices)
    meanhr = hrCalc(peakindices, t)
    metrics = {"Data_file": csvfile,
               "mean_hr_bpm": meanhr,
               "voltage_extremes": voltextremes,
               "duration": duration,
               "num_beats": beatnum,
               "beats": heartbeattimes}
    jsonfile = csvfile.rstrip('csv')
    jsonfile = jsonfile + 'json'
    with open(jsonfile, 'w') as file:
        json.dump(metrics, file)
        logging.info("JSON export complete to %s", jsonfile)
    plt.plot(t, avgvolt)
    plt.plot(t[peakindices], avgvolt[peakindices], 'o')
    plt.show()

if __name__ == "__main__":
    main()