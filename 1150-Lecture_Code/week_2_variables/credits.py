# assignment statement, use input to ask question and store answer in a new variable
# called username, whatever user types is what is saved
username = input('What is your name?')
# optional
name_length = len(username)
print('Your name is ' + str(name_length) + ' letters long')
credits_taken = int(input('How many credits are you taking this semester?')) # Ask for how many credits, as before but "wrap" the input in an int function call to
# convert the data to an int variable. otherwise, it will be a string.
# cant do math with strings
print(credits_taken)
print(username + ' is taking ' + str(credits_taken) + ' credits.') # TODO task completed
credits_taken_last_semester = int(input('How many credits did you take last semester?'))

print(credits_taken_last_semester + credits_taken) # TODO fix message to include 'credits taken'

total_credits = credits_taken_last_semester + credits_taken

print('The total credits will be ' + str(total_credits) + ' in this and last semester')


