import pandas as pd
from pandas import Series, DataFrame
import numpy as np

srs1 = Series([1, 9, -4, 3, 3])
print(srs1)
srs2 = Series([2, 3, 4, 5, 10], index=[0, 1, 2, 3, 5])

print(srs2)

print(srs1 + srs2)

print(srs1 * srs2)

print(srs1 ** srs2)

print(np.sqrt(srs2))

#define a custom ufunc: notice the decorator notation?

@np.vectorize
def trunc(x):
    return x if x > 0 else 0


ret_v = trunc(np.array([-1, 5, 4, -3, 0]))

print(ret_v)

print(srs2.mean())

print(srs2.std())

print(srs2.max())

#print(srs2.argmax())
print(srs2.idxmax())

print(srs2.cumsum())

srs1.apply(lambda x: x if x > 2 else 2)

srs1.map(lambda x: x if x > 2 else 2)  #works like apply



#DataFrames

df = DataFrame(np.arange(15).reshape(5, 3), columns=["AAA", "BBB", "CCC"])

print(df)

# Define a function for the geometirc mean

def geomean(srs):
    return srs.prod() ** (1 / len(srs))


ret_v = geomean(Series([2, 3, 4]))

print(ret_v)

ret_v = df - df.loc[:, ["AAA", "BBB"]]
print(ret_v)

print(df.mean())
print(df.std())

std_variation = (df - df.mean())/df.std()

print(std_variation)

