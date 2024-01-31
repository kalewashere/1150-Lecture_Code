name = input('What is your name?: ')

if name == 'Taylor':
    print('Hi Taylor!')

else:
    print('You are not Taylor.')

age = int(input('How old are you?: '))

if age <= 12:
    print('You are not Taylor, kiddo')

elif age >= 2000:
    print('Unlike you, Taylor is not an undead, immortal vampire.')

elif age >= 100:
    print('You are not Taylor, granpops.')

elif age == 32:
    print('Welcome, Taylor!')

else:
    print('Try again.')
