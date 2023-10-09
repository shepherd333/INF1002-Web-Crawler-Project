import requests
import numpy as np
from bs4 import BeautifulSoup


def curb_weight_error_handler(data_value):
    if len(data_value) < 2:  # deals with ['NA'] input
        desired_value = np.nan

    else:
        try:
            desired_value = int(data_value[0].split(',')[0] +\
                                       data_value[0].split(',')[1])  # Will fail on index error if try to split 900
        except IndexError:
            desired_value = int(data_value[0])
    return desired_value


def curb_weight_retrieval(parsed_listing_url):
    data_value = parsed_listing_url.find_all(class_='row_info')[5].text.split()
    curb_weight = curb_weight_error_handler(data_value)
    return curb_weight

listing_url = 'https://www.sgcarmart.com/used_cars/info.php?ID=1238173'
listing_url2 = 'https://www.sgcarmart.com/used_cars/info.php?ID=1235109'
response = requests.get(listing_url)
response2 = requests.get(listing_url2)
parsed_listing_url = BeautifulSoup(response.text, 'lxml')
parsed_listing_url2 = BeautifulSoup(response2.text, 'lxml')

print(curb_weight_retrieval(parsed_listing_url))
print(curb_weight_retrieval(parsed_listing_url2))