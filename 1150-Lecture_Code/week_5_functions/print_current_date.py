""" Function that takes no parameters (input) and has no return value (output) """

from datetime import datetime # imports datetime library, has various


# this function has no parameters, and returns no output
def display_current_time():
    print(datetime.now())

def main():
    display_current_time() # call the function, use the name and empty parameter


main()