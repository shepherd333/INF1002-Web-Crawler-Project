import numpy as np
import re

def power_error_handler(power_text):
    try:
        power_match = re.search(r'(\d+\.\d+)\s+kW', power_text)
        if power_match:
            return float(power_match.group(1))
    except (AttributeError, ValueError):
        pass
    return np.nan

def power_retrieval(listing_url):
    power_element = listing_url.find_all(class_='row_info')[10]
    if power_element:
        return power_error_handler(power_element.text)
    return np.nan



