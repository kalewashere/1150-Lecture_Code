# asking for quiz store
quiz_score = float(input('Enter score for quiz, out of 100: '))

if quiz_score == 100:  # two equal signs tells python to check if condition entered meets 'if command'
    # ':' a condition, is syntax for python, telling it that is the end of the command entered, to run, and check
    # conditions
    print('Congrats! You aced the quiz!')  # conditional code, will only run if condition above is approved
    # indentation is important, used by python to indication line is/may be conditional code.
    print('Amazing!')

print('This is the end of the program')  # skips over 'if command', if condition not met
