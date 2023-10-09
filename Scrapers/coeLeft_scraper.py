import requests
from bs4 import BeautifulSoup


# Retrieve into usable format for link
def days_of_coe_retrieval(parsed_listing_url):
    try:
        if not parsed_listing_url:
            print("failed to retrieve data")
            return None

        rows = parsed_listing_url.find_all(class_='row_bg')

        if len(rows) >= 2:
            td_elements = rows[1].find_all('td')
            if len(td_elements) >= 4:
                text = td_elements[3].text
                if 'COE' in text:
                    coe_text = text.split('COE')[0].strip()
                    return yr_mm_dd_cleaner(coe_text)

        # If the expected elements are not found, return None or an appropriate default value.
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None


# Define a function to calculate days of COE left
def yr_mm_dd_cleaner(str1):
    # Convert days_of_coe_left_yy_mm_dd to days
    year_index = str1.find('yr')
    if year_index == -1:
        year = 0
    else:
        year = int(str1[year_index - 1])

    mth_index = str1.find('mth')
    if mth_index == -1:
        mth = 0
    else:
        mth = int(str1[mth_index - 1])

    day_index = str1.find('day')
    if day_index == -1:
        day = 0
    else:
        day = int(str1[day_index - 1])

    days_of_coe_left = (year * 365) + (mth * 30) + day
    return days_of_coe_left


listing_url = 'https://www.sgcarmart.com/used_cars/info.php?ID=1238173'
listing_url2 = 'https://www.sgcarmart.com/used_cars/info.php?ID=1235109'
response = requests.get(listing_url)
response2 = requests.get(listing_url2)
parsed_listing_url = BeautifulSoup(response.text, 'lxml')
parsed_listing_url2 = BeautifulSoup(response2.text, 'lxml')

print(days_of_coe_retrieval(parsed_listing_url))
print(days_of_coe_retrieval(parsed_listing_url2))