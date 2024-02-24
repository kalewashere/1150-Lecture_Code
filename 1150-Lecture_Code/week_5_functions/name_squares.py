def main():

    while user_wants_to_continue('make squares from words'):
        word = input('Please enter the word to print in a square: ')
        word_square(word)

    print('Thanks for using the program!')

def word_square(word):  # watch indentation to make sure program runs correctly
    for letter in range(len(word)):  # indentation
        print(word)    # indent

def user_wants_to_continue(task):
    response = input(f'Do you want to {task}? Enter "Y" for yes, anything else for no. ')
    # Uppercase the response, so "y" and "Y" are both equal to "Y".
    # this means user can enter either upper or lowercase
    # this is useful for case-insensitive comparisons.
    if response.upper() == 'Y':
        return True # True must be uppercase
    return False # False must be uppercase


main() # call function