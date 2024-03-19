history = [] # empty list

# examples of visited webpages
history.append('www.google.com')
history.append('www.minneapolis.edu')
history.append('www.msn.com') # .append(x) adds element to list indicated

# this would be an example of using the back button in a browser - using .pop() returns last item in list
print(history.pop())
print(history.pop())
print(history.pop()) # careful not to add too many .pop() - will break code, cannot remove (return) from an empty list
