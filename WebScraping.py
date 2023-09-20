import pandas as pd
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

#url that we want to scrape from
url ="https://www.sgcarmart.com/used_cars/listing.php?VEH=13"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
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
# Extract the text between the model div elements and store in an array without formatting
model_array = [div.get_text().strip() for div in model]
print(model_array)

#finding price
price= soup.find_all('div', style='width:67px; font-weight:bold;')
price_array=[div.get_text().strip() for div in price]
print(price_array)


# finding depreciation
depre=soup.find_all('div',style='width:101px;')
depre_array=[div.get_text().strip() for div in depre]
print(depre_array)

# finding reg date
reg_date =soup.findAll('div',style='width:89px;')
reg_date_array = [div.get_text().strip() for div in reg_date]
# remove vehicle type from this list
del reg_date_array[1::2]
print(reg_date_array)

# finding engine cap
eng_cap=soup.findAll('div',style='width:84px;')
eng_cap_array=[div.get_text().strip() for div in eng_cap]
print(eng_cap_array)

# finding mileage
mile=soup.findAll('div',style='width:83px;')
mile_array=[div.get_text().strip() for div in mile]
print(mile_array)

# finding vehicle type
veh_type=soup.findAll('div',style='width:89px;')
veh_type_arr=[div.get_text().strip() for div in veh_type]
# remove reg date from list
del veh_type_arr[::2]
print(veh_type_arr)

# printing data to csv file
df = pd.DataFrame({'Model':model_array,'Prices':price_array, 'Depreciation':depre_array, 'Reg Date':reg_date_array, 'Eng Cap':eng_cap_array, 'Mileage':mile_array, 'Vehicle Type':veh_type_arr})
df.to_csv('UsedCars_20sep.csv', index=False, encoding='utf-8')


