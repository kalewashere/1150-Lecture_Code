def main():
    credits_completed = 34
    college = 'Minneapolis College'
    report(credits_completed, college) # arguments must be in correct order


def report(cr, col):
    print('Your school is', col)
    print(f'You need {60 - cr} credits to graduate.')


main()