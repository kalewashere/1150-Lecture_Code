import random

movies = ['Amelie', 'The Nightmare Before Christmas', 'Godzilla Vs. Rodan', 'Stand By Me', 'Practical Magic', 'Pink '
                                                                                                              'Flamingoes']
print(movies)

random.shuffle(movies)


for index, movie in enumerate(movies):
    print(f'{index + 1}: {movie}')
