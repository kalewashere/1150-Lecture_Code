# alert user if parked for too long
parking_time = float(input('How many hours have you parked? '))
# max parking time 2 hours
if parking_time >= 2: # greater than + equal to makes it so if 2 hours is entered, warning is still given
    print('Warning! You should move your car.')
    # personally prefer '>='
    # especially for parking...only seems fair
    # can we print how many hours over parking time? - Answer: yes
    time_over = parking_time - 2 # swapped parking time variable and subtracted max parking time to get hours over limit
    print('You have gone ' + str(time_over) + ' hours over time allowed.') # converted to string
else:
    print('You are okay for parking, you still have time.') # else statements used to tell program that data that
    # does not match condition will get this message instead
    # can we calculate how much time is left?
    # yes! math. Set data in variable
    # subtract from parking time of 2 hours
    time_left = 2 - parking_time
    print('You have ' + str(time_left) + ' hours left') # turn into string
print('This is the end of the program.') # not indented
# runs after if/else