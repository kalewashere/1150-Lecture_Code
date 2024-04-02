import requests

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

response = requests.get(url).json()

print(response)  # this is a response to a dictionary in a dictionary

bpi = response['bpi']  # accessing dictionary
print(bpi)

usd_data = bpi['USD']  # accessing data in dictionary within dictionary
print(usd_data)

rate = usd_data['rate_float']  # accessing data further inside dictionary, inside dictionary
print(rate)

# also solve like this

usd_exchange_rate = response['bpi']['USD']['rate_float']
print(usd_exchange_rate)

