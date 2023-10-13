# Retrieve into usable format for link
def days_of_coe_retrieval(listing_url):
    try:
        if not listing_url:
            print("failed to retrieve data")
            return None

        rows = listing_url.find_all(class_='row_bg')

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
def yr_mm_dd_cleaner(str_coeleft):
    def extract_value(substring):
        index = str_coeleft.find(substring)
        if index != -1:
            return int(str_coeleft[index - 1])
        return 0

    year = extract_value('yr')
    month = extract_value('mth')
    day = extract_value('day')

    days_of_coe_left = (year * 365) + (month * 30) + day
    return days_of_coe_left



