# while loop version of total program

total = 0
more_books = True

while more_books:
    book_price = float(input('Enter the price of book in $ '))
    total = total + book_price
    any_more = input('anymore books? Enter "Y" for yes and "N" for no. ')
    if any_more.upper() == 'N':
        more_books = False

print(f'Total for all of your books is ${total}')
# bonus question - my program did not stop for a lowercase n, it read it as a Y
# which is weird because I entered lowercase y on purpose to see if it ran and it did
