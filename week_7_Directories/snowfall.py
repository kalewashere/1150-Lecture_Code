winter_months = ['October', 'November', 'December', 'January', 'February', 'March', 'April']  # set months used to ask
# user for data on each - keys

snowfall = {}  # empty, to be filled with user input, dictionary

for month in winter_months:  # asking user to enter data for snowfall in inches
    snow = float(input(f'How much snow in {month}, in inches: ')) # must use float
    snowfall[month] = snow  # sets variable based off user input, allowing program to gather and store in dictionary

print('Here is all of the data you have entered: ')  # this will print all data user entered with keys and values

for month, snow in snowfall.items():
    print(f'In {month} there were {snow} inches of snow.')
#  what is the total amount of snow?
# we can use sum() to calculate
total_snow = sum(snowfall.values()) # this tells the program to sum(add) all data in value portion of keys
# we can also do averages with some simple math - which is the total divided by the number of months - as always set
# before final print
months = len(snowfall) # calculates length (number) of months in dictionary snowfall, allowing us to use data (
# number) for math
average = total_snow / months # this will give us the average amount of snow in range of months calculated with len()

print()  # empty to add space in output
print(f'The total amount of snow in {months} months is {total_snow} inches.') # format string to include months and
# total snow, without averaging it out yet - see below
print(f'The average amount if snow per month is {average:.2f} inches.')  # remember :.2f is used at the end of floats
# to keep number down to number set in operator
