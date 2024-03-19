#  print(['cat'] * 6) # this lists cat 6 times in one list
quiz_scores = [0] * 5  # this prints a list of five 0s
print(quiz_scores)

# for quiz in quiz_score:    for loop detailing asking user to enter quiz score for quiz number indicated
#   score = int(input(f'Enter score for {quiz+1}: ')
#   quiz_scores[quiz] = score
# can also enumerate
for quiz, score in enumerate(quiz_scores):
    new_score = int(input(f'Enter score for quiz {quiz+1}: '))
    quiz_scores[quiz] = new_score
print('You scores are: ')
print(quiz_scores)