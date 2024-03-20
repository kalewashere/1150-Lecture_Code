paint_colors = {
    'Kitchen': 'blue',
    'Living Room': 'green',
    'Bedroom': 'purple',
    'Bathroom': 'blue'
}
print('Rooms to paint:', paint_colors)

# this next example will tell us that we painted the bedroom - removing key and returning value using pop
bedroom_color = paint_colors.pop('Bedroom')
print('Painted the bedroom', bedroom_color)

print('Rooms left to paint:', paint_colors)  # this will tell us which rooms we have left to paint, since we removed
# the bedroom from the dictionary
# if we need to add a room(key)to paint(color, value), we can do that like so
print('Need to paint the hallway')
paint_colors['Hallway'] = 'Beige'
print('Rooms left to paint:', paint_colors)

# to get a value for a key we can do it like this
kitchen_color = paint_colors['Kitchen']
print('The kitchen will be painted ' + kitchen_color)  # we can call this value IF we tell the program what we are
# looking for, by making a new variable and assigning the key to it with []
