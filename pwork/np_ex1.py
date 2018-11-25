import numpy as np

schema = np.dtype([('sepal_length', np.float16),
                   ('sepal_width', np.float16),
                   ('petal_length', np.float16),
                   ('petal_width', np.float16),
                   ('species', '<U16')])

np_data = np.loadtxt("iris.csv", skiprows=1, dtype=schema, delimiter=",")

print(np_data[0])

print(type(np_data))

print(np_data[:5])

print(np_data[:5]['sepal_length'])