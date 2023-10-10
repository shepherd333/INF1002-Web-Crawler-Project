def clean_brand(brand):
    try:
        # Check if the brand is empty (blank)
        if not brand.strip():
            return 'N/A'
        else:
            # Convert the brand to a string to ensure consistency
            return str(brand)
    except (ValueError, TypeError):
        return 'N/A'

def clean_price(price):
    try:
        # Check if the price is None or not an integer
        if price is None or not isinstance(price, int):
            return 'N/A'
        else:
            return str(price)
    except (ValueError, TypeError):
        return 'N/A'


def clean_depre(depre):
    try:
        # Check if the depre can be converted to an integer
        depreciation = int(depre)
        return str(depreciation)  # Convert it to a string to maintain consistency
    except (ValueError, TypeError):
        return 'N/A'



def clean_roadtax(roadtax):
    try:
        # Check if the manu_year can be converted to an integer
        year = int(roadtax)
        return str(year)  # Convert it to a string to maintain consistency
    except (ValueError, TypeError):
        return 'N/A'


def clean_coeLeft(coeLeft):
    try:
        # Check if the coeLeft can be converted to an integer
        coe_left = int(coeLeft)
        return str(coe_left)  # Convert it to a string to maintain consistency
    except (ValueError, TypeError):
        return 'N/A'



def clean_mileage(mile):
    try:
        # Check if mile is None or not an integer
        if mile is None or not isinstance(mile, int):
            return 'N/A'
        else:
            # Convert mile to a string to ensure consistency
            return str(mile)
    except (ValueError, TypeError):
        return 'N/A'


def clean_manufacture_year(manu_year):
    try:
        # Check if the manu_year can be converted to an integer
        year = int(manu_year)
        return str(year)  # Convert it to a string to maintain consistency
    except (ValueError, TypeError):
        return 'N/A'


def clean_transmission(transmission):
    if transmission is None:
        return 'N/A'
    elif transmission in ['Auto', 'Manual']:
        return str(transmission)
    else:
        return 'N/A'


def clean_dereg(dereg):
    try:
        # Check if mile is None or not an integer
        if dereg is None or not isinstance(dereg, int):
            return 'N/A'
        else:
            # Convert mile to a string to ensure consistency
            return str(dereg)
    except (ValueError, TypeError):
        return 'N/A'


def clean_omv(omv):
    try:
        # Check if mile is None or not an integer
        if omv is None or not isinstance(omv, int):
            return 'N/A'
        else:
            # Convert mile to a string to ensure consistency
            return str(omv)
    except (ValueError, TypeError):
        return 'N/A'


def clean_arf(arf):
    try:
        # Check if mile is None or not an integer
        if arf is None or not isinstance(arf, int):
            return 'N/A'
        else:
            # Convert mile to a string to ensure consistency
            return str(arf)
    except (ValueError, TypeError):
        return 'N/A'


def clean_coeprice(coeprice):
    try:
        # Check if mile is None or not an integer
        if coeprice is None or not isinstance(coeprice, int):
            return 'N/A'
        else:
            # Convert mile to a string to ensure consistency
            return str(coeprice)
    except (ValueError, TypeError):
        return 'N/A'


def clean_enginecap(enginecap):
    try:
        # Check if mile is None or not an integer
        if enginecap is None or not isinstance(enginecap, int):
            return 'N/A'
        else:
            # Convert mile to a string to ensure consistency
            return str(enginecap)
    except (ValueError, TypeError):
        return 'N/A'


def clean_power(power):
    try:
        # Check if power is None or not a numeric value (integer or float)
        if power is None or not (isinstance(power, int) or isinstance(power, float)):
            return 'N/A'
        else:
            # Convert power to a string to ensure consistency
            return str(power)
    except (ValueError, TypeError):
        return 'N/A'

def clean_curbweight(curbweight):
    try:
        # Check if mile is None or not an integer
        if curbweight is None or not isinstance(curbweight, int):
            return 'N/A'
        else:
            # Convert mile to a string to ensure consistency
            return str(curbweight)
    except (ValueError, TypeError):
        return 'N/A'


def clean_noOwners(no_of_owners):
    try:
        # Check if mile is None or not an integer
        if no_of_owners is None or not isinstance(no_of_owners, int):
            return 'N/A'
        else:
            # Convert mile to a string to ensure consistency
            return str(no_of_owners)
    except (ValueError, TypeError):
        return 'N/A'



