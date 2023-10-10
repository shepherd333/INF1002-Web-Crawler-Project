import numpy as np


def curb_weight_error_handler(data_value):
    if len(data_value) < 2:  # deals with ['NA'] input
        desired_value = np.nan

    else:
        try:
            desired_value = int(data_value[0].split(',')[0] +\
                                       data_value[0].split(',')[1])  # Will fail on index error if try to split 900
        except IndexError:
            desired_value = int(data_value[0])
    return desired_value


def curb_weight_retrieval(parsed_listing_url):
    data_value = parsed_listing_url.find_all(class_='row_info')[5].text.split()
    curb_weight = curb_weight_error_handler(data_value)
    return curb_weight
