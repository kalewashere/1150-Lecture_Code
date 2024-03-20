colleges = {'Minneapolis College': '1501 Hennepin Ave, Minneapolis',  # dont forget commas
            'Metro State': '100 E 7th St, St. Paul',
            'Saint Paul College': '235 Marshall Ave, St. Paul',
            'North Hennepin Community College': '7411 85th Ave N, Brooklyn Park',
            'Century College': '3300 Century Ave N, White Bear Lake'}  # the keys listed are the names of colleges

for college in colleges:  # prints college names only
    print(college)

colleges['Metro State'] = 'Harmon Place, Minneapolis'  # modifies address of college indicated

print(colleges)  # will print updated colleges directory
# if you try and change a key that doesn't exist, it will be added to the directory
colleges['Hennepin Technical College'] = '13100 College View Dr, Eden Prairie'
# this will add the information provided here to the directory
print(colleges)

# here is an example of using [] syntax, which will error if the key is not in the directory
# use [] to read a value for a key
metro_state_address = colleges['Metro State']
print(metro_state_address)  # this will print updated/modified address for Metro State, Harmon Place
# ex of breaking would be trying to find key that is not there, like using normandale or another college not
# specified in directory
# another way is .get() to get a value for a key
# it will error if the key is not found
# will return key's value
# .get() will return None if key is not found
# always check for None before using it
# example
normandale_address = colleges.get('Normandale Community College') # this will return None
print(normandale_address) # does not break code, but None is listed in output
metro_state_address = colleges.get('Metro State')  # will return modified address of Harmon Place, Minneapolis
print(metro_state_address)

# using 'in' to check if key is in the directory

if 'Normandale Community College' in colleges: # using an if/else statement to check the directory for normandale. It
    # is not
    print('Normandale is in the directory')
else:
    print('Normandale is not in the directory.') # this is what will print

if 'Minneapolis College' in colleges:
    print('Minneapolis College is in the directory.')
else:
    print('Minneapolis College is not in the directory.')

# we can also use .get() to check if key is in the directory
normandale_address = colleges.get('Normandale Community College')
if normandale_address:
    print(f'Normandale College\'s address is {normandale_address}.') # '\'' is used to add ''s' to f'strings. This
    # will not print d/t the key not being in directgory
else:
    print('Normandale College\'s address not found.') # this is the one that will print
# example of .get() with key that is in directory
minneapolis_address = colleges.get('Minneapolis College')
if minneapolis_address:
    print(f'Minneapolis College\'s address is {minneapolis_address}.') # this is the one that prints d/t key in
    # dictionary
else:
    print('Minneapolis College\'s address not found.')

