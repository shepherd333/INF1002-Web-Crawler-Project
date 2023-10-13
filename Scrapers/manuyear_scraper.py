import numpy as np

def manufactured_year_error_handler(data_value):
    try:
        manufactured_year = data_value[6].text
        return manufactured_year.strip()
    except (IndexError, AttributeError):
        return "N/A"

def manufactured_year_retrieval(listing_url):
    row_info = listing_url.find_all(class_='row_info')
    manufactured_year = manufactured_year_error_handler(row_info)
    return manufactured_year


