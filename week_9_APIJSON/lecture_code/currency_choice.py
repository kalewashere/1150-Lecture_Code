import requests

url = 'https://1150-exchange-rates.azurewebsites.net/latest?base=USD'

response = requests.get(url).json()
print(response)

rates = response['rates']
print(rates)

dollars = float(input('Enter number of dollars: '))  # asks user to enter amount of USD to convert
print('Here are the currency codes: ')  # this tells user they are about to see currency codes
list_of_codes = list(rates.keys())  # this puts our keys into a list for the user to see, stored in variable for us to
# use
list_of_codes.sort()  # sorts keys alpha, easier for user to read and decide
print(', '.join(list_of_codes))  # joins list of currency codes, separated by comma
currency_code = input('Enter currency code to convert to: ')  # asking user to choose from list provided

exchange_rate = rates.get(currency_code)  # for example JPY
if exchange_rate:
    converted_value = dollars * exchange_rate
    print(f'${dollars} is equal to {converted_value:.2f} {currency_code}.')
else:
    print('Not a valid country code.')  # can also solve with example below

# if exchange_rate is None:
#   print('That is not a valid country code.')
# else:
#   converted_value = dollars * exchange_rate
#   print(f'${dollars} is equal to {converted_value:.2f} {currency_code}.')
