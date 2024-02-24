""" Write a code that can tell which classes are first or second year courses """


# function that returns first or second year when course number is entered
# use if statements
# class codes for first year classes are between 1000 and 1999
# class codes for second year classes are between 2000 and 2999
# use 'invalid' for all other values (else)
# ask user for class code in main function
def main():
    class_code = int(input('Please enter your course number: ')) # asking user for course number to feed to program
    # so it can fun through the function
    if class_code in range(1000, 1999):
        print(f'"{class_code}" is a first year course. ')
    elif class_code in range(2000, 2999):
        print(f'"{class_code}" is a second year course. ') # i prefer f strings
    else:
        print('Invalid Entry.')  # using this for any other value entered that is not listed about in function


def code(class_code): # more trial and error here, eventually figured out where to put what after going back on the
    # videos a little bit.
    course = class_code
    return course

main() # calling function
# my code lookis v e r y different than in the video - which i know it ok - but it is interesting to see how codes
# can be written differently