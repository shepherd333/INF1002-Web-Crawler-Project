import pandas as pd
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re

def get_html(url):
    # Define user-agent headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    req = Request(url, headers=headers)
    page = urlopen(req)
    html_bytes = page.read()
    return html_bytes.decode("utf-8")

def extract_data(html):
    soup = BeautifulSoup(html, 'html.parser') # Parse the HTML content
    # Create empty lists to store data
    listingid_set = set()
    listingid_array = []
    model_array = []
    price_array = []
    depre_array = []
    reg_date_array = []
    eng_cap_array = []
    mile_array = []
    veh_type_arr = []

    table = soup.find('table', style='margin-top:1px;')
    links = table.find_all('a', href=re.compile(r'info.php\?ID=\d+'))
    for link in links:
        href = link.get("href")  # Get the href attribute
        if href:
            # Extract the listing ID using regular expressions
            match = re.search(r'ID=(\d+)', href)
            if match:
                listing_id = match.group(1)
                # Check if the listing ID is unique before adding it
                if listing_id not in listingid_set:
                    listingid_set.add(listing_id)
    listingid_array = list(listingid_set)

    # finding model
    table = soup.find('table', style='margin-top:1px;')
    model = table.find_all('div', style='width:186px;padding-left:4px;')
    # Extract the text between the model div elements and store in the array without formatting
    model_array.extend([div.get_text().strip() for div in model])

    # finding price
    table = soup.find('table', style='margin-top:1px;')
    price = table.find_all('div', style='width:67px; font-weight:bold;')
    price_array.extend([div.get_text().strip().replace('$', '') for div in price])

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

    return listingid_array, model_array, price_array, depre_array, reg_date_array, eng_cap_array, mile_array, veh_type_arr

def scrape_multiple_pages(base_url, num_pages):
    # Create empty lists to append multiple pages data into
    listingid_array = []
    model_array = []
    price_array = []
    depre_array = []
    reg_date_array = []
    eng_cap_array = []
    mile_array = []
    veh_type_arr = []

    # Loop through the pages
    for page_number in range(1, num_pages):
        url = base_url.format(page_number * 100)
        html = get_html(url)  # Get HTML content

        # Extract data from HTML using extract_data function
        listingid_data, model_data, price_data, depre_data, reg_date_data, eng_cap_data, mile_data, veh_type_data = extract_data(
            html)

        # Extend lists with extracted data
        listingid_array.extend(listingid_data)
        model_array.extend(model_data)
        price_array.extend(price_data)
        depre_array.extend(depre_data)
        reg_date_array.extend(reg_date_data)
        eng_cap_array.extend(eng_cap_data)
        mile_array.extend(mile_data)
        veh_type_arr.extend(veh_type_data)

    return listingid_array, model_array, price_array, depre_array, reg_date_array, eng_cap_array, mile_array, veh_type_arr

def main():
    base_url = "https://www.sgcarmart.com/used_cars/listing.php?BRSR={}&RPG=100&AVL=2&VEH=0"
    num_pages = 3

    # Call the scrape_multiple_pages function to get data
    listingid_array, model_array, price_array, depre_array, reg_date_array, eng_cap_array, mile_array, veh_type_arr = scrape_multiple_pages(base_url, num_pages)

    # Create a DataFrame from the collected data
    df = pd.DataFrame({
        'ID': listingid_array,
        'Model': model_array,
        'Prices': price_array,
        'Depreciation': depre_array,
        'Reg Date': reg_date_array,
        'Eng Cap': eng_cap_array,
        'Mileage': mile_array,
        'Vehicle Type': veh_type_arr
    })

    # Set pandas options to display all columns
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.expand_frame_repr', False)

    # Remove rows with 'N.A.' or '-' in any column
    df = df[~df.isin(['N.A.', '-']).any(axis=1)]

    # Print the DataFrame
    print(df)

    # Save the DataFrame to a CSV file
    df.to_csv('UsedCars_20sep.csv', index=False, encoding='utf-8')


if __name__ == "__main__":
    main()