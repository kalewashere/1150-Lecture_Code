import requests  # requests needs to be installed, once done usually is already loaded - if error occurs, hover + alt

# enter, install requests. process will complete if online


data = requests.get('https://catfact.ninja/fact').json()  # .get() retrieves data from requested url - .json()
# converts url to python code
print(data)

fact = data['fact']  # get value from data heap, helps us print it in a more readable way
print('A random cat fact is: ' + fact)  # prints retrieved fact in string
