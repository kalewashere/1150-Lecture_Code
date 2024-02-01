import random

want_to_quit = ''

while not want_to_quit:  # empty string is false, so hitting enter is telling the program nothing is entered.
    # the while not command is saying the variable of want_to_quit is true, since not is placed beforehand meaning
    # the empty string is true
    dice_value = random.randint(1, 6) # random int number from 1 to 6
    print(f'You rolled a {dice_value}') # f string to be concise
    want_to_quit = input('Roll again? Press enter to roll again, any other key to quit.') # program will end if any
    # other key is pressed
