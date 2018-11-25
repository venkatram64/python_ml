import numpy as np
import pandas as pd
from pandas import Series, DataFrame


df = DataFrame(np.round(np.random.randn(7, 3) * 10),
               columns=["AAA", "BBB", "CCC"],
               index=list("defcabg"))

print(df)

print(df.sort_index())

print(df.sort_index(axis=1, ascending=False))

#Now I sort according to the values of the Dataframe

print(df.sort_values(by="AAA"))

print(df.sort_values(by=['BBB', 'CCC']))

print(df.rank())

print(df.rank(method='max'))