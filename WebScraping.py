import pandas as pd
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

#url that we want to scrape from
base_url ="https://www.sgcarmart.com/used_cars/listing.php?BRSR={}&RPG=100&AVL=2&VEH=0"

# set number of pages to scrape from ( 1 page has 100 listings sorted by latest )
num_pages = 5

# Define user-agent headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

# Create empty lists to store data
model_array = []
price_array = []
depre_array = []
reg_date_array = []
eng_cap_array = []
mile_array = []
veh_type_arr = []

# Loop through the pages
for page_number in range(0, num_pages):
    url = base_url.format(page_number * 100)

    # get html of website using requests
    req = Request(url, headers=headers)
    page = urlopen(req)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    # print(html)

    # Parse the HTML content
    soup = BeautifulSoup(html, 'html.parser')

    # finding model
    model = soup.find_all('div', style='width:186px;padding-left:4px;')
    # Extract the text between the model div elements and store in the array without formatting
    model_array.extend([div.get_text().strip() for div in model])

    # finding price
    price = soup.find_all('div', style='width:67px; font-weight:bold;')
    price_array.extend([div.get_text().strip() for div in price])

    # finding depreciation
    depre = soup.find_all('div', style='width:101px;')
    depre_array.extend([div.get_text().strip() for div in depre])

    # finding reg date
    reg_date = soup.findAll('div', style='width:89px;')
    reg_date_values = [div.get_text().strip() for div in reg_date]
    # remove vehicle type from this list
    del reg_date_values[1::2]
    reg_date_array.extend(reg_date_values)

    # finding engine cap
    eng_cap = soup.findAll('div', style='width:84px;')
    eng_cap_array.extend([div.get_text().strip() for div in eng_cap])

    # finding mileage
    mile = soup.findAll('div', style='width:83px;')
    mile_array.extend([div.get_text().strip() for div in mile])

    # finding vehicle type
    veh_type = soup.findAll('div', style='width:89px;')
    veh_type_values = [div.get_text().strip() for div in veh_type]
    # remove reg date from list
    del veh_type_values[::2]
    veh_type_arr.extend(veh_type_values)


# printing data to csv file
df = pd.DataFrame({'Model':model_array,'Prices':price_array, 'Depreciation':depre_array, 'Reg Date':reg_date_array, 'Eng Cap':eng_cap_array, 'Mileage':mile_array, 'Vehicle Type':veh_type_arr})
df.to_csv('UsedCars_20sep.csv', index=False, encoding='utf-8')


