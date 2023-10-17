import numpy as np


def type_of_vehicle_error_handler():
    return np.nan


def type_of_vehicle_retrieval(listing_url):
    type_of_vehicle = type_of_vehicle_error_handler()  # Initialize with a default value
    try:
        type_of_vehicle = listing_url.find(class_='row_bg1')
        if type_of_vehicle:
            links = type_of_vehicle.find_all('a')
            if links:
                type_of_vehicle = links[0].text
    except Exception as e:
        print(f"An error occurred while retrieving the vehicle type: {e}")
    return type_of_vehicle
