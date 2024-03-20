# String keys and number values

rainfall_by_month = {
    'March': 1.4,
    'April': 2.5,
    'May': 0.5,
    'June': 3.1,
    'July': 2.8,
    'August': 1.0,
    'September': 0.2,
    'October': 1.9
}
print(rainfall_by_month)

# number keys and string values
class_codes = {
    1100: 'IT Concepts',
    1150: 'Programming Logic',
    1310: 'PC Maintenance',
    1425: 'Data Communications'
} # numbers placed first - not sure yet if that is required but definitely looks better with
print(class_codes)
# string keys and string values
paint_colors = {
    'Kitchen': 'blue',
    'Living Room': 'green',
    'Hallway': 'beige',
    'Main bedroom': 'purple',
    'Secondary bedroom': 'pink',
    'Bathroom': 'blue'
}
print(paint_colors) # will print directory with bedrooms and colors chosen for each room

# string keys, various values
book = {
    'Title': 'Automate the Boring Stuff',
    'Author': 'Al Swiegart',
    'Price': 0.00,
    'Quantity': 10,
    'Year': 2018
}
print(book) # will print all information listed above

# string keys, list values
# each student took 3 quizes
quiz_scores = {
    'Al': [8, 9, 10],
    'Ally': [6, 10, 10], # forgot my comma and the error message ASKED me if i forgot something - that made me laugh
    'Codyana': [7, 7, 9]
}
print(quiz_scores)

# TODO can we print Ally's lowest score?
for student, list_of_scores in quiz_scores.items():
    print(f'Student {student} scores are {list_of_scores}.')
# to get one list
ally_scores = quiz_scores['Ally']
# this is a list, and will give us all values assigned to 'Ally'
for x, score in enumerate(ally_scores):
    print(f'On quiz {x+1} Ally scored {score}.')

ally_max = max(ally_scores)
print(f'Ally\'s best score is {ally_max}.')
# Ally's lowest score using min() operator
ally_minimum = min(ally_scores)
print(f'Ally\'s worst score is {ally_minimum}')