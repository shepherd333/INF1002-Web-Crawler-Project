import requests
import numpy as np
from bs4 import BeautifulSoup
import re

def power_retrieval(parsed_listing_url):
    power_element = parsed_listing_url.find_all(class_='row_info')[10]
    if power_element:
        power_text = power_element.text
        power_match = re.search(r'(\d+\.\d+)\s+kW', power_text)
        if power_match:
            power_kW = float(power_match.group(1))
            return power_kW
    return np.nan

listing_url = 'https://www.sgcarmart.com/used_cars/info.php?ID=1238173'
listing_url2 = 'https://www.sgcarmart.com/used_cars/info.php?ID=1235109'
response = requests.get(listing_url)
response2 = requests.get(listing_url2)
parsed_listing_url = BeautifulSoup(response.text, 'lxml')
parsed_listing_url2 = BeautifulSoup(response2.text, 'lxml')

print(power_retrieval(parsed_listing_url))
print(power_retrieval(parsed_listing_url2))
