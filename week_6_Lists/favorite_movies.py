movies = ['Amelie', 'The Nightmare Before Christmas', 'Godzilla vs. Rodan', 'Stand By Me']  # favorite movies
movies.sort()  # MUST sort FIRST - this was giving me issues - would not print movies in reverse order bc i did not
# sort first
movies.reverse()

for movie in movies:  # name variables in list as something that is specific - ie movie in movies
    print(movie)

favorite_movies = ', '.join(movies)  # using .join function to create a string listing favorite movies
print(favorite_movies)  # this will print movies, reverse alpha, on one line (outside of loop - therefore on one line)

movies.append('Practical Magic')  # this adds an element to list at top. edits only that list, in order to get it to
# look like i want it too, I will need to edit 'movies.append('Practical Magic)' to favorite_movies.append('Practical
# Magic') -- update: just kidding that broke the code - i will revisit in a moment (see below)
print(movies)  # list was already sorted, append will always add to end of list no matter what was done to list above

number_of_movies = len(movies)
print(f'There are {number_of_movies} movies in the list.')

# movies.remove('Stand By Me')  if the movie is not in the list, error will occur. But error will print at beginning
# of output, with rest of code coming after - best if you know what you want to remove ie movie title
print(movies)
print('')  # ease of viewing break
movies.pop(4)
print(movies)
print('')  # ease of viewing break
movies.remove('Stand By Me')
print(movies)
print('')  # ease of viewing
# i enjoy making output as easy to read as possible, especially if I want to keep code above for future ref
movies.sort()
movies.reverse()
for movie in movies:
    print(movie)

# you can also use pop() if you know where in the list you want to remove the item from - what position,
# etc. movies.pop(0) indicates which index # to remove from - remember 0 is first position - pop removes by index -
# can be written with no argument, meaning it will return last item in list
