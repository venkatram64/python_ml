import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

"""
Why limit ourselves to straight lines?
Not all relationships are linear.
Linear formula: y = mx + b
This is a "first order" or "first degree"
polynomial, as the power of x is 1
Second order polynomial: y = ax^2 + bx + c
Third order: y = ax^3 + bx^2 + cx + d
Higher orders produce more complex curves.
"""

def polyPlot():
    np.random.seed(2)
    pageSpeeds = np.random.normal(3.0, 1.0, 1000)
    purchaseAmount = np.random.normal(50, 10.0, 1000) / pageSpeeds
    plt.scatter(pageSpeeds, purchaseAmount)
    plt.show()

    x = np.array(pageSpeeds)
    y = np.array(purchaseAmount)
    """
    numpy has a handy polyfit function we can use, to let us construct
    an nth-degree polynomial model of our data that minimizes squared 
    error. Let's try it with a 4th degree polynomial
    """
    p4 = np.poly1d(np.polyfit(x, y, 4))

    """
    We'll visualize our original scatter plot, together with a plot of
    our predicted values using the ploynomial for page speed times ranging
    from 0 to 7 seconds
    """

    xp = np.linspace(0, 7, 100)
    plt.scatter(x, y)
    plt.plot(xp, p4(xp), c='r')
    plt.show()

    r2 = r2_score(y, p4(x))
    print(r2)



if __name__ == '__main__':
    polyPlot()