import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import random


# Create a data frame of random numbers, some randomly censored

vals = np.random.randn(21)
vals[random.sample([i for i in range(21)], 5)] = np.nan

print(vals)

df = DataFrame(vals.reshape(7, 3), columns=["AAA", "BBB", "CCC"])

print(df)

srs = Series([2, 3, 3, 9, 8, np.nan, 8, np.nan, 4, 4, 5])

print(srs)

"""
Here we see methods for detecting missing data. These methods
produce identical results
"""

print(np.isnan(df))

print(df.isnull())

print(df.notnull())

print(df.dropna())

print(srs.dropna())

xbar = srs.mean()

print(xbar)