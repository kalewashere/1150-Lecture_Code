def above_freezing(temp):
    if temp > 32:
        return 'above freezing'
    else:
        return 'below freezing'

def main():
    # Call the above_freezing function, in different ways - 3

    today_temp = float(input('Please enter today\'s high temperature: ')) # tip: use "\'" to insert apostrophe in
    # print statement
    # Call the function in a print statement
    print('It will be ' + above_freezing(today_temp) + ' today.')

    tonight_temp = float(input('Please enter tonight\'s low temperature: '))
    # calling function, saving return value in new variable to use later in print statement
    above_below_tonight = above_freezing(tonight_temp)
    print('It will be ' + above_below_tonight + ' tonight.') # used here in print statement

    tomorrow_temp = float(input('Please enter tomorrow\'s high temperature: ')) # calling function in f string next
    print(f'It will be {above_freezing(tomorrow_temp)} tomorrow. ')


main()