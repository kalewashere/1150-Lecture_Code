winter_months = ['October', 'November', 'December', 'January', 'February', 'March', 'April']  # set months used to ask
# user for data on each - keys

snowfall = {}  # empty, to be filled with user input, dictionary

for month in winter_months:  # asking user to enter data for snowfall in inches
    snow = float(input(f'How much snow in {month}, in inches: '))
    snowfall[month] = snow  # sets variable based off user input, allowing program to gather and store

print('Here is all of the data you have entered: ')  # this will print all data user entered with keys and values

for month, snow in snowfall.items():
    print(f'In {month} there were {snow} inches of snow.')
# todo what is the total amount of snow?
# we can use sum() to calculate
total_snow = sum(snowfall.values())
# we can also do averages with some simple math - which is the total divided by the number of months - as always set
# before final print
months = len(snowfall)
average = total_snow / months

print()  # empty to add space in output
print(f'The total amount of snow in {months} months is {total_snow} inches.')
print(f'The average amount if snow per month is {average:.2f} inches.')  # remember :.2f is used at the end of floats
# to keep number down to number set in operator
