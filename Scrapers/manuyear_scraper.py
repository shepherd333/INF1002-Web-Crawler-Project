import requests
from bs4 import BeautifulSoup

# Define an error handler function for manufactured_year_retrieval
def manufactured_year_error_handler(data):
    try:
        manufactured_year = data.find_all(class_='row_info')[6].text
        return manufactured_year
    except (IndexError, AttributeError):
        return "N/A"  # Return a default value if data is not found or cannot be parsed

# Define a function that returns the manufactured date using a parsed html
def manufactured_year_retrieval(parsed_listing_url):
    manufactured_year = manufactured_year_error_handler(parsed_listing_url)
    manufactured_year = manufactured_year.replace(" ", "")
    manufactured_year = manufactured_year.strip()
    return manufactured_year

listing_url = 'https://www.sgcarmart.com/used_cars/info.php?ID=1238173'
listing_url2 = 'https://www.sgcarmart.com/used_cars/info.php?ID=1235109'
response = requests.get(listing_url)
response2 = requests.get(listing_url2)
parsed_listing_url = BeautifulSoup(response.text, 'lxml')
parsed_listing_url2 = BeautifulSoup(response2.text, 'lxml')

print(manufactured_year_retrieval(parsed_listing_url))
print(manufactured_year_retrieval(parsed_listing_url2))
