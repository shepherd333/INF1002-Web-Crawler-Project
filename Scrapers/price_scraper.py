import numpy as np


def price_retrieval(listing_url):
    data_value = listing_url.find_all(class_='font_red')[0].text.strip()
    data_value = data_value.split('$')
    price = price_error_handling(data_value)
    return price


def price_error_handling(data_value):
    try:
        price = data_value[1]
        price = int(price.split(',')[0] + price.split(',')[
            1])

    except IndexError:
        try:
            price = int(data_value[1])
        except IndexError:
            price = np.nan

    return price
