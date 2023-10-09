import requests
from bs4 import BeautifulSoup

def transmission_retrieval(parsed_listing_url):
    try:
        transmission = parsed_listing_url.find_all(class_='row_info')[7].text
        return transmission.strip()  # Remove extra spaces and return the transmission info

    except (IndexError, AttributeError):
        return "Transmission info N/A"  # Return a default value if data is not found or cannot be parsed

listing_url = 'https://www.sgcarmart.com/used_cars/info.php?ID=1238173'
listing_url2 = 'https://www.sgcarmart.com/used_cars/info.php?ID=1235109'
response = requests.get(listing_url)
response2 = requests.get(listing_url2)
parsed_listing_url = BeautifulSoup(response.text, 'lxml')
parsed_listing_url2 = BeautifulSoup(response2.text, 'lxml')

print(transmission_retrieval(parsed_listing_url))
print(transmission_retrieval(parsed_listing_url2))
