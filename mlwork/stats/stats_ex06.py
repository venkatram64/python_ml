from itertools import permutations

import numpy as np
from scipy.stats import skew
from scipy.stats import kurtosis

import matplotlib.pyplot as plt

"""
Moments:
Quantitative measures of the shape of a probability density function
Mathematically they are a bit hard to wrap your hear around

The first moment is the mean.
The second moment is the variance
The third moment is the skew
how losided is the distribution
A distribution with a longer tail on the left
will be skewed left, and have a negative skew.
The fourth moment is "kurtosis"
How thick is the tail, and how shar is the peak,
compared to a normal distribution.
eg: higher peaks have higher kurtosis
"""

vals = np.random.normal(0, 0.5, 10000)

plt.hist(vals, 50)
plt.show()

first_mean = np.mean(vals)

print("First moment is the mean: {}".format(first_mean))

second_variance = np.var(vals)

print("Second moment is the variance: {}".format(second_variance))

third_moment = skew(vals)
print("Third moment is the Skew {}".format(third_moment))

fourth_moment = kurtosis(vals)
print("Fourth moment is the kurtosis {}".format(fourth_moment))