import numpy as np

def depreciation_value_per_year_error_handler(data_value):
    try:
        value_parts = data_value[1].split('/yr')
        desired_value = int(''.join(value_parts[0].split(',')))
    except (IndexError, ValueError):
        desired_value = np.nan
    return desired_value

def depreciation_value_per_year_retrieval(listing_url):
    label = listing_url.find_all(class_="label")[1].findNextSibling()
    data_value = label.text.strip().split('$')
    depreciation_value_per_year = depreciation_value_per_year_error_handler(data_value)
    return depreciation_value_per_year
