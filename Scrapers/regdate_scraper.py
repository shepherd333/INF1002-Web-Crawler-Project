
def registered_date_retrieval(parsed_listing_url):
    try:
        if not parsed_listing_url:
            return "Failed to retrieve data"

        reg_date = parsed_listing_url.find_all(class_='row_bg')[1].find_all('td')[3].text.split()[0].split('(')[0]
        if reg_date:
            return reg_date
        else:
            return "registration date N.A."
    except (IndexError, AttributeError):
        return "registration date N.A."

