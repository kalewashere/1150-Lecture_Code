def main():
    credit_count = int(input('Please enter the number of credits you are taking this semester: '))

    while not credits_valid(credit_count):
        print('That is not a valid number of credits.')
        credit_count = int(input('Please enter the number of credits you are taking this semester, between 0 and 24: '))

    status_message = full_time_part_time(credit_count)

    print(f'Your status is a {status_message} student.')


def credits_valid(credit_count):
    if credit_count < 0 or credit_count > 24:  # giving credits_valid definition w parameters and arguments for main
        # function
        return False
    else:
        return True


def full_time_part_time(credit_count):  # giving full_time_part_time a definition with parameters and arguments
    if credit_count >= 12:
        return 'full time'
    elif credit_count >= 6:
        return 'part time'
    else:
        return 'less than part time'


main()  # calling function
