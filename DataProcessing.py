import pandas as pd

pd.set_option('display.max_columns', None)  # Display all columns
pd.set_option('display.max_rows', None)  # Display all rows


def process_data(data):
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
        brand_list.append(item.get('brand', 'Not Available'))
        price_list.append(item.get('price', 'Not Available'))
        depre_list.append(item.get('depre', 'Not Available'))
        roadtax_list.append(item.get('roadtax', 'Not Available'))
        reg_date_list.append(item.get('reg_date', 'Not Available'))
        coe_left_list.append(item.get('coeLeft', 'Not Available'))
        mileage_list.append(item.get('mile', 'Not Available'))
        manu_year_list.append(item.get('manuyear', 'Not Available'))
        transmission_list.append(item.get('transmission', 'Not Available'))
        deregistration_list.append(item.get('dereg', 'Not Available'))
        omv_list.append(item.get('omv', 'Not Available'))
        arf_list.append(item.get('arf', 'Not Available'))
        coe_price_list.append(item.get('coeprice', 'Not Available'))
        engine_cap_list.append(item.get('eng_cap', 'Not Available'))
        power_list.append(item.get('power', 'Not Available'))
        curb_weight_list.append(item.get('curb_weight', 'Not Available'))
        owners_list.append(item.get('no_of_owners', 'Not Available'))
        vehicle_type_list.append(item.get('veh_type', 'Not Available'))

    # Create a DataFrame from the lists
    df = pd.DataFrame({
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

def save_data_to_csv(df, filename):
    # Save the DataFrame to a CSV file
    df.to_csv(filename, index=False, encoding='utf-8')
    print(df)
