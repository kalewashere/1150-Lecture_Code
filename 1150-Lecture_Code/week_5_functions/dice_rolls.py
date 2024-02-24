# imports random library code
import random


def main():
    # asks the user how many dice to roll
    # different games may have different numbers of dice user needs to specify
    # convert data from a str to an int (anything we need to do with math or counting needs to be a number
    number_of_dice = int(input('How many dice to roll?'))
    starting_message = f'About to roll {number_of_dice}'

    # TODO call the dice_rolling function
    dice_rolling(number_of_dice, starting_message)

    print('That is all the dice.')


def dice_rolling(dice_count, message):  # tip: select all the code to indent and press tab to indent multi lines
    # todo move the dice rolling code into a function with on parameter, the number of dice to roll
    # function does not need to return anything

    # Loop is here, based on number of dice user enters
    # repeats once for each dice to roll (4 = 4, 6 = 6, 10 = 10, etc)
    # how many times to repeat AND what is the task that is repeated
    for dice_counter in range(dice_count):  # how many to repeat
        # indented lines are the task to repeat
        dice_value = random.randint(1, 6)  # this line picks the random number
        print(f'The dice rolled a {dice_value}')  # this prints the number, in f string bc easier for me


# why is it not running? must call main function to start program

main()  # solution - call the main function to start program
