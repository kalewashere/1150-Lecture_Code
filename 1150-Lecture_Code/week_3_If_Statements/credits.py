number_of_credits = int(input('How many credits are you taking this semester?'))

if number_of_credits >= 12:  # greater than or equal to for 12 credits or more
    print('You are a full-time student!')
# want a message for half-time and for less than half-time
# we use else-if, elif, for more
elif number_of_credits >= 6:
    print('You are a half-time student!')
else:
    print('You are less than half-time.')  # else can be placed here after other conditions are not met
