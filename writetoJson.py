
def writetoJson(csvfile, meanhr, voltextremes, duration, beatnum, heartbeattimes):
    """ Writes JSON file with hrm results

    This function writes the calculated hr parameters to
    a JSON file with same name as the data.

    Args:
        :csvfile (string): Name of data file
        :meanhr (float): Calculated mean hr in interval
        :voltextremes (tuple): Tuple of floats corresponding to voltage extrema
        :duration (float): Time duration of data
        :beatnum (int): Number of beats detected in ECG data
        :heartbeattimes (list): List time floats of detected R wave peaks

    Returns:
    """
    import json
    import logging
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
