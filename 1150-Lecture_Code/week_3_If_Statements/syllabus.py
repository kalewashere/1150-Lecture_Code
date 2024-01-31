read_syllabus = input('Enter Y if you have read the syllabus for the class: ') # case-sensitive

if read_syllabus.upper() != 'Y': # the '.' changes the entered data to uppercase, not recommended for things like
    # passwords
    # the '!' means not equal. anything other than 'Y' or 'y' entered, message below is received
    print('Please read the syllabus, it has important information in it. Thanks!')
