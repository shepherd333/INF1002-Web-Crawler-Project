import numpy as np
import requests
from bs4 import BeautifulSoup

def price_retrieval(parsed_listing_url):
    data_value = parsed_listing_url.find_all(class_='font_red')[0].text.strip()
    data_value = data_value.split('$')
    price = price_error_handling(data_value)
    return price


def price_error_handling(data_value):
    # Try-Exception error handling

    try:  # First try to deal with values higher than 1000
        price = data_value[1]  # will fail on IndexError if retrieves ['na'] scenario
        price = int(price.split(',')[0] + price.split(',')[
            1])  # Will fail on IndexError if tries to split '900' with a ',' in ['',900]

    except IndexError:  # Dealing with ['na'] and ['', 900'] scenarios
        try:
            price = int(data_value[1])  # Will fail on IndexError if ['na'] scenario
        except IndexError:  # Deals with ['na'] scenarios
            price = np.nan  # Stores NA values as nan

    return price


listing_url = 'https://www.sgcarmart.com/used_cars/info.php?ID=1238173'
listing_url2 = 'https://www.sgcarmart.com/used_cars/info.php?ID=1235109'
response = requests.get(listing_url)
response2 = requests.get(listing_url2)
parsed_listing_url = BeautifulSoup(response.text, 'lxml')
parsed_listing_url2 = BeautifulSoup(response2.text, 'lxml')
print(price_retrieval(parsed_listing_url))
print(price_retrieval(parsed_listing_url2))