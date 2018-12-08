import numpy as np
from scipy.stats import norm
from scipy.stats import expon
from scipy.stats import binom
from scipy.stats import poisson

import matplotlib.pyplot as plt

#uniform distribution

values = np.random.uniform(-10.0, 10.0, 10000) #27000-> centered around, std = 150000 with 10000 data points

plt.hist(values, 50)
plt.show()


#Noramal / Gaussian

#Visualie the probability density function

x = np.arange(-3, 3, 0.001)
plt.plot(x, norm.pdf(x))
plt.show()

mu = 5.0
sigma = 2.0
values = np.random.normal(mu, sigma, 10000)
plt.hist(values, 50)
plt.show()

#Exponential PDF / Power Law

x = np.arange(0, 10, 0.001)
plt.plot(x, expon.pdf(x))       #probability density function
plt.show()

#Binomial probability Mass function

n, p = 10, 0.5
x = np.arange(0, 10, 0.001)
plt.plot(x, binom.pmf(x, n, p)) #probability mass function
plt.show()

#Poisson Probability Mass Function

mu = 500
x = np.arange(400, 600, 0.5)
plt.plot(x, poisson.pmf(x, mu))
plt.show()