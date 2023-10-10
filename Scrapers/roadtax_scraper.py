def road_tax_retrieval(parsed_listing_url):
    string_data = parsed_listing_url.find_all(class_='row_info')[1].text.strip()
    road_tax_per_year = road_tax_error_handler(string_data)
    return road_tax_per_year


def road_tax_error_handler(string_data):
    if string_data == 'NA':
        return None  # Return None for "NA" values

    try:
        # Remove '$' character and split string_data into a list
        parts = string_data.replace('/yr', '').strip().split('$')

        if len(parts) == 2:
            # Handle values like ['', 1,000] or ['', 900]
            road_tax_per_year = int(''.join(parts[1].split(',')))
        else:
            # Handle values like ['1,000/yr']
            road_tax_per_year = int(''.join(parts[0].split(',')))

        return road_tax_per_year

    except (ValueError, IndexError):
        return None  # Return None for errors and unexpected formats

