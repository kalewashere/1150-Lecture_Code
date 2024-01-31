print('Quiz time!')
answer = input('What is the state bird of Minnesota: ')  # it's the loon

if answer.upper() != 'LOON': # in order for this to work, needs to be uppercase
    print('The state bird of Minnesota is the loon.')
else:
    print('Correct!')


