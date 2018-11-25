import pandas as pd
from pandas import Series, DataFrame
import numpy as np


ser1 = Series([1, 2, 3, 4])
print(ser1)
ser2 = Series(['a', 'b', 'c'])
print(ser2)

#Create a pandas Index

idx = pd.Index(["New Yourk", "Los Angeles", "Chicago",
                "Houston", "Philadelphia", "Phoenix",
                "San Antonio", "San Diego", "Dallas"])

print(idx)

pops = Series([8550, 3972, 2721, 2296, 1567, np.nan, 1470, 1395, 1300],
              index=idx, name="Population")
print(pops)

state = Series({"New Your": "New York", "Los Angeles": "California",
                "Phoenix": "Arizona","San Antonio":"Texas",
                "San Diego": "California", "Dallas": "Texas"}, name="State")

print(state)

area = Series({"New Your": 302.6, "Los Angeles": 468.7,
                "Philadelphia": 134.1, "Phoenix": 516.7, "Austin": 322.48}, name="Area")

print(area)

mat = np.arange(0, 9).reshape(3, 3)
print(mat)

print(DataFrame(mat))

# Let's append new data to each Series
pops.append(Series({"Seattle": 684, "Denver": 683}))     # Not done in place

df = DataFrame([pops, state, area]).T
df.append(DataFrame({"Population": Series({"Seattle": 684, "Denver": 683}),
                     "State": Series({"Seattle": "Washington", "Denver": "Colorado"}),
                     "Area": Series({"Seattle": np.nan, "Denver": np.nan})}))


df = DataFrame([pops, state, area]).T
# Saving data to csv file
df.to_csv("cities.csv")