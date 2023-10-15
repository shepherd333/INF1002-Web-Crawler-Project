import numpy as np


def registered_date_error_handler(reg_date):
    try:
        if reg_date:
            return reg_date
    except (AttributeError, IndexError):
        pass
    return np.nan


def registered_date_retrieval(listing_url):
    try:
        if not listing_url:
            return "Failed to retrieve data"

        reg_date_element = listing_url.find_all(class_='row_bg')[1].find_all('td')[3].text
        reg_date = reg_date_element.split()[0].split('(')[0]

        return registered_date_error_handler(reg_date)
    except (IndexError, AttributeError):
        return np.nan


