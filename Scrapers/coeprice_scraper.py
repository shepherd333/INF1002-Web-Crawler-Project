import numpy as np

# Write a function to retrieve COE as of today from a parsed listing url
def coe_error_handler(data_value):
    if len(data_value) < 2:  # deals iwth ['NA'] input
        coe_from_scrape_date = np.nan

    else:
        try:
            coe_from_scrape_date = int(data_value[1].split(',')[0] +\
                                       data_value[1].split(',')[1])  # Will fail on index error if try to split 900
        except IndexError:
            coe_from_scrape_date = int(data_value[1])
    return coe_from_scrape_date


def coe_retrieval(parsed_listing_url):
    data_value = parsed_listing_url.find_all(class_='row_info')[3].text.split('$')
    coe_from_scrape_date = coe_error_handler(data_value)
    return coe_from_scrape_date