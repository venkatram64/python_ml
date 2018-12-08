import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def linearRegression():
    pageSpeeds = np.random.normal(3.0, 1.0, 1000) # median, Std, number of points
    purchaseAmmount = 100 - (pageSpeeds + np.random.normal(0, 0.1, 1000) * 3)

    plt.scatter(pageSpeeds, purchaseAmmount)
    plt.show()

    slope, intercept, r_value, p_value, std_err = stats.linregress(pageSpeeds, purchaseAmmount)

    rs = r_value ** 2
    print("R-Squreared Value is {}".format(rs))

    fitLine = slope * pageSpeeds + intercept
    plt.scatter(pageSpeeds, purchaseAmmount)
    plt.plot(pageSpeeds, fitLine, c='r')
    plt.show()



if __name__ == '__main__':
    linearRegression()
