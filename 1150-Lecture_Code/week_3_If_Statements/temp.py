temperature = float(input('Enter the temperature in Fahrenheit: '))

if temperature <= 32:
    print('It is below freezing. Watch for ice.')
    snowing = input('Enter "Y" if it is snowing today: ')
    if snowing.upper() == 'Y':
        print('Snow boots are recommend today.')

else:
    print('It is above freezing today.')

# can use Boolean variables instead
# example: *preferred version
# below_freezing = True
# if below_freezing:
    #print('Brr')
# else:
    #print('It is above freezing')