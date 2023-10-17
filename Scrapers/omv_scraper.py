import numpy as np


def omv_error_handler(data_value):
    try:
        omv_str = data_value[1].replace(',', '')
        omv = int(omv_str)
    except (IndexError, ValueError):
        omv = np.nan
    return omv


def omv_retrieval(listing_url):
    row_info = listing_url.find_all(class_='row_info')[8].text
    data_value = row_info.split('$')
    omv = omv_error_handler(data_value)
    return omv

