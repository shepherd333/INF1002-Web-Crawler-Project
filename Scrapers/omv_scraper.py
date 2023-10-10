import numpy as np


def omv_error_handler(data_value):
    if len(data_value) < 2:  # deals iwth ['NA'] input
        omv = np.nan

    else:
        try:
            omv = int(data_value[1].split(',')[0] + \
                      data_value[1].split(',')[1])
        except IndexError:
            omv = int(data_value[1])
    return omv


def omv_retrieval(parsed_listing_url):
    data_value = parsed_listing_url.find_all(class_='row_info')[8].text.split('$')
    # Splits data into ['', '21,967'], ['','900'] or ['NA'] format for input into error function

    omv = omv_error_handler(data_value)
    return omv
