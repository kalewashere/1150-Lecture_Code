movie_ratings = {'Amelie': 10, 'The Nightmare Before Christmas': 9, 'Stand By Me': 8} # movie ratings out of ten, descending

# reading a score - create variable for each movie to read that specific score
amelie_score = movie_ratings['Amelie']
print(amelie_score)

# another example
before_chirstmas_score = movie_ratings['The Nightmare Before Christmas']
print(before_chirstmas_score)

# last one for good measure
by_me_score = movie_ratings['Stand By Me']
print(by_me_score)

# we can also change scores
movie_ratings['Amelie'] = 9
print(movie_ratings) # this will tell program to re-print list with updated rating

# can also add new movie and ratings
movie_ratings['Pink Flamingos'] = 10
print(movie_ratings)

# another
movie_ratings['James and the Giant Peach'] = 9
print(movie_ratings)

for movie, values in movie_ratings.items():
    print(f'{movie} has a rating of {values}.') # TODO print all movies and ratings using a loop with .items()

