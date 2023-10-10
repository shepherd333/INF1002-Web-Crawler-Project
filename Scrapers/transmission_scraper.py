
def transmission_retrieval(parsed_listing_url):
    try:
        transmission = parsed_listing_url.find_all(class_='row_info')[7].text
        return transmission.strip()  # Remove extra spaces and return the transmission info

    except (IndexError, AttributeError):
        return "Transmission info N/A"  # Return a default value if data is not found or cannot be parsed


