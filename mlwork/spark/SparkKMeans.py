from pyspark.mllib.clustering import KMeans
from pyspark import SparkConf, SparkContext
from sklearn.preprocessing import scale
import numpy as np
from math import sqrt

class KMeanCluster:


    @classmethod
    def createClusteredData(cls, N, k):
        np.random.seed(10)
        pointsPerCluster = float(N)/k
        X = []
        for i in range(k):
            incomeCentroid = np.random.uniform(20000.0, 200000.0)
            ageCentroid = np.random.uniform(20.0, 70.0)
            for j in range(int(pointsPerCluster)):
                X.append([np.random.normal(incomeCentroid, 10000.0), np.random.normal(ageCentroid, 2.0)])
        X = np.array(X)
        return X

    @classmethod
    def error(cls, point, clusters):
        center = clusters.centers[clusters.predict(point)]
        return sqrt(sum([x**2 for x in (point - center)]))

    @classmethod
    def processData(cls, K, sc):

        data = sc.parallelize(scale(cls.createClusteredData(100, K)))
        clusters = KMeans.train(data, K, maxIterations=10, runs=10,
                                initializationMode="random")
        resultRDD = data.map(lambda point: clusters.predict(point)).cache()

        print("Counts by value: ")
        counts = resultRDD.countByValue()
        print(counts)

        print("Cluster assignments: ")
        results = resultRDD.collect()
        print(results)

        #Within Set Sum of Squared Errors
        WSSSE = data.map(lambda point: cls.error(point, clusters))\
            .reduce(lambda x, y: x + y)

        print("Within Set Sum of Squared Error = " + str(WSSSE))



if __name__ == '__main__':
    conf = SparkConf().setMaster("local").setAppName("SparkKMeans")
    sc = SparkContext(conf=conf)
    KMeanCluster.processData(5, sc)

