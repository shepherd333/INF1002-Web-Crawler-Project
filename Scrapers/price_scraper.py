import numpy as np


def price_retrieval(listing_url):
    data_value = listing_url.find_all(class_='font_red')[0].text.strip()
    price = price_error_handling(data_value)
    return price


def price_error_handling(data_value):
    try:
        price_str = ''.join(filter(str.isdigit, data_value))

        price = int(price_str)
    except (ValueError, IndexError):
        price = np.nan

    return price

