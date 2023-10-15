def number_of_owners_retrieval(listing_url):
    no_of_owners = number_of_owners_error_handler(listing_url)
    return no_of_owners


def number_of_owners_error_handler(listing_url):
    try:
        owners_info = listing_url.find_all(class_='row_info')[-1].text.strip()
        # Extract the number of owners from the text (e.g., 'More than 6' to 6)
        if 'More than' in owners_info:
            no_of_owners = int(owners_info.split('More than')[-1].strip())
        else:
            no_of_owners = int(owners_info)
    except (ValueError, IndexError):
        no_of_owners = None  # Handle the case where the number of owners is not available or cannot be parsed
    return no_of_owners

