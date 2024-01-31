# allows python to use code to do things like choosing a random option, or random number
import random  # include random library from python standard library code - optional to make available for program
# import will remain light - this means code is unneeded and not entered in correctly. Command will remain light until
# choices are entered and . function is given
# next line will choose a random string from the choices 'rock', 'paper', or 'scissors'
#
computer_choice = random.choice(['rock', 'paper', 'scissors']) # square brackets = make a list of strings
# .choice is a python function


human_choice = input('Enter "rock", "paper", or "scissors": ')

if human_choice != "rock" and human_choice != 'paper' and human_choice != 'scissors':
    print('You need to enter rock, paper, or scissors')

else:
    print('The computer chooses ' + computer_choice)
    # situation can call for a tie
    if human_choice == computer_choice:
        print('You both chose ' + human_choice + ', the game is a TIE.')
    # Human wins
    elif human_choice == 'rock' and computer_choice == 'scissors':
        print('Rock beats scissors. You win!')
    elif human_choice == 'scissors' and computer_choice == 'paper':
        print('Scissors beats paper. You win!')
    elif human_choice == 'paper' and computer_choice == 'rock':
        print('Paper beats rock. You win!')
    # could write out code for each time computer beats human, but easiest to use
    else:
        print('So sorry, ' + computer_choice + ' beats ' + human_choice + '. You loose.')
