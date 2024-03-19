""" Changing a list item """

quiz_scores = [8, 4, 10, 9, 7]  # initial list for user's quiz scores

quiz = int(input('Which quiz did you retake?'))
# can modify for humans by using index = quiz - 1, but will need to modify quiz_score[quiz] = score to quiz_score[
# index] = score in order to modify correct value
# What if the user re-took the second quiz? let's say the user aced
# the quiz and scored 10 update the quiz_scores list

# quiz_scores[1] = 10  # use square brackets to indicate which index you would like to update print(quiz_scores)  #
# prints updated quiz scores but can also enter as an int, as well as an input - we can ask the user
score = int(input('Wait was your score on quiz 2?'))

quiz_scores[quiz] = score  # can use either the index number, OR ask the user which quiz they took, and place that
# variable there instead

print(quiz_scores)
