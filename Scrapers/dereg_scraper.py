import numpy as np


# Write a function to retrieve dereg value from a parsed url
def dereg_value_retrieval(parsed_listing_url):
    # Splits into ['NA'], or ['$11,026', 'as', 'of', 'today', '(change)'] or ['$900', 'as', 'of', 'today', '(change)']
    data_value = parsed_listing_url.find_all(class_='row_info')[2].text.strip().split()

    dereg_value_from_scrape_date = dereg_value_error_handler(data_value)
    return dereg_value_from_scrape_date


def dereg_value_error_handler(data_value):
    if len(data_value) < 2:  # Deals with ['NA'] scenario
        dereg_value_from_scrape_date = np.nan

    else:
        data_value = data_value[0].split('$')[1]  # Puts input into '11,026' or '900' format
        try:
            dereg_value_from_scrape_date = \
                int(data_value.split(',')[0] + \
                    data_value.split(',')[1])  # Will fail on IndexError if tries to split '900' with a ',' in ['',900]
        except IndexError:
            dereg_value_from_scrape_date = int(data_value.strip())

        return dereg_value_from_scrape_date

