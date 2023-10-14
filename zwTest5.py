import csv
from datetime import datetime

class Car:
    def __init__(self, Listing_ID, Listing_URL, Brand, Price, Depreciation, Road_Tax, Registration_Date, COE_Left, Mileage, Manufacture_Year,
                 Transmission,Deregistration, OMV, ARF, COE_Price, Engine_Capacity, Power, Curb_Weight, No_Of_Owners, Vehicle_Type):
        self.listingid = Listing_ID
        self.listingurl = Listing_URL
        self.brand = Brand
        self.price = float(Price)
        self.depreciation = float(Depreciation)
        self.road_tax = float(Road_Tax)
        self.registration_date = datetime.strptime(Registration_Date, '%d-%b-%Y').date()
        self.coe_left = float(COE_Left)
        self.mileage = float(Mileage)
        self.manufactured_year = int(Manufacture_Year)
        self.transmission = Transmission
        self.deregistration = Deregistration
        self.omv = float(OMV)
        self.arf = float(ARF)
        self.coe_price = float(COE_Price)
        self.engine_capacity = float(Engine_Capacity)
        self.power = float(Power)
        self.curb_weight = float(Curb_Weight)
        self.num_owners = int(No_Of_Owners)
        self.vehicle_type = Vehicle_Type

def read_cars_from_csv(file_path):
    cars = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            car = Car(row['Listing ID'],
                      row['Listing URL'],
                      row['Brand'],
                      row['Price'],
                      row['Depreciation'],
                      row['Road Tax'],
                      row['Registration Date'],
                      row['COE Left'],
                      row['Mileage'],
                      row['Manufacture Year'],
                      row['Transmission'],
                      row['Deregistration'],
                      row['OMV'],
                      row['ARF'],
                      row['COE Price'],
                      row['Engine Capacity'],
                      row['Power'],
                      row['Curb Weight'],
                      row['No. Of Owners'],
                      row['Vehicle Type'])
            cars.append(car)
        return cars

# Load cars data from CSV
cars = read_cars_from_csv('ProcessedData_.csv')








'''ALGORITHM'''
def calculate_score(car, budget_weight, mileage_weight, manufactured_year_weight, registration_date_weight,
                    num_owners_weight, engine_capacity_weight, power_weight, curb_weight_weight):
    # Score each criterion for the car

    # (1 - dataValue / userInputValue) * weight
    '''NEGATIVE SCORES'''  # = ( 1-(dataValue/userInput) ) * weight
    '''POSITIVE WEIGHTS''' # = ( dataValue/userInput) * weight
    #

    budget_score = max(0, min(1, 1 - car.price / max_budget)) * budget_weight
    mileage_score = max(0, min(1, 1 - car.mileage / max_mileage)) * mileage_weight
    manufactured_year_score = max(0, min(1, (current_year - car.manufactured_year) / max_year_difference)) * manufactured_year_weight
    registration_date_score = max(0, min(1, (current_year - car.registration_date.year) / max_year_difference)) * registration_date_weight
    num_owners_score = max(0, min(1, 1 - car.num_owners / max_num_owners)) * num_owners_weight
    engine_capacity_score = max(0, min(1, car.engine_capacity / max_engine_capacity)) * engine_capacity_weight
    power_score = max(0, min(1, car.power / max_power)) * power_weight
    curb_weight_score = max(0, min(1, car.curb_weight / max_curb_weight)) * curb_weight_weight

    # Calculate the overall score for the car
    overall_score = (budget_score + mileage_score + manufactured_year_score + registration_date_score +
                     num_owners_score + engine_capacity_score + power_score + curb_weight_score)
    return overall_score

def recommend_cars(cars, max_budget, max_mileage, max_year_difference, max_num_owners,
                    max_engine_capacity, max_power, max_curb_weight):
    recommendations = []

    for car in cars:
        score = calculate_score(car,
                                budget_weight=0.15,
                                mileage_weight=0.15,
                                manufactured_year_weight=0.15,
                                registration_date_weight=0.1,
                                num_owners_weight=0.1,
                                engine_capacity_weight=0.1,
                                power_weight=0.15,
                                curb_weight_weight=0.1)
        recommendations.append((car.brand, car.listingid,car.listingurl, score))

    # Sort cars based on their scores in descending order
    recommendations.sort(key=lambda x: x[3], reverse=True)

    return recommendations[:10]

'''TEST HERE'''
# Buyer's preferences
max_budget = 52000
max_mileage = 95000
max_year_difference = 5
max_num_owners = 2
max_engine_capacity = 1600
max_power = 95
max_curb_weight = 1400
current_year = 2023

# Recommend cars based on buyer's preferences
recommendations = recommend_cars(cars, max_budget, max_mileage, max_year_difference,
                                 max_num_owners, max_engine_capacity, max_power, max_curb_weight)
print("Recommended Cars:")
for i, recommendation in enumerate(recommendations):
    print(f"{i+1}. {recommendation[0]} {recommendation[1]} {recommendation[2]} (Score: {recommendation[3]:.2f})")
# display hyperlink for LISTING URL