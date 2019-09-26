import math


def mean(data):
    """ This is used to find the mean in a set of data. The mean is commonly referred to as the 'average'."""

    data = data
    sum = 0
    for x in data:
        sum += x
    return sum/len(data)

    def __repr__(): "Mean(enter data here)"




def range(data):
    """ This is used to find the range of a set of data. The range is the difference between the lowest and highest valued digits in a given set of data."""

    data = data
    data.sort()
    return data[len(data)-1] - data[0]


def median(data):
    """ This is used to find the median in a set of data. The median is the number that is exactly 'in the middle' of a set of data"""
    data = data
    data.sort()
    #We check to see if the N of our data is even or odd. If the modulas of our data is 0, that would mean that our N is an even number. But that same 0 results in a "false"...
    if len(data)%2 == 1:
        return data[int(math.floor(len(data))/2)]
    else:
        return (data[int((len(data))/2)]+ data[int((len(data))/2)-1] )/2



def mode(data):
    """ This finds the thing that we find "most" often. """
    data = data
    data.sort()
    mostOften = False
    for x in data:
        if data.count(x) > data.count(mostOften):
            mostOften = x
        elif data.count(x) == data.count(mostOften):
            mostOften = False

    return mostOften





def percentile(data,percent):
    """This finds what data point is found at a given percentile. Percentile should be given as a float."""
    data = data
    percent = percent
    data.sort()
    if percent > 0.999:
        return "We don't allow 100% percentiles...That would mean you are greater than 100% of the data. You cannat be greater than yourself!"
    else:
        return data[int(math.ceil(percent*len(data)))]








def fMean(Y,frequency):
    """ Both of these values should be arrays. This is used to find the mean of a set of data that utilizes frequencies to measure how often something occurs..."""
    Y = Y
    frequency = frequency
    sum = 0
    N = 0
    if len(Y) == len(frequency):
        i = 0
        while i < len(Y):
            sum += (Y[i]*frequency[i])
            N += frequency[i]
            i += 1

        return sum/N
    else:
        return "Y and Frequency do not have the same amount of measurements."


def iqv(data):
    """Data in this case should be a list of percentages adding up to 100%. IQV is used to measure qualative variation found in the measurment of nominal data. For example the different percentages of ethnicities found in state."""
    data = data
    k = len(data)
    sum = 0
    for i in data:
        sum += (i**2)
    return (k*(100**2-sum))/((100**2)*(k-1))


def variation(data):
    data = data
    sum = 0
    for i in data:
        sum += ((i-mean(data))**2)
    return sum / (len(data)-1)

def stanDev(data):
    return math.sqrt(variation(data))

def iqr(data):
    """ The interquartile range measures the range between the the upper and lower quartiles of a set of data, thus measuring the width of the middle 50% of the distribution."""
    data = data
    return percentile(data,.75)-percentile(data,.25)

def rawToZ(rawScore,data):
    rawScore = rawScore
    data = data
    return (dataPoint - mean(dataSet)) / stanDev(dataSet)

def zToRaw(zScore,data):
    zScore = zScore
    data = data
return mean(data) + (zScore * stanDev(data))

def zScoreProps(zScore)
    zScore = zScore
    snt = {

    "0.00":[0.0000,0.5000],
    "0.01": [0.0040,0.4960],
    "0.02" : [0.0080,0.4920],
    "0.03"
    "0.05"
    "0.06"
    "0.07"
    "0.08"
    "0.09"
    "0.10"
    "0.11"
    "0.12"
    "0.13"
    "0.14"
    "0.15"
    "0.16"
    "0.17"
    "0.18"
    "0.19"
    "0.20"
    "0.21"
    "0.20"


     }
    pass 
