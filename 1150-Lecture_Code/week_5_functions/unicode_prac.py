example_class_code = 'itec 1234'

uppercase_class_code = ''

for letter in example_class_code:
    # convert letter to unicode value
    character_code = ord(letter)
    # is this a lowercase letter? is it between 97 and 122?
    if character_code >= 97 and character_code <= 122:
        # Subtract 32 to get the code for the matching uppercase letter
        uppercase_class_code = character_code - 32
        # convert unicode to a character
        uppercase_letter = chr(uppercase_class_code)
        # "Append to the output string"
        uppercase_class_code = uppercase_class_code + uppercase_letter
    else:
        # Not a lowercase letter. Append it to the output string
        uppercase_class_code = uppercase_class_code + letter

print(f'The class code in uppercase is {uppercase_class_code}.')
# hmm...copied this code from the lecture/powerpoint video and I cannot seem to get it to print...correctly
