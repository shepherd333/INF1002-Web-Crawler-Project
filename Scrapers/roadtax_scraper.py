import requests
from bs4 import BeautifulSoup

def road_tax_retrieval(parsed_listing_url):
    string_data = parsed_listing_url.find_all(class_='row_info')[1].text.strip()
    road_tax_per_year = road_tax_error_handler(string_data)
    return road_tax_per_year

def road_tax_error_handler(string_data):
    if string_data == 'NA':
        return None  # Return None for "NA" values

    try:
        # Remove '$' character and split string_data into a list
        parts = string_data.replace('/yr', '').strip().split('$')

        if len(parts) == 2:
            # Handle values like ['', 1,000] or ['', 900]
            road_tax_per_year = int(''.join(parts[1].split(',')))
        else:
            # Handle values like ['1,000/yr']
            road_tax_per_year = int(''.join(parts[0].split(',')))

        return road_tax_per_year

    except (ValueError, IndexError):
        return None  # Return None for errors and unexpected formats

listing_url = 'https://www.sgcarmart.com/used_cars/info.php?ID=1238173'
listing_url2 = 'https://www.sgcarmart.com/used_cars/info.php?ID=1235109'
response = requests.get(listing_url)
response2 = requests.get(listing_url2)
parsed_listing_url = BeautifulSoup(response.text, 'lxml')
parsed_listing_url2 = BeautifulSoup(response2.text, 'lxml')
print(road_tax_retrieval(parsed_listing_url))
print(road_tax_retrieval(parsed_listing_url2))
