# string keys, list values
# each student took 3 quizes
quiz_scores = {
    'Al': [8, 9, 10],
    'Ally': [6, 10, 10], # forgot my comma and the error message ASKED me if I forgot something - that made me laugh
    'Codyana': [7, 7, 9]
}
print(quiz_scores)


#  can we print Ally's lowest score? - yes
for student, list_of_scores in quiz_scores.items():
    print(f'Student {student} scores are {list_of_scores}.')
# to get one list
ally_scores = quiz_scores['Ally']
# this is a list, and will give us all values assigned to 'Ally'
for x, score in enumerate(ally_scores):
    print(f'On quiz {x+1} Ally scored {score}.')

ally_max = max(ally_scores)  # this will tell the program to get us Ally's max score
print(f'Ally\'s best score is {ally_max}.')
# Ally's lowest score using min() operator
ally_minimum = min(ally_scores) # this will tell the program to get us ally's lowest score
print(f'Ally\'s worst score is {ally_minimum}')