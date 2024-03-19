import random
movies = ['Amelie', 'The Nightmare Before Christmas', 'Godzilla Vs. Rodan', 'Stand By Me', 'Practical Magic', 'Pink '
                                                                                                              'Flamingoes']
random.shuffle(movies)
print(movies)

for index, movie in enumerate(movies):
    print(f'{index+1}: {movie}')