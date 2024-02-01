# i need to know how many books someone needed to buy
number_of_books = int(input('How many books do you need to buy? '))

total = 0

for book in range(number_of_books):   # we can put any logic in a for loops; if statements, variables, more loops even
    #  the loop will run until number_of_books value is met
    book_price = float(input('Enter book price in $ '))
    if book_price == 0:
        print('You get a free book!')
    total = total + book_price

# print('The total price for all books is $' + str(total))
print(f'The total price for all your books is ${total}')
