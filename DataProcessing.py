import pandas as pd
from cleaner import clean_brand, clean_price, clean_depre, clean_roadtax, clean_coeLeft, clean_mileage, clean_manufacture_year, clean_transmission, clean_dereg, clean_omv, clean_arf, clean_coeprice, clean_enginecap, clean_power, clean_curbweight, clean_noOwners

pd.set_option('display.max_columns', None)  # Display all columns
pd.set_option('display.max_rows', None)  # Display all rows


def process_data(data, listing_url, listingid_array):
    # Create lists to store data for each column
    brand_list = []
    price_list = []
    depre_list = []
    roadtax_list = []
    reg_date_list = []
    coe_left_list = []
    mileage_list = []
    manu_year_list = []
    transmission_list = []
    deregistration_list = []
    omv_list = []
    arf_list = []
    coe_price_list = []
    engine_cap_list = []
    power_list = []
    curb_weight_list = []
    owners_list = []
    vehicle_type_list = []

    # Iterate through the data
    for item in data:
        # Append values to respective lists or use placeholder if value is missing
        brand_list.append(clean_brand(item.get('brand', 'Not Available')))
        price_list.append(clean_price(item.get('price', 'Not Available')))
        depre_list.append(clean_depre(item.get('depre', 'Not Available')))
        roadtax_list.append(clean_roadtax(item.get('roadtax', 'Not Available')))
        reg_date_list.append(item.get('reg_date', 'Not Available'))
        coe_left_list.append(clean_coeLeft(item.get('coeLeft', 'Not Available')))
        mileage_list.append(clean_mileage(item.get('mile', 'Not Available')))
        manu_year_list.append(clean_manufacture_year(item.get('manuyear', 'Not Available')))
        transmission_list.append(clean_transmission(item.get('transmission', 'Not Available')))
        deregistration_list.append(clean_dereg(item.get('dereg', 'Not Available')))
        omv_list.append(clean_omv(item.get('omv', 'Not Available')))
        arf_list.append(clean_arf(item.get('arf', 'Not Available')))
        coe_price_list.append(clean_coeprice(item.get('coeprice', 'Not Available')))
        engine_cap_list.append(clean_enginecap(item.get('eng_cap', 'Not Available')))
        power_list.append(clean_power(item.get('power', 'Not Available')))
        curb_weight_list.append(clean_curbweight(item.get('curb_weight', 'Not Available')))
        owners_list.append(clean_noOwners(item.get('no_of_owners', 'Not Available')))
        vehicle_type_list.append(item.get('veh_type', 'Not Available'))

    # Create a DataFrame from the lists
    df = pd.DataFrame({
        'Listing ID': listingid_array,
        'Listing URL': listing_url,
        'Brand': brand_list,
        'Price': price_list,
        'Depreciation': depre_list,
        'Road Tax': roadtax_list,
        'Registration Date': reg_date_list,
        'COE Left': coe_left_list,
        'Mileage': mileage_list,
        'Manufacture Year': manu_year_list,
        'Transmission': transmission_list,
        'Deregistration': deregistration_list,
        'OMV': omv_list,
        'ARF': arf_list,
        'COE Price': coe_price_list,
        'Engine Capacity': engine_cap_list,
        'Power': power_list,
        'Curb Weight': curb_weight_list,
        'No. Of Owners': owners_list,
        'Vehicle Type': vehicle_type_list
    })

    return df


def remove_na_rows(df):
    try:
        # Replace 'N/A' and 'nan' with NaN
        df.replace(['N/A', 'nan'], pd.NA, inplace=True)

        # Drop rows containing NaN values
        df.dropna(inplace=True)

        return df  # Return the cleaned DataFrame
    except Exception as e:
        print(f"An error occurred during data cleaning: {str(e)}")
        return df  # Return the original DataFrame in case of an error



def save_data_to_csv(df, filename):
    # Save the DataFrame to a CSV file
    df.to_csv(filename, index=False, encoding='utf-8')
    print(df)
