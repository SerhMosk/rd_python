# Task 1. Write a program that will make a request to one of the 5 sites
# and print the status code of the response, the name of the site, as well
# as the length of the HTML code from the response.
# The site for making a request must be selected randomly.
# Sites:
# - google.com,
# - facebook.com,
# - twitter.com,
# - amazon.com,
# - apple.com.

import random
import requests
from pprint import pprint

sites = [
    'google.com',
    'facebook.com',
    'twitter.com',
    'amazon.com',
    'apple.com'
]


def init_app():
    site = random.choice(sites)
    print(f'Request to the {site}')

    res = requests.get(f'https://{site}')

    # pprint(res.headers)
    print(f'Response status code: {res.status_code}')
    print(f'Content type: {res.headers["content-type"]}')
    print(f'Encoding: {res.headers["Content-Encoding"]}')
    print(f'Server: {res.headers.get("server")}')
    print('=' * 30)
    print(f'Page HTML-code length: {len(res.text)}')

    # for item in res:
    #     print(item)


# Run program
init_app()
