weight = float(input('Please enter your weight in pounds: '))
age = int(input('Please enter your age in years: '))

if weight >= 110 and age >= 16:
    print('Great! You are eligible to be a blood donor.')
elif weight < 110 and age >= 16:
    print("Sorry, you are not eligible. You are 16, but you do not weigh 110 lbs or more.")
elif weight >= 110 and age < 16:
    print('Sorry, you are not eligible. You weigh 110lbs or more, but you are not old enough (16).')
elif weight < 110 and age < 16:
    print('Sorry, you are not eligible. You do not weigh enough (110lbs) and you are not old enough (16).')

# bonus question: how do you display a message for being less than 110 lbs but over 16? what about over 110 lbs,
# but not 16?
#
# hm. I got the program to run the bonus question, but I am finding that means the ' else' statement
# is...kind of useless?..I mean, it will print that message if lets say...both variables are false? testing: ok so
# both variables listed ( < 110 and age < 16) didnt break the code, but displayed the message for weight being enough
# but age being too young...
# okay fixed the code to recognize weight < 110 and age < 16 (i also mistyped a variable in an elif statement)
# now i was to edit the last elif to include a more complete sentence. 'else' statement changed to
# elif weight < 110 and age <16
# deleted both ifs under old else and compacted it into one sentence
