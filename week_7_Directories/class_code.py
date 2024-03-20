classes = {  # initial directory
    1150: 'Programming Logic',
    1425: 'Data Communication',
    1310: 'PC Maintenance'
}
for class_code in classes:  # this will print the code only
    print(class_code)

for class_name in classes.values():  # this will print the elements/data in the value portion of the keys, meaning
    # here, the name of the class, only
    print(class_name)

# this last loop will loop over both, and combine them to create an f'string
for class_code, class_name in classes.items():  # we use items() function here, will edit comments once .items() is
    # understood more
    print(f'ITEC {class_code} is {class_name}')  # all three loops will print in output
