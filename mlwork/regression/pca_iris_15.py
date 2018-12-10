from sklearn.datasets import  load_iris
from sklearn.decomposition import PCA
import pylab as pl
from itertools import cycle


"""
PCA is a dimensionality reduction technique; it lets you distill multi-dimensional data down to fewer dimensions, 
selecting new dimensions that preserve variance in the data as best it can.

Let's do this with a simpler example: the Iris data set that comes with scikit-learn. 
It's just a small collection of data that has four dimensions of data for three different 
kinds of Iris flowers: The length and width of both the petals and sepals of many individual 
flowers from each species. Let's load it up and have a look:
"""

def processIrisData():
    iris = load_iris()
    numSamples, numFeatures = iris.data.shape
    print(numSamples)
    print(numFeatures)
    print(list(iris.target_names))

    X = iris.data
    pca = PCA(n_components=2, whiten=True).fit(X)
    print(pca.components_)
    X_pca = pca.transform(X)

    print(pca.explained_variance_ratio_)
    print(sum(pca.explained_variance_ratio_))

    colors = cycle('rgb')
    target_ids = range(len(iris.target_names))
    pl.figure()

    for i, c, label in zip(target_ids, colors, iris.target_names):
        pl.scatter(X_pca[iris.target == i, 0], X_pca[iris.target == i, 1],
                   c=c, label=label)

    pl.legend()
    pl.show()


if __name__ == '__main__':
    processIrisData()