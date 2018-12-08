import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

def validate_model():
    np.random.seed(2)
    pageSpeeds = np.random.normal(3.0, 1.0, 100)
    purchaseAmount = np.random.normal(50.0, 30.0, 100) / pageSpeeds

    plt.scatter(pageSpeeds, purchaseAmount)
    plt.show()

    trainX = pageSpeeds[:80]
    testX = pageSpeeds[80:]

    trainY = purchaseAmount[:80]
    testY = purchaseAmount[80:]

    plt.scatter(trainX, trainY)
    plt.show()

    plt.scatter(testX, testY)
    plt.show()

    #Try to fit 8th degree
    x = np.array(trainX)
    y = np.array(trainY)

    p4 = np.poly1d(np.polyfit(x, y, 8))

    xp = np.linspace(0, 7, 100)
    axes = plt.axes()
    axes.set_xlim([0, 7])
    axes.set_ylim([0, 200])
    plt.scatter(x, y)
    plt.plot(xp, p4(xp), c='r')
    plt.show()

    r2 = r2_score(y, p4(x))
    print("Training R-square : {}".format(r2))

    #testing
    testx = np.array(trainX)
    testy = np.array(trainY)

    p4 = np.poly1d(np.polyfit(testx, testy, 8))

    xp = np.linspace(0, 7, 100)
    axes = plt.axes()
    axes.set_xlim([0, 7])
    axes.set_ylim([0, 200])
    plt.scatter(testx, testy)
    plt.plot(xp, p4(xp), c='r')
    plt.show()

    r2 = r2_score(testy, p4(testx))
    print("Testing R-square : {}".format(r2))




if __name__ == '__main__':
    validate_model()