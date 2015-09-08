'''
Pandas Homework with IMDb data
'''

'''
BASIC LEVEL
'''

import pandas as pd
import matplotlib.pyplot as plt

# read in 'imdb_1000.csv' and store it in a DataFrame named movies
movies = pd.read_csv('imdb_1000.csv')

# check the number of rows and columns
movies.shape

# check the data type of each column
movies.dtypes

# calculate the average movie duration
movies.duration.mean()

# sort the DataFrame by duration to find the shortest and longest movies
movies.sort('duration',ascending=True)

# create a histogram of duration, choosing an "appropriate" number of bins
movies.duration.plot(kind='hist',bins=10)
plt.xlabel('Duration')
plt.ylabel('Number of Movies')

# use a box plot to display that same data
movies.duration.plot(kind='box')
'''
INTERMEDIATE LEVEL
'''

# count how many movies have each of the content ratings
movies.content_rating.value_counts()

# use a visualization to display that same data, including a title and x and y labels
movies.content_rating.value_counts().plot(kind='bar')
plt.xlabel('Ratings')
plt.ylabel('Number of Movies')
plt.title('Ratings Distribution')

# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP
movies.loc[movies.content_rating == 'NOT RATED','content_rating'] = 'UNRATED'
movies.loc[movies.content_rating == 'APPROVED','content_rating'] = 'UNRATED'
movies.loc[movies.content_rating == 'PASSED','content_rating'] = 'UNRATED'
movies.loc[movies.content_rating == 'GP','content_rating'] = 'UNRATED'

# convert the following content ratings to "NC-17": X, TV-MA
movies.loc[movies.content_rating == 'X','content_rating'] = 'NC-17'
movies.loc[movies.content_rating == 'TV-MA','content_rating'] = 'NC-17'

# count the number of missing values in each column
movies.isnull().sum()

# if there are missing values: examine them, then fill them in with "reasonable" values
movies.content_rating.fillna(value='PG', inplace=True)

# calculate the average star rating for movies 2 hours or longer,
# and compare that with the average star rating for movies shorter than 2 hours
movies[movies.duration >= 120].star_rating.mean() #7.95
movies[movies.duration < 120].star_rating.mean()  #7.84

# use a visualization to detect whether there is a relationship between duration and star rating
movies.plot(kind='scatter',x='duration',y='star_rating', alpha=0.3)

# calculate the average duration for each genre
movies.groupby('genre').duration.mean()

'''
ADVANCED LEVEL
'''

# visualize the relationship between content rating and duration
#Can't plot strings, so created a new column, num_content_rating, and assigned a numeric value to each rating
movies['num_content_rating'] = None
movies.loc[movies.content_rating == 'G','num_content_rating'] = 1
movies.loc[movies.content_rating == 'PG','num_content_rating'] = 2
movies.loc[movies.content_rating == 'PG-13','num_content_rating'] = 3
movies.loc[movies.content_rating == 'R','num_content_rating'] = 4
movies.loc[movies.content_rating == 'NC-17','num_content_rating'] = 5
movies.loc[movies.content_rating == 'UNRATED','num_content_rating'] = 6
movies.plot(kind='scatter',x='duration',y='num_content_rating')

#realized you could also do
movies['num_content_rating2'] = movies.content_rating.factorize()[0]
movies.plot(kind='scatter',x='duration',y='num_content_rating2')

# determine the top rated movie (by star rating) for each genre
maxIndexes = movies.groupby('genre')['star_rating'].transform(max) == movies.star_rating
movies[maxIndexes].title

# check if there are multiple movies with the same title, and if so, determine if they are actually duplicates

# calculate the average star rating for each genre, but only include genres with at least 10 movies

'''
BONUS
'''

# Figure out something "interesting" using the actors data!
