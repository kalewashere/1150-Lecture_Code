# loop examples while loops - loops that repeat while some condition is true - slightly less common could be repeat
# while input is invalid (ie incorrect pw) could repeat while game is playing, loop ends = game-over used in cases
# where you're not exactly sure how long the loop will be while True:      - made this line a comment to not break
# code and refer back to if needed print('this is a loop')  - comment as well for ref. can be used 'no times' if
# input is valid, once if it invalid and then valid, or more depending on how long the user takes to enter correctly,


# for loop example - more useful and common, used when you know how many times you are going to need a loop
favorite_number = 5
# can use commands, set variables, use if, elif, else statements with for loops
for number in range(10):
    print(number + 1)
    # programs, or computers in general, start counting at 0
    if number == 5:
        print('That is my favorite number!')
