import requests

url = 'https://1150-exchange-rates.azurewebsites.net/latest?base=USD&symbols=EUR'  # this is the dictionary we are
# pulling data from

dollars = float(input('Enter number of dollars: '))  # asking the user to enter dollar amount to convert

response = requests.get(url).json()

print(response)  # prints complex response
rates = response['rates']  # setting rates in variable
print(rates)
euro_exchange_rate = rates['EUR']  # setting euros in variable
print(euro_exchange_rate)  # this will print only the euro exchange rate

euros = dollars * euro_exchange_rate  # math for mathing - this will tell us and user what the amount of dollars will
# be converted to
print(f'${dollars} is equal to {euros:.2f} euros.')  # format string, including math, tells user what the amount of
# euros will be for the exchange in a nice, concise way
