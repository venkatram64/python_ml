import numpy as np
import matplotlib.pyplot as plt

"""
Covariance:
Measures how two variables vary in tandem from their means.

Measuring covariance:
Think of the data sets for the two variables as high dimensional vectors
Convert these to vectors of variances from the mean
Take the dot product(consine of the angle between them) of the two vectors
Divide by the sample size.

We know a small covariance, close to 0, means there isn't much correlation between
the two variables.

And large covariances - that is, far from 0(could be negative for inverse
relationships) mean there is a correlation
But how large is "large"?

That's where correlation comes in!

Just divide covariance by the standard deviations of the both variables,
and that normalizes things.

So a correlation of -1 means a perfect inverse correlation
correlation of 0: no correlation
correlation of 1: perfect correlation

Remember: correlation does not imply causation.
Only a controlled, randomied experiment can give you insights on causation.
Use correlation to decide what experiments to conduct
"""

def de_mean(x):
    xmean = np.mean(x)
    return [xi -xmean for xi in x]

def covariance(x, y):
    n = len(x)
    return np.dot(de_mean(x), de_mean(y)) /(n - 1)

def case1():
    pageSpeeds = np.random.normal(3.0, 1.0, 1000)
    purchaseAmount = np.random.normal(50.0, 10.0, 1000)
    plt.scatter(pageSpeeds, purchaseAmount)
    plt.show()
    cov = covariance(pageSpeeds, purchaseAmount)
    print(cov)

def case2():
    pageSpeeds = np.random.normal(3.0, 1.0, 1000)
    purchaseAmount = np.random.normal(50.0, 10.0, 1000) /pageSpeeds
    plt.scatter(pageSpeeds, purchaseAmount)
    plt.show()
    cov = covariance(pageSpeeds, purchaseAmount)
    print(cov)

def correlation(x, y):
    std_devx = x.std()
    std_devy = y.std()
    return covariance(x, y) / std_devx / std_devy



def case3():
    pageSpeeds = np.random.normal(3.0, 1.0, 1000)
    purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds
    plt.scatter(pageSpeeds, purchaseAmount)
    plt.show()
    cov = correlation(pageSpeeds, purchaseAmount)
    print(cov)

def case4():
    pageSpeeds = np.random.normal(3.0, 1.0, 1000)
    purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds
    cor = np.corrcoef(pageSpeeds, purchaseAmount)
    print(cor)

def case5():
    pageSpeeds = np.random.normal(3.0, 1.0, 1000)
    purchaseAmount = 100 - pageSpeeds * 3
    plt.scatter(pageSpeeds, purchaseAmount)
    plt.show()
    cor = correlation(pageSpeeds, purchaseAmount)
    print(cor)


if __name__ == '__main__':
    case1()
    case2()
    case3()
    case4()
    case5()


