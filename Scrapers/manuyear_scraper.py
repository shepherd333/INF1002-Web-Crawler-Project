def manufactured_year_error_handler(data):
    try:
        manufactured_year = data.find_all(class_='row_info')[6].text
        return manufactured_year
    except (IndexError, AttributeError):
        return "N/A"  # Return a default value if data is not found or cannot be parsed


# Define a function that returns the manufactured date using a parsed html
def manufactured_year_retrieval(parsed_listing_url):
    manufactured_year = manufactured_year_error_handler(parsed_listing_url)
    manufactured_year = manufactured_year.replace(" ", "")
    manufactured_year = manufactured_year.strip()
    return manufactured_year

