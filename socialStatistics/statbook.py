import math
import random

#Random set of data so I don't have to make one everytime I debug...


def createRandData(sampleSize,low,high):
    """ This is used to quickly make a test data set so I can make sure my other functions work properly. Sample Size is the "N" of your dataset. You then add a high or low to the data set. """
    sampleSize = sampleSize
    low = low
    high = high
    data = []
    for x in range(sampleSize):
        data.append(random.randint(low,high))

    return data

def createRandSample(data,n):
    sample = []
    data = data
    n = n
    for x in range(n):
        sample.append(data[random.randint(0,(len(data)-1))])
    return sample



def mean(data):
    """ This is used to find the mean in a set of data. The mean is commonly referred to as the 'average'."""

    data = data
    sum = 0
    for x in data:
        sum += x
    return sum/len(data)

    def __repr__(): "Mean(enter data here)"




def dataRange(data):
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
    """ Finds how much the data in our data set varies from one n to another. """
    data = data
    sum = 0
    for i in data:
        sum += ((i-mean(data))**2)
    return sum / (len(data)-1)

def stanDev(data):
    """ Finds the average amount of difference between each data point by scquaring the variation. """
    return math.sqrt(variation(data))

def iqr(data):
    """ The interquartile range measures the range between the the upper and lower quartiles of a set of data, thus measuring the width of the middle 50% of the distribution."""
    data = data
    return percentile(data,.75)-percentile(data,.25)

def rawToZ(rawScore,data):
    """Takes a score from a set of data and determines what it's Z score is. Z score basically describes howo many deviations something is from the mean of the data set.  """
    rawScore = rawScore
    data = data
    return (rawScore - mean(data)) / stanDev(data)

def zToRaw(zScore,data):
    """Takes a Z score and tells you what data point would it be found on in a set of data."""
    zScore = zScore
    data = data
    return mean(data) + (zScore * stanDev(data))


def zTable(x):

    """ This doesn't really make sense to me yet. I took this code from a data science article. Unfortunately my book doens't include in information about how the z table was actual caluculated, it simply just give us a Z table. This entire thing needs to be scrapped and re-made. """
    x = []
    y = []
    i = -4
    while i<4:
        i+=0.01
        x.append(round(i,3))

    constant = 1.0 / math.sqrt(2*math.pi)
    standard_normal_curve = constant*(math.e**math.exp((-x**2)/2))
    return standard_normal_curve



# Sampling Size Things.


def sampleDistribution(data,totalSamples,n):
    """ This is used to take a distribution of possible samples. It is a theoretical mean of this distribution that can then be used to make estimations of our population based off of a sample. To put it simple. This funciton will give you the mean of a sampling distribution of means. Assumes that the data given is the population. Creates samples for that population. Retrieves the means of those samples. """
    counter = 0
    sampleMeans = []
    n = n
    data = data
    totalSamples = totalSamples

    while counter < totalSamples:
        currentSample = []
        for x in range(n):
            currentSample.append(data[random.randint(0,(len(data)-1))])
        sampleMeans.append(mean(currentSample))
        counter += 1

    return sampleMeans


def standardError(sampleDeviation,n):
    """This will find the sampling distribution's standard deviaton. In the book it is found under the section that explains the 'Central Limit Theorem'. Enter a standard deviation and a sample size (N). This can be used to make an estimation when we dont know our populations values as long as N>50. """
    sampleDeviation = sampleDeviation
    n = n

    return sampleDeviation/math.sqrt(n)



def confidenceInterval(sample,zScore):
    """ This function will give us the confidence interval for the means of our sample distribution. Enter in the sample data as a list and the Z as a float. Traditonally the Z will be either 1, 1.96, or 2.58, which corresponds with a 68%,95% or 99% confidence level. """

    sample = sample
    zScore = zScore
    sE = standardError(stanDev(sample),len(sample))
    cIPositive = mean(sample) + (zScore*sE)
    cINegative = mean(sample) - (zScore*sE)

    return "{} to {}".format(cINegative,cIPostives)


def zStatistic(sampleMean, standardError, deviation,N):
    """This formula in the book  contains a lot of variables that we don't often have"""

    pass 
