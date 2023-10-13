import numpy as np


def error_handler(data_value):
    if len(data_value) < 2:  # deals with ['NA'] input
        desired_value = np.nan

    else:
        try:
            desired_value = int(data_value[1].split(',')[0] +\
                                data_value[1].split(',')[1])   # Will fail on index error if try to split 900
        except IndexError:
            desired_value = int(data_value[1])
    return desired_value

# Retrieve ARF based on parsed listing url
def arf_retrieval(listing_url):
    data_value = listing_url.find_all(class_='row_info')[9].text.split('$')
    arf = error_handler(data_value)
    return arf


