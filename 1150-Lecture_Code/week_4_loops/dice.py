import random   # importing random library

number_of_dice = int(input('How many dice would you like to roll? '))  # setting dice in variable - easier to keep track
# of numbers/make code a bit neater
# can also ask user for variable to use
# print('About to roll ' + str(number_of_dice) + ' dice~')
print(f'About to roll {number_of_dice} dice~')  # format string or F string - can be used to be more concise instead of
# concatenation
for dice in range(number_of_dice):  # number of dice being rolled
    dice_value = random.randint(1, 6)  # using random.radint(1, 6) to tell program to pull random int from a range of
    # 1 to 6
    #  print('Dice ' + str(dice) + ' value is ' + str(dice_value))
    print(f'Dice {dice+1} value is {dice_value}') # added + 1 to dice value to get rid of dice 0
