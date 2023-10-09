import requests
from bs4 import BeautifulSoup

def type_of_vehicle_retrieval(parsed_listing_url):
    type_of_vehicle = type_of_vehicle_error_handler()  # Initialize with a default value
    try:
        type_of_vehicle_element = parsed_listing_url.find(class_='row_bg1')
        if type_of_vehicle_element:
            links = type_of_vehicle_element.find_all('a')
            if links:
                type_of_vehicle = links[0].text
    except Exception as e:
        print(f"An error occurred while retrieving the vehicle type: {e}")
    return type_of_vehicle

def type_of_vehicle_error_handler():
    return "N/A"

listing_url = 'https://www.sgcarmart.com/used_cars/info.php?ID=1238173'
listing_url2 = 'https://www.sgcarmart.com/used_cars/info.php?ID=1235109'
response = requests.get(listing_url)
response2 = requests.get(listing_url2)
parsed_listing_url = BeautifulSoup(response.text, 'lxml')
parsed_listing_url2 = BeautifulSoup(response2.text, 'lxml')

print(type_of_vehicle_retrieval(parsed_listing_url))
print(type_of_vehicle_retrieval(parsed_listing_url2))
