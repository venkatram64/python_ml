import pandas as pd
import numpy as np

schema = np.dtype([('sepal_length', np.float16),
                   ('sepal_width', np.float16),
                   ('petal_length', np.float16),
                   ('petal_width', np.float16),
                   ('species', '<U16')])

np_data = np.loadtxt("iris.csv", skiprows=1, dtype=schema, delimiter=",")

pd_data = pd.read_csv("iris.csv")

#print(pd_data)

#print(type(pd_data))

#print(pd_data.head())

#print(pd_data.head().sepal_length)

#print(pd_data.head().loc[:, ['petal_length', 'species']])

#print(pd_data.values)

np_pd_data = pd.DataFrame(np_data)

print(np_pd_data)