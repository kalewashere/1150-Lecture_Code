# Invoice Program
# • Ask for the name of a product sold
item_name = input('Enter name of item: ')
# • Ask how many were sold
items_sold = int(input('Enter quantity of ' + item_name + ' sold: '))
# • Ask for the price of one item
unit_price = float(input('Enter unit price of ' + item_name + ': ')) # float number for decimal points
# • Do the math to figure out the total price
total = unit_price * items_sold
# • Print a neat invoice with all the data in
print() # print blank line
print(item_name + ' sales')
print('Quantity sold: ' + str(items_sold)) # str to combine letters and numbers into sentence
print('Unit price: ' + str(unit_price))
print('Total: ' + str(total))
# • Comment code