# loop practice - FOR
answer = input('What is the capital of Wisconsin? ')
attempts = 0 + 1
attempts_allowed = 3
remaining_attempts = attempts_allowed - attempts

for attempts in range(attempts_allowed):
    if answer.lower() != 'madison':
        print(f'Sorry, {answer} is incorrect. ')