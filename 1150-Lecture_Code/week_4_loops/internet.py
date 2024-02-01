from urllib import request
from time import sleep
import winsound

url = 'https://www.google.com'
seconds_to_sleep_between_checks = 3

while True:
    print('Checking if you are online...')  # infinite loop-will run until stopped or computer shuts off
    try:
        request.urlopen(url).read()
        print('You are probably online!')
        winsound.MessageBeep()

    except:
        print('You are not online~')
    print(f'Sleeping for {seconds_to_sleep_between_checks} seconds.')
    sleep(seconds_to_sleep_between_checks)
