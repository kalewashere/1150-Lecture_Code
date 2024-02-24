def is_password_long_enough(password):
    # Returnn True if password is at least 8 characters
    if len(password) >= 8:
        return True
    else:
        return False


def main():

    password = input('Please enter a password: ')
    if is_password_long_enough(password):
        print(f'The password "{password}" is long enough.')
    else:
        print(f'The password "{password}" is NOT long enough.')


main()
