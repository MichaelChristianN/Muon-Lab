import numpy as np
import matplotlib.pyplot as plt

## Reads a data file and returns a sorted array of valid times
def parseFile(file):
    with open(file) as file_object:
        lines = file_object.readlines()

    valid_times = []

    ## read line by line and grab any data less than 4000
    for line in lines:
        numbers = line.split()
        if int(numbers[0]) < 40000: #TODO move out magic number
            valid_times.append(int(numbers[0]))

    valid_times.sort()
    return valid_times

## Put our data in to bins of a given size
def binData(dataSet, binsize):
    ## 4000 is a max, so we'll break up the data set into chunks based on binsize
    bincount = int(40000 / binsize)
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
def plotData(data):
    ## matplotlib boilerplate
    xdata, ydata = zip(*data.items())

    x = np.array(xdata)
    y = np.array(ydata)

    plt.plot(x, y, linestyle='--')

    ## an expontial fucntion to check our data

    plt.show()

def main(file, binsize):
    times = parseFile(file)
    binnedData = binData(times, binsize)
    plotData(binnedData)

main('../data/muon 1-31-21.data', 50)
