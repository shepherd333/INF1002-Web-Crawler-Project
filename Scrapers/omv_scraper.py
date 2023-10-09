import requests
import numpy as np
from bs4 import BeautifulSoup


# Define a function that retrieves omv based on a parsed listing url
def omv_error_handler(data_value):
    if len(data_value) < 2:  # deals iwth ['NA'] input
        omv = np.nan

    else:
        try:
            omv = int(data_value[1].split(',')[0] + \
                      data_value[1].split(',')[1])  # Will fail on index error if try to split 900
        except IndexError:
            omv = int(data_value[1])
    return omv


def omv_retrieval(parsed_listing_url):
    data_value = parsed_listing_url.find_all(class_='row_info')[8].text.split('$')
    # Splits data into ['', '21,967'], ['','900'] or ['NA'] format for input into error function

    omv = omv_error_handler(data_value)
    return omv

listing_url = 'https://www.sgcarmart.com/used_cars/info.php?ID=1238319'
listing_url2 = 'https://www.sgcarmart.com/used_cars/info.php?ID=1235109'
response = requests.get(listing_url)
response2 = requests.get(listing_url2)
parsed_listing_url = BeautifulSoup(response.text, 'lxml')
parsed_listing_url2 = BeautifulSoup(response2.text, 'lxml')

print(omv_retrieval(parsed_listing_url))
print(omv_retrieval(parsed_listing_url2))