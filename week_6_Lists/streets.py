streets = ['Lake', 'Hennepin', 'Lyndale', 'Maryland']  # use commas after variables in lists to separate, if put
# inside '',
# comma will print with street name
print(streets)  # prints variables in list 'streets'
print(streets[1])  # prints variable in value slot 1 - remember 0 is counted as a number in python - also known as
# index number

streets[2] = 'Franklin'  # modified element - will print instead of Lyndale
print(streets)  # prints list with modified element

print(streets[0])
print(streets[1])
print(streets[2])

streets[0] = 'Chicago'  # modifies element at index 0
print(streets)

# TODO can you modify element 1 to a different street name
# TODO can you modify modify element 2 to a different street name?
# do not need to modify in order

streets[1] = 'Independence Ave'  # modified element 1
streets[2] = 'Emerson Ave S'  # modified element 2
print(streets[0])
print(streets[1])
print(streets[2])  # printed list like this for ease of viewing

streets[3] = 'Park'  # program will crash, must add to list at top because there is no index 3 at beginning list to
# either modify or print
print(streets[3])  # must tell program to print element in index 3, or it will not print regardless of value placed
# TODO print street names using loop
streets.sort()
print('')  # added a line break here for ease of viewing

for street in streets:
    print(street)  # loop prints street names one per line, alphabetically, after line break, with modified elements
delivery_instructions = 'Please deliver to these streets: '

for street in streets:
    delivery_instructions = delivery_instructions + street + ', '

print(delivery_instructions)

# TODO hide code - ask