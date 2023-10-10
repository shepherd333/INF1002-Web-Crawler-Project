def brand_retrieval(parsed_url):
    if not parsed_url:
        raise ValueError("Failed to retrieve data")

    # Locate the <a> element with the specified class
    brand = parsed_url.find('a', class_='nounderline globaltitle')
    if brand:
        brand = brand.text.split()[0]
        return brand
    else:
        raise ValueError("Brand N.A")
