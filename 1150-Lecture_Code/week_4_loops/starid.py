star_id = input('Please enter your StarID: ')

while len(star_id) != 8: # if the variable entered is not exactly 8, this message will print
    print('Error - a valid StarID has 8 characters.')
    star_id = input('Please enter your StarID: ') # asking again to make sure the program doesn't go on forever

print('Thank you, your StarID is ' + star_id)
