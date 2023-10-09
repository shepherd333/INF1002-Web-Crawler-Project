import requests
from bs4 import BeautifulSoup

# Define a function to retrieve the number of owners from a parsed listing url
def number_of_owners_retrieval(parsed_listing_url):
    no_of_owners = number_of_owners_error_handler(parsed_listing_url)
    return no_of_owners

def number_of_owners_error_handler(parsed_listing_url):
    try:
        owners_info = parsed_listing_url.find_all(class_='row_info')[-1].text.strip()
        # Extract the number of owners from the text (e.g., 'More than 6' to 6)
        if 'More than' in owners_info:
            no_of_owners = int(owners_info.split('More than')[-1].strip())
        else:
            no_of_owners = int(owners_info)
    except (ValueError, IndexError):
        no_of_owners = None  # Handle the case where the number of owners is not available or cannot be parsed
    return no_of_owners

listing_url = 'https://www.sgcarmart.com/used_cars/info.php?ID=1238173'
listing_url2 = 'https://www.sgcarmart.com/used_cars/info.php?ID=1235109'
response = requests.get(listing_url)
response2 = requests.get(listing_url2)
parsed_listing_url = BeautifulSoup(response.text, 'lxml')
parsed_listing_url2 = BeautifulSoup(response2.text, 'lxml')

print(number_of_owners_retrieval(parsed_listing_url))
print(number_of_owners_retrieval(parsed_listing_url2))
