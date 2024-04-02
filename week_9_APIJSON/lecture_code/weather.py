import requests

url = 'https://api.weather.gov/gridpoints/MPX/107,71/forecast'  # a lot of data, but we can work with it

response = requests.get(url).json()
print(response)

properties = response['properties']
# print(properties)
forecast_periods = properties['periods']
# print(forecast_periods)

for period in forecast_periods:  # this is the most readable for users - example
    name = period['name']
    temp = period['temperature']
    forecast = period['detailedForecast']
    print(f'{name:<17} {temp:<17} {forecast}.')  # the ':<17' formats data to be even MORE readable - this program is
    # a godo template/reference point for future referral
    # you can EMOJIS??
    
