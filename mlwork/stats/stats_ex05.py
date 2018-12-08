from itertools import permutations

import numpy as np
from scipy.stats import norm
from scipy.stats import expon
from scipy.stats import binom
from scipy.stats import poisson

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

percentile = np.percentile(vals, 50)

print(percentile)

percentile = np.percentile(vals, 90)

print(percentile)

percentile = np.percentile(vals, 20)

print(percentile)