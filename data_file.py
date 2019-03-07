import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

class data_file:

    # initialize object of class data
    def __init__(self, filename):
        self.filename = filename
        self.time = []
        self.data = []
        self.itime = []
        self.idata = []

    # function to read thru file and add information to data and time
    def read(self):
        with open(self.filename,'r') as f:
            for line in f:
                if(line[0] is not '='):
                    line_split = line.split(';')
                    if (len(line_split) != 6):
                        continue
                    self.time.append(float(line_split[0]))
                    self.data.append(float(line_split[1]))

    # function to find index of point just before 0.5ml/min
    # returns: index in data just before flow is > 0.5ml/min
    def just_before_pointfive(self):
        for x in self.data:
            if (x > 1):
                return (self.data.index(x) - 1)
            else:
                continue

    # function to remove time and data points so the arrays start at 'just before the 0.5'
    # and reset time so that it starts at 0
    def align(self):
        if (len(self.time) == 0):
            self.read()

        indexbefore5 = self.just_before_pointfive()

        self.time = np.array(self.time[indexbefore5:])
        self.data = np.array(self.data[indexbefore5:])

        shift = self.time[0]

        for i in range(len(self.time)):
            self.time[i] = self.time[i] - shift

    # function that interpolates data at consistent time intervals (20 measurements a second)
    def interpolate(self):
        if (len(self.time) == 0):
            self.read()
            self.align()

        self.itime = np.linspace(0, 5, 300)
        self.idata = np.interp(self.itime, self.time, self.data)

    # function that plots (but doesn't show) the regular data in a file
    # params: marker colour and size in 'format'
    def plot(self, format):
        if (len(self.time) == 0):
            self.read()
            self.align()
        plt.plot(self.time, self.data, format, markersize = 1)

    # function that plots (but doesn't show) the interpolated data from the given file
    # params: marker colour and size in 'format'
    def interp_plot(self, format):
        if (len(self.time) == 0):
            self.read()
            self.align()
        self.interpolate()
        plt.plot(self.itime, self.idata, format, markersize = 1)
