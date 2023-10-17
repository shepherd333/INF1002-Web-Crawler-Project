import numpy as np

def dereg_value_error_handler(data_value):
    if len(data_value) < 2:
        return np.nan

    try:
        value_parts = data_value[0].split('$')[1]
        desired_value = int(''.join(value_parts.split(',')))
    except (IndexError, ValueError):
        desired_value = np.nan

    return desired_value

def dereg_value_retrieval(listing_url):
    row_info = listing_url.find_all(class_='row_info')[2].text.strip().split()
    dereg_value_from_scrape_date = dereg_value_error_handler(row_info)
    return dereg_value_from_scrape_date


