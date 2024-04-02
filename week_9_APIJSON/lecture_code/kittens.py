import requests

picture_url = 'https://images.dnr.state.mn.us/destinations/state_parks/1_large/SPK00103_003.jpg'  # if we want more
# pictures, we can turn url variable into a list - we use square brackets, and commas to separate urls.
# updated place kitten urls were not loading for me, so I was unable to try multi-url responses.

# picture_urls = ['this is where I would enter a list of urls',        remember to be very careful with indentation
#                 'each url separated by comma',
#                 'inbetween square brackets']
# for index, url in enumerate(picture_urls):     including index will help us name multiple files if there is more than
#                                                one to download
#          response = requests.get(url)
#          filename = f'nature_{index}.jpg'
#          with open(filename, 'wb') as file:    # including filename will add the index number to the file saved to
#                                                help us differentiate between files
#              for chunk in response.iter_content():
#                  file.write(chunk)

response = requests.get(picture_url)

with open('picture.jpeg', 'wb') as file:
    for chunk in response.iter_content():
        file.write(chunk)


# this was included in video lecture, will ask about this in class 4/3/24
"""url_parts = url.split('/')
filename = url_parts.pop() # last part - use pop
print(filename) # SPK00103_003.jpg"""