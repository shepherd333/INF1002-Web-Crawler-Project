import numpy as np


def road_tax_error_handler(string_data):
    if string_data == 'NA':
        return np.nan

    try:
        parts = string_data.replace('/yr', '').strip().split('$')

        if len(parts) == 2:
            road_tax_per_year = int(''.join(parts[1].split(',')))
        else:
            road_tax_per_year = int(''.join(parts[0].split(',')))

        return road_tax_per_year

    except (ValueError, IndexError):
        return np.nan


def road_tax_retrieval(listing_url):
    string_data = listing_url.find_all(class_='row_info')[1].text.strip()
    road_tax_per_year = road_tax_error_handler(string_data)
    return road_tax_per_year
