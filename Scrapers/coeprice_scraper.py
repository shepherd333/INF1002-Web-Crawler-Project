import numpy as np

def coe_error_handler(data_value):
    try:
        coe_value = int(''.join(data_value[1].split(',')[:2]))
    except (IndexError, ValueError):
        coe_value = np.nan
    return coe_value

def coe_retrieval(listing_url):
    row_info = listing_url.find_all(class_='row_info')[3].text
    data_value = row_info.split('$')
    coe_from_scrape_date = coe_error_handler(data_value)
    return coe_from_scrape_date
