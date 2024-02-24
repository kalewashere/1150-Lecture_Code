""" Python library function that takes no parameters (inoput) and has a return value (output) """

import os  # library contatining various operating system related functions

# library function os.getcwd() takes no parameters
# returns the current working directory
# typically the directory containing the python project
cwd = os.getcwd()
print(f'The current directory is {cwd}')