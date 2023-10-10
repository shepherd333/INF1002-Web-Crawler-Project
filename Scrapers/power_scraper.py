import numpy as np
import re


def power_retrieval(parsed_listing_url):
    power_element = parsed_listing_url.find_all(class_='row_info')[10]
    if power_element:
        power_text = power_element.text
        power_match = re.search(r'(\d+\.\d+)\s+kW', power_text)
        if power_match:
            power_kW = float(power_match.group(1))
            return power_kW
    return np.nan


