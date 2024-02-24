# create strings with multiple repeats
# for example 'ha' repeated 5 times is 'hahahahaha'

def main():
    string = input('Please enter a string: ')
    repeat = int(input('How many times to repeat? '))
    result = string_repeater(string, repeat) # two parameters
    print(result)


def string_repeater(text, n): # two parameters
    repeated_string = text * n
    return repeated_string


main()
