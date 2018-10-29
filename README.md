# bme590hrm
Heart Rate Monitor Assignment 2018 [1.0.0]
##Status Badge:
![alt text](https://travis-ci.com/ashishvankara/bme590hrm.svg?branch=master "Status Badge")


## Introduction

The goal of this software is to take input ECG data (.csv), calculate the paramaters listed below, and write the data as a dictionary to a JSON file.

    - `mean_hr_bpm`: estimated average heart rate over a user-specified number
      of minutes (can choose a default interval)
    - `voltage_extremes`: tuple containing minimum and maximum lead voltages
    - `duration`: time duration of the ECG strip
    - `num_beats`: number of detected beats in the strip
    - `beats`: numpy array of times when a beat occurred


## Code

The software package is separated into the following files: 

- main.py: This script runs all the functions to obtain the relevant data and writes to a JSON file.
- extVolt.py: Contains a function that determines the min and max voltages of an ECG data set.
- hrcalc.py: Contains a function that determines average number of beats/minute over a specified interval of ECG data.
- peakDetection.py: Contains a function that identifies R wave peaks using the continuous wavelet transform.
- processECG.py: Contains the functions to subtract the data's DC offset and smooth the data by applying a moving average.
- readCSV.py: Contains the functions to read ECG data from a csv and allow for user-input modulation of time interval.
- timeDuration.py: Contains a function that determines the duration of time of an ECG strip.
- writetoJson.py: Contains a function that writes the calculated hr parameters to a JSON file with same name as the data.
- Unit Tests: Several are included for adequate test coverage.


# Possible areas of improvement

The continuous wavelet transform method for peak detection requires a different CWT matrix for every ECG strip. Perhaps a better strategy would be to cross-correlate a clean ECG strip with a prominent QRS wave.

# License

MIT License

Copyright (c) [2018] [Ashish Vankara]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
