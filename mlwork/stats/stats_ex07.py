from itertools import permutations

import numpy as np
from scipy.stats import norm
from scipy.stats import kurtosis

import matplotlib.pyplot as plt


x = np.arange(-3, 3, 0.001)

plt.plot(x, norm.pdf(x))
plt.show()

plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))
plt.show()

plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))
plt.savefig("my_plot.png", format='png')

#adjust the axes

ax = plt.axes()
ax.set_xlim([-5, 5])
ax.set_ylim([0, 1.0])

ax.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
ax.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))
plt.show()

#add a grid

ax = plt.axes()
ax.set_xlim([-5, 5])
ax.set_ylim([0, 1.0])

ax.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
ax.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
ax.grid()
plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))
plt.show()

#change line types and colors

ax = plt.axes()
ax.set_xlim([-5, 5])
ax.set_ylim([0, 1.0])

ax.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
ax.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
ax.grid()
plt.plot(x, norm.pdf(x), 'b-') # blue solid line
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'r:') #red linke
plt.show()

#Labeling Axes and Adding a legend

ax = plt.axes()
ax.set_xlim([-5, 5])
ax.set_ylim([0, 1.0])

ax.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
ax.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
ax.grid()
plt.xlabel('Greebles')
plt.ylabel('Probability')
plt.plot(x, norm.pdf(x), 'b-') # blue solid line
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'r:') #red linke
plt.legend(['Sneetches', 'Gacks'], loc=4)
plt.show()

