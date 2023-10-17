import numpy as np


def curb_weight_error_handler(data_value):
    try:
        value_parts = data_value[0].split(',')
        desired_value = int(''.join(value_parts))
    except (IndexError, ValueError):
        desired_value = np.nan
    return desired_value


def curb_weight_retrieval(listing_url):
    row_info = listing_url.find_all(class_='row_info')[5].text
    data_value = row_info.split()
    curb_weight = curb_weight_error_handler(data_value)
    return curb_weight

