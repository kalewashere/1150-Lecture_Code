summer_months = ['June', 'July', 'August']
# basically took the snowfall program and edited it to read for the 3 summer months nd get averages the same way
rainfall = {}

for month in summer_months:  # this asks the user to enter inches of rain, for each month - loop
    rain = float(input(f'How much rain fell in {month}, in inches: '))  # stored in variable
    rainfall[month] = rain  # variable assigned and stored in dictionary (key and value)
print()
print('Here is the data you have entered for rainfall')  # prints data entered

for month, rain in rainfall.items():  # this loop will print each line per month in rainfall dictionary
    print(f'In {month} there was {rain} inches of rain.')  # this is what tells program to print, and how

total_rain = sum(rainfall.values())  # variable for total rain
months = len(rainfall)  # tells program how many months we have data for
average = total_rain / months  # MATH

print()  # ease of output reading - blank line
print(f'The total amount of rain in {months} months is {total_rain} inches. ')  # this shows us data after math is
# run, total inches in how many (3) months
print(f'The average amount of rain per month is {average:.1f} inches. ')  # prints message that includes math for
# average - :.1f cut decimals to one (1) point after decimal
