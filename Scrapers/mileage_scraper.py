import numpy as np


def mileage_error_handler(data_value):
    if len(data_value) < 2:  # Deals with ['na'] scenarios
        mileage_km = np.nan  # Stores NA values as nan

    else:
        try:
            mileage_km = int(data_value[0].strip().split(',')[0] + data_value[0].strip().split(',')[1])
        except IndexError:  # Will fail on IndexError if tries to split '900' with a ',' in ['',900]
            mileage_km = int(data_value[0].strip())

    return mileage_km


def mileage_retrieval(parsed_listing_url):
    data_value = parsed_listing_url.find_all(class_='row_info')[0].text.strip()
    data_value = data_value.split('km')
    mileage_km = mileage_error_handler(data_value)

    return mileage_km
