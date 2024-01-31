secret_password = 'mittens' # in python, passwords are case-sensitive
# upper and lowercase are registered as their own character

password = input('enter the secret password: ')

if password == secret_password: # dont forget the condition command, :
    print('Welcome, verified User!')
else:
    print('So sorry, wrong password :/')
print('Thanks for using the program, User!')