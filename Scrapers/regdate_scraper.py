import requests
from bs4 import BeautifulSoup

def registered_date_retrieval(parsed_listing_url):
    try:
        if not parsed_listing_url:
            return "Failed to retrieve data"

        reg_date = parsed_listing_url.find_all(class_='row_bg')[1].find_all('td')[3].text.split()[0].split('(')[0]
        if reg_date:
            return reg_date
        else:
            return "registration date N.A."
    except (IndexError, AttributeError):
        return "registration date N.A."

listing_url = 'https://www.sgcarmart.com/used_cars/info.php?ID=1238173'
listing_url2 = 'https://www.sgcarmart.com/used_cars/info.php?ID=1235109'
response = requests.get(listing_url)
response2 = requests.get(listing_url2)
parsed_listing_url = BeautifulSoup(response.text, 'lxml')
parsed_listing_url2 = BeautifulSoup(response2.text, 'lxml')

print(registered_date_retrieval(parsed_listing_url))
print(registered_date_retrieval(parsed_listing_url2))
