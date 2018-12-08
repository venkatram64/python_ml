from itertools import permutations

import numpy as np
from scipy.stats import norm
from scipy.stats import expon
from scipy.stats import binom
from scipy.stats import poisson

import matplotlib.pyplot as plt

"""
Percentiles:
In a data set, what's the point at which X% of the values are less than that value?
eg: Income distribution

Percentiles in a normal distribution
quortile range = 1Q = 50%
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