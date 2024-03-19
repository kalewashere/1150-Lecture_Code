# list of int values
bus_routes = [17, 6, 4, 21]  # whole numbers
# list of float values
lbs = [2.15, 14.5, 3.25]  # not whole numbers
first_weight = lbs[0] # assigning first weight to variable, allowing us to print in f' string
print(f'This was the first thing weighed was {first_weight} lbs.')
lbs[2] = 10.1 # modified element in value 2
print(lbs) # will print modified list
# list of different things
example = [True, 14, 65.25, 'Goodbye']  # mixture of all
# list of lists!
lists = [bus_routes, lbs, example, [1, 2, 3]]  # prints all values in lists listed above + 1, 2, 3
print(lists) # prints all lists
