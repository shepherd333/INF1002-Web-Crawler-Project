import numpy as np


def depreciation_value_per_year_error_handler(data_value):
    if len(data_value) < 2:
        data_value = np.nan

    else:
        data_value = data_value[1].split('/yr')
        try:
            desired_value = int(data_value[0].split(',')[0] + \
                                data_value[0].split(',')[
                                    1])  # Will fail on IndexError if tries to split '900' with a ',' in ['900','']
        except IndexError:
            desired_value = int(data_value[0])

        return desired_value


def depreciation_value_per_year_retrieval(parsed_listing_url):
    data_value = parsed_listing_url.find_all(class_="label")[1].findNextSibling().text.strip().split('$')
    depreciation_value_per_year = depreciation_value_per_year_error_handler(data_value)
    return depreciation_value_per_year

