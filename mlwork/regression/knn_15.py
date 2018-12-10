import pandas as pd
import numpy as np
from scipy import spatial
import operator

"""
KNN (K-Nearest Neighbours)

KNN is a simple concept: define some distance metric between the items in your dataset, 
and find the K closest items. You can then use those items to predict some property of a test item, 
by having them somehow "vote" on it.
As an example, let's look at the MovieLens data. We'll try to guess the rating of a movie by looking 
at the 10 movies that are closest to it in terms of genres and popularity.
To start, we'll load up every rating in the data set into a Pandas DataFrame:
"""

r_cols = ['user_id', 'movie_id', 'rating']

ratings = pd.read_csv('u.data', sep='\t', names=r_cols, usecols=range(3))
print(ratings.head())

movieProperties = ratings.groupby('movie_id').agg({'rating':[np.size, np.mean]})
print(movieProperties.head())

movieNumRatings = pd.DataFrame(movieProperties['rating']['size'])
print("***********  movieNumRatings *************")
print(movieNumRatings)
movieNormalizedNumRatings = movieNumRatings.apply(lambda x: (x - np.min(x))/(np.max(x) - np.min(x)))
print(movieNormalizedNumRatings.head())

movieDict = {}
with open(r'u.item') as f:
    temp = ''
    for line in f:
        #line.decode("ISO-8859-1")
        fields = line.rstrip('\n').split('|')
        movieID = int(fields[0])
        name = fields[1]
        genres = fields[5:25]
        genres = map(int, genres)
        movieDict[movieID] = (name, np.array(list(genres)),
                              movieNormalizedNumRatings.loc[movieID].get('size'),
                              movieProperties.loc[movieID].rating.get('mean'))

print(movieDict[1])

def computeDistance(a, b):
    genresA = a[1]
    genresB = a[2]
    genresDistance = spatial.distance.cosine(genresA, genresB)
    popularityA = a[2]
    popularityB = b[2]
    popularityDistance = abs(popularityA - popularityB)
    return genresDistance + popularityDistance


computeDistance(movieDict[2], movieDict[4])

print(movieDict[2])
print(movieDict[4])

def getNeighbors(movieID, K):
    distances = []
    for movie in movieDict:
        if(movie != movieID):
            dist = computeDistance(movieDict[movieID], movieDict[movie])
            distances.append((movie, dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(K):
        neighbors.append(distances[x][0])
    return neighbors

K = 10
avgRating = 0
neighbors = getNeighbors(1, K)
for neighbor in neighbors:
    avgRating += movieDict[neighbor][3]
    print(movieDict[neighbor][0] + "  " + str(movieDict[neighbor][3]))

avgRating /= K

print(avgRating)

print(movieDict[1])
