star_id = input('Please enter your StarID: ')

star_id_length = len(star_id)

if star_id:
    print('You have entered a StarID')
else:
    print('You have not entered a StarID')

if star_id_length == 8:
    print('Your StarID is the correct length. Thank you, now we we will verify your password.')
elif star_id_length > 8:
    print('Your StarId is too long. Your StarID should be no more than 8 characters long. Please try again.')
else:
    print('Your StarID is too short. Your password must be at least 8 characters long. Please try again.')