"""
TF-IDF:
Stands for Term Frequency and Inverse Document Frequency
Important data for search - figures out what terms are most relevant for a document

Term Frequency just measures how often a word occurs in a document
    A word that occurs frequently is probably important to tht document's meaning

Document Frequency is how often a word occurs in an entire set of documents, i.e., all
of Wikipedia or every page

    This tells us about common words that just appear everywhere no matter what the topic,
    like "a", "the", "and", etc.
"""

from pyspark import SparkContext, SparkConf
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.feature import IDF

class TFIDF:

    @classmethod
    def processDocument(cls, sc):
        rawData = sc.textFile("subset-small.tsv")
        fields = rawData.map(lambda x: x.split("\t"))
        documents = fields.map(lambda x: x[2].split(" "))

        documentNames = fields.map(lambda x: x[1])

        hashingTF = HashingTF(100000)
        tf = hashingTF.transform(documents)

        tf.cache()
        idf = IDF(minDocFreq=2).fit(tf)
        tfidf = idf.transform(tf)

        gettysburgTF = hashingTF.transform(["Gettysburg"])
        gettysburgHashValue = int(gettysburgTF.indices[0])

        gettysburgRelevance = tfidf.map(lambda x: x[gettysburgHashValue])

        zippedResults = gettysburgRelevance.zip(documentNames)

        print("Best document for Gettysburg is :")
        print(zippedResults.max())



if __name__ == '__main__':
    conf = SparkConf().setMaster("local").setAppName("TFIDF")
    sc = SparkContext(conf=conf)
    TFIDF.processDocument(sc)