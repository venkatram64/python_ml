from itertools import permutations

import numpy as np
from scipy.stats import norm
from scipy.stats import kurtosis

import matplotlib.pyplot as plt



#XKCD Style
plt.xkcd()
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim([-30, 10])

data = np.ones(100)
data[70:] -= np.arange(30)

plt.annotate(
    'THE DAY I REALIZED\n I COULD COOK BACON\n WHENEVER I WANTED',
    xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))

plt.plot(data)

plt.xlabel('Time')
plt.ylabel('My Overal Health')
plt.show()

#Pie Chart

plt.rcdefaults()
values = [12, 55, 4, 32, 14]
colors = ['r', 'g', 'b', 'c', 'm']
explode = [0, 0, 0.2, 0, 0]
labels = ['India', 'United States', 'Russia', 'China', 'Europe']
plt.pie(values, colors=colors, labels=labels, explode=explode)
plt.title('Student Locations')
plt.show()

#Pie Chart

plt.rcdefaults()
values = [12, 55, 4, 32, 14]
colors = ['r', 'g', 'b', 'c', 'm']

plt.bar(range(0, 5), values, color=colors)
plt.show()

#Scatter Plot

"""X = np.randn(500)
Y = np.randn(500)
plt.scatter(X, Y)
plt.show()"""

#Histogram

incomes = np.random.normal(27000, 15000, 10000)
plt.hist(incomes, 50)  #50 buckets
plt.show()

