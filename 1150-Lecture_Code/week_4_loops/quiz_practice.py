# this is practice code for lab 4 quiz v2. I wanted a space to try different things out
answer = input('What is the capital of Wisconsin? ')
attempts_allowed = 2
total_attempts = 0


for total_attempts in range(attempts_allowed):
    attempts_remaining = attempts_allowed - total_attempts
    if answer.lower() == 'madison':
        total_attempts = total_attempts + 1
        print(f'Correct! It took you {total_attempts} attempts.')
    elif answer.lower() != 'madison':
        total_attempts = total_attempts + 1
        print(f'Sorry, {answer} is not correct. You have {attempts_remaining} attempts left')
        answer = input('What is the capital of Wisconsin? ')
        if total_attempts == 2 and attempts_allowed == 0:
            print('Sorry~ you are out of guesses. The correct answer is "Madison".')



