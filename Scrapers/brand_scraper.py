import requests
from bs4 import BeautifulSoup


def brand_retrieval(parsed_url):
    if not parsed_url:
        raise ValueError("Failed to retrieve data")

    # Locate the <a> element with the specified class
    brand = parsed_url.find('a', class_='nounderline globaltitle')
    if brand:
        brand = brand.text.split()[0]
        return brand
    else:
        raise ValueError("Brand N.A")


listing_url = 'https://www.sgcarmart.com/used_cars/info.php?ID=1238173'
listing_url2 = 'https://www.sgcarmart.com/used_cars/info.php?ID=1235109'
response = requests.get(listing_url)
response2 = requests.get(listing_url2)
parsed_listing_url = BeautifulSoup(response.text, 'lxml')
parsed_listing_url2 = BeautifulSoup(response2.text, 'lxml')

print(brand_retrieval(parsed_listing_url))
print(brand_retrieval(parsed_listing_url2))
