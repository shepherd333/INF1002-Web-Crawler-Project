def brand_retrieval(url):
    if not url:
        raise ValueError("Failed to retrieve data")

    # Locate the <a> element with the specified class
    brand = url.find('a', class_='nounderline globaltitle')
    if brand:
        brand = brand.text.split()[0]
        return brand
    else:
        raise ValueError("Brand N.A")
