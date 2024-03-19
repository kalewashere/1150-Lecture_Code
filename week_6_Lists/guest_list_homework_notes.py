"""creating a list for managing a guest list for an event or party"""
""" this is NOT the homework lab file - I accidentally started homework in lecture code and forgot to delete before commiting - Homework Labs 
will be sent as a zip file """
# create an empty list - part 1
# use a while loop to ask the user for the names of guests - they will enter one by one
# - add each name to list - should reject duplicate names - print message with a warning about dup print all names -
# use enumerate() to print numbered list = part 3
# ask user if they would like to delete any names - use while loop
# so the user can delete as many names as needed. can either user remove to delete by name or pop to delete by index.
# you can decide - part 4
# print all the names, again using enumerate() to print numbered list - write and call
# function instead of re-writing part 3 - part 5
# part 6 last video has info on this here
# part 7

# part 1 - create empty list
guest_list = []  # this is an empty list, indicated by brackets. we don't know the guests, so it is blank

# part 2 - ask for guest names, one by one we don't know how many so while loop is needed - must reject duplicate names
while True:  # set up loop, then return and review condition - how to stop later
    guest_name = input('Please enter first name and last initial for your guests (or press enter to stop entering '
                       'names): ')  # this is our variable - first and last initial helps with guests with the same name
    # enter name one by one, close loop when done - add name to guest_list
    # do all checks before adding name to list
    if guest_name in guest_list:
        print('You already entered ' + guest_name)
        continue

    if guest_name == '':  # is length 0? or == to empty string? # one way to close loop is to modify condition,
        # another is to check the loop and break
        break  # check for user is done before adding to list - ends loop and moves on to next part of program

    guest_list.append(guest_name)  # syntax - .append() adds input to designated target (guest_list)

# print('The final guest list is: ')
# print(guest_list)  # good to test code as we work on it - to make sure it is working and data is being entered -
# part 3
print('After adding all the names, your complete guest list is ')
# use enumerate() to create a numbered list - insert variable that you want numbered
for number, guest_name in enumerate(guest_list):  # tuple unpacking -
    print(f'{number + 1}: {guest_name}') # add 1 to number to get rid of 0 value (python counts 0)
# part 4

while True:
    guest_name_to_remove = input('Enter name to remove, or enter to stop: ')
    if guest_name_to_remove == '':
        print('You are done removing names.')
        break
    else: # remove name from guest_list
        guest_list.remove(guest_name_to_remove)
        print('Removed ' + guest_name_to_remove)


print('After removing guests, your final list is: ')
for number, guest in enumerate(guest_list):
    print(f'{number+1}: {guest}')
