employee_data = {  # this is an example of a dictionary within a dictionary, which uses two sets of {} and ,
    # to separate key-value pairs
    'name': 'Cody Dev',
    'employee_number': 123456,
    'Location': {
        'city': 'Minneapolis',
        'office': 'M.123',
        'telephone': '612-123-4567',
    },
    'roles': ['python developer', 'server administrator']
}
# this is how we modify cody's information
# modifying cody's office to another number
employee_data['Location']['office'] = 'M.4000'  # this calls information from dictionary - location first, from it's
# dictionary, then value
# from key inside that second dictionary

# we can also tell the program to print specific data by calling the first dictionary, then the second
print(employee_data['Location']['telephone']) # dont forget - keys need to be typed just as they are in the
# dictionary or code will break

# we can add new data using .append
employee_data['roles'].append('web developer') # dont forget .append adds to end of list by default - so it will be
# placed after 'server administrator'

print(employee_data)