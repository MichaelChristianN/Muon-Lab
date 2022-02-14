import numpy as np
import matplotlib.pyplot as plt
import sys

# time axis is nano seconds

time_out = 40000 # any time after this isn't recorded, they should be ignored

## Reads a data file and returns a sorted array of valid times
def parseFile(file):
    with open(file) as file_object:
        lines = file_object.readlines()

    valid_times = []

    ## read line by line and grab any data less than 4000
    for line in lines:
        numbers = line.split()
        if int(numbers[0]) < time_out: #TODO move out magic number(done?)
            valid_times.append(int(numbers[0]))

    valid_times.sort()

## DEBUG
    ##print(valid_times)
##
    return valid_times

## Put our data in to bins of a given size
def binData(dataSet, binsize):
    ## 4000 is a max, so we'll break up the data set into chunks based on binsize
    bincount = int(time_out / binsize)
    counter = {}

    ## So counter will be a dict counting how man data points were in each bin
    ## looking like {0: 10, 100: 23, 200: 34,...}
    for i in range(bincount):
        counter[binsize * i] = 0

    currentBin = 0
    iteration = 0

    ## Look through our data and count up the points into bins
    ## Its sorted so we once we found an out of range bin
    ## we just move on to the next largest
    for data in dataSet:
        if data >= currentBin and data < currentBin + binsize:
            counter[currentBin] = counter[currentBin] + 1
        else:
            ## without this we would skip the first data point for each bin
            counter[currentBin + binsize] = counter[currentBin + binsize] + 1
            currentBin = currentBin + binsize

    return counter

## Data is expected to be a dict of type int, int
def plotData(data, file_name):
    ## matplotlib boilerplate
    xdata, ydata = zip(*data.items())

    x = np.array(xdata)
    y = np.array(ydata)

    plt.plot(x, y)

    plt.title(file_name)

    ## an expontial fucntion to check our data

    plt.show()

def main(files, binsize):
    for file in files :
        times = parseFile(str(file))
        binnedData = binData(times, binsize)
        plotData(binnedData, str(file))

# the device measures in increments of 20, so if the bin size is not a multiple of 20
# the bins get skewed
# we can change the bin number in the measuring program

main(sys.argv[1:], 20)
