import numpy as np
from scipy import stats

import matplotlib.pyplot as plt


incomes = np.random.normal(100.0, 20.0, 10000) #27000-> centered around, std = 150000 with 10000 data points
m = np.mean(incomes)

print("Mean: {}".format(m))

plt.hist(incomes, 50)
plt.show()

std = incomes.std()
print("Standard Deviation: {}".format(std))

variance = incomes.var()
print("Variance: {}".format(variance))