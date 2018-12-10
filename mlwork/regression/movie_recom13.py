import pandas as pd
import numpy as np

"""
 user based collaboration
"""

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv('u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)

print(ratings.head())

movieRatings = ratings.pivot_table(index=['user_id'], columns=['title'], values='rating')
print(movieRatings.head())

starWarsRatings = movieRatings['Star Wars (1977)']
print(starWarsRatings.head())

similarMovies = movieRatings.corrwith(starWarsRatings)
similarMovies = similarMovies.dropna()
df = pd.DataFrame(similarMovies)
print(df.head(10))

print(similarMovies.sort_values(ascending=False))

movieStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})
print(movieStats.head())

popularMovies = movieStats['rating']['size'] >= 100
sorted_recs = movieStats[popularMovies].sort_values([('rating', 'mean')], ascending=False)[:15]
print(sorted_recs)

df = movieStats[popularMovies].join(pd.DataFrame(similarMovies, columns=['similarity']))

print(df.head())

sortVals = df.sort_values(['similarity'], ascending=False)[:15]

print(sortVals)


