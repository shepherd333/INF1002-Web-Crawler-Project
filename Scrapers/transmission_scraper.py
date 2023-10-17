import numpy as np


def transmission_error_handler(transmission):
    if transmission:
        return transmission.strip()
    return np.nan


def transmission_retrieval(listing_url):
    try:
        transmission = listing_url.find_all(class_='row_info')[7].text
        return transmission_error_handler(transmission)
    except (IndexError, AttributeError):
        return np.nan
