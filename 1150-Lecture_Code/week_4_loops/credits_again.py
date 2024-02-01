# copied code from week 3
number_of_credits = int(input('How many credits are you taking this semester?'))

while number_of_credits < 0:  # we or the program do not know how many times someone might enter a negative number so we
    # use a while loop to loop until a positive number is given
    print('Error - please enter 0 or a positive number ')
    number_of_credits = int(input('How many credits are you taking this semester?'))
# loop will continue unless close. if no input is asked again i.e. above, it will run forever until you hit stop.
# condition must be able to be false.
if number_of_credits >= 12:  # greater than or equal to for 12 credits or more
    print('You are a full-time student!')
# want a message for half-time and for less than half-time
# we use else-if, elif, for more

elif number_of_credits >= 6:
    print('You are a half-time student!')
else:
    print('You are less than half-time.')  # else can be placed here after other conditions are not met
