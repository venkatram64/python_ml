import numpy as np
from scipy import stats

import matplotlib.pyplot as plt


incomes = np.random.normal(27000, 15000, 10000) # 27000-> centered around, std = 150000 with 10000 data points
m = np.mean(incomes)

print(m)

plt.hist(incomes, 50)
plt.show()

median = np.median(incomes)
print(median)

ages = np.random.randint(18, high=90, size=500)
print(ages)
mode = stats.mode(ages)
print(mode)