import csv
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
import customtkinter
import os
from PIL import Image,ImageTk
class Car:
    def __init__(self, Listing_ID, Listing_URL, Brand, Price, Depreciation, Road_Tax, Registration_Date, COE_Left, Mileage, Manufacture_Year,
                 Transmission,Deregistration, OMV, ARF, COE_Price, Engine_Capacity, Power, Curb_Weight, No_Of_Owners, Vehicle_Type):
        self.listingid = Listing_ID
        self.listingurl = Listing_URL
        self.brand = Brand
        self.price = float(Price)
        self.depreciation = float(Depreciation)
        self.road_tax = float(Road_Tax)
        self.registration_date = datetime.strptime(Registration_Date, '%d-%b-%y').date()
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
            #print("Row:", row)
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
#cars = read_cars_from_csv('Book1.csv')







'''ALGORITHM'''
#def calculate_score(car, budget_weight, mileage_weight, manufactured_year_weight,num_owners_weight, engine_capacity_weight, power_weight, curb_weight_weight):
def calculate_score(car, max_budget, max_mileage, max_num_owners, max_year_difference,
                    max_engine_capacity, max_power, max_curb_weight,
                    budget_weight, mileage_weight, manufactured_year_weight,
                    num_owners_weight, engine_capacity_weight, power_weight, curb_weight_weight):

    current_year = 2023
    # Score each criterion for the car
    '''NEGATIVE SCORES'''
    # (1-(car.price/max_budget))*0.15
    #budget_score = max( 0, min(1, 1 - (car.price / max_budget)) * budget_weight )
    budget_score = (1 - (car.price / max_budget)) * budget_weight

    # (1-(car.mileage/max_mileage)*0.15
    #mileage_score = max(0, min(1, 1 - (car.mileage / max_mileage)) * mileage_weight)
    mileage_score = (1 - (car.mileage / max_mileage)) * mileage_weight

    # 1 - (car.num_owners/max_num_owners)*0.1
    #num_owners_score = max(0, min(1, 1 - (car.num_owners / max_num_owners))) * num_owners_weight
    num_owners_score = 1-(car.num_owners/max_num_owners)+num_owners_weight

    '''POSITIVE WEIGHTS'''
    # 1 - (2023-car.manufactured_year)/max_year_difference * 0.15
    #manufactured_year_score = max(0, min(1, 1 - (current_year - car.manufactured_year) / max_year_difference)) * manufactured_year_weight
    manufactured_year_score = 1 - (current_year-car.manufactured_year)/max_year_difference*manufactured_year_weight

    # (car.engine_capacity/max_engine_capacity)*0.1
    #engine_capacity_score = max(0, min(1, car.engine_capacity / max_engine_capacity)) * engine_capacity_weight
    engine_capacity_score = (car.engine_capacity / max_engine_capacity) * engine_capacity_weight

    # (car.power/max_power)*0.1
    #power_score = max(0, min(1, car.power / max_power)) * power_weight
    power_score = (car.power / max_power) * power_weight

    # (car.curb_weight/max_curb_weight)*0.1
    curb_weight_score = max(0, min(1, car.curb_weight / max_curb_weight)) * curb_weight_weight
    curb_weight_score = (car.curb_weight / max_curb_weight) * curb_weight_weight


    # Calculate the overall score for the car
    overall_score = (budget_score + mileage_score + manufactured_year_score + num_owners_score + engine_capacity_score + power_score + curb_weight_score)
    return overall_score



def recommend_cars(cars, max_budget, max_mileage, max_year_difference, max_num_owners,
                    max_engine_capacity, max_power, max_curb_weight):
    recommendations = []

    for car in cars:
        score = calculate_score(car,max_budget, max_mileage, max_year_difference, max_num_owners,
                                max_engine_capacity, max_power, max_curb_weight, #added smt here
                                budget_weight=0.15,
                                mileage_weight=0.15,
                                manufactured_year_weight=0.15,
                                num_owners_weight=0.1,
                                engine_capacity_weight=0.1,
                                power_weight=0.15,
                                curb_weight_weight=0.1)
        recommendations.append((car.brand, car.listingid,car.listingurl, score))

    # Sort cars based on their scores in descending order
    recommendations.sort(key=lambda x: x[3], reverse=True)

    return recommendations[:10]

'''
# Buyer's preferences
max_budget = 25000
max_mileage = 40000
max_year_difference = 5
max_num_owners = 2
max_engine_capacity = 2000
max_power = 180
max_curb_weight = 1500
current_year = 2023

# Recommend cars based on buyer's preferences
recommendations = recommend_cars(cars, max_budget, max_mileage, max_year_difference, max_num_owners, max_engine_capacity, max_power, max_curb_weight)

print("Recommended Cars:")
for i, recommendation in enumerate(recommendations):
    print(f"{i+1}. {recommendation[0]} {recommendation[1]} {recommendation[2]} (Score: {recommendation[3]:.2f})")
# display hyperlink for LISTING URL
'''






def display_recommendations():
    global recommendations
    # Get user preferences from GUI inputs
    max_budget = float(max_budget_entry.get())
    max_mileage = float(max_mileage_entry.get())
    max_year_difference = float(max_year_difference_entry.get())
    max_num_owners = float(max_num_owners_entry.get())
    max_engine_capacity = float(max_engine_capacity_entry.get())
    max_power = float(max_power_entry.get())
    max_curb_weight = float(max_curb_weight_entry.get())

    # Recommend cars based on buyer's preferences
    recommendations = recommend_cars(cars, max_budget, max_mileage, max_year_difference, max_num_owners,
                                    max_engine_capacity, max_power, max_curb_weight)

    # Display recommendations in the GUI
    display_results(recommendations)

def display_results(recommendations):
    # Display recommendations in the results_text widget
    results_text.delete("1.0", tk.END)
    for i, recommendation in enumerate(recommendations):
        results_text.insert(tk.END, f"{i+1}. {recommendation[0]} {recommendation[1]} {recommendation[2]} (Score: {recommendation[3]:.2f})\n")

def save_to_csv(recommendations):
    # Save recommendations to a CSV file
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if file_path:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Brand", "Listing ID", "Listing URL", "Score"])
            for recommendation in recommendations:
                writer.writerow([recommendation[0], recommendation[1], recommendation[2], recommendation[3]])

# GUI display
root = customtkinter.CTk()
#root = tk.Tk()
root.title("Car Recommendation System")
customtkinter.set_default_color_theme("blue")
file_path=os.path.dirname(os.path.realpath(__file__))
image1=customtkinter.CTkImage(Image.open(file_path+"/rThumbsUp.png"),size=(32,32))


# user inputs
customtkinter.CTkLabel(root, text="Buyer Preferences",width=120,font=("Roboto-Bold",int(24.8)),height=25,).pack(pady=10)
#tk.Label(root, text="Buyer Preferences").pack(pady=10)

customtkinter.CTkLabel(root, font=("Arial-BoldMT",int(15)), text="Max Budget:").pack()
max_budget_entry = tk.Entry(root)
max_budget_entry.pack()

tk.Label(root, text="Max Mileage:").pack()
max_mileage_entry = tk.Entry(root)
max_mileage_entry.pack()

tk.Label(root, text="Max Year Difference:").pack()
max_year_difference_entry = tk.Entry(root)
max_year_difference_entry.pack()

tk.Label(root, text="Max Number of Owners:").pack()
max_num_owners_entry = tk.Entry(root)
max_num_owners_entry.pack()

tk.Label(root, text="Max Engine Capacity:").pack()
max_engine_capacity_entry = tk.Entry(root)
max_engine_capacity_entry.pack()

tk.Label(root, text="Max Power:").pack()
max_power_entry = tk.Entry(root)
max_power_entry.pack()

tk.Label(root, text="Max Curb Weight:").pack()
max_curb_weight_entry = tk.Entry(root)
max_curb_weight_entry.pack()





# Btn to show top 10 recommendations
recommend_button = customtkinter.CTkButton(root, text="Recommend Me!", image=image1, compound="right", command=display_recommendations)
#recommend_button = tk.Button(root, text="Recommend", command=display_recommendations)
recommend_button.pack(pady=10)
# Text widget to display recommendations
results_text = tk.Text(root, width=80, height=15, state="normal")
results_text.pack(pady=10)
# Btn to save recommendations to a CSV file
save_button = customtkinter.CTkButton(root, text="Download", command=lambda: save_to_csv(recommendations))
#save_button = tk.Button(root, text="Save to CSV", command=lambda: save_to_csv(recommendations))
save_button.pack(pady=10)

root.mainloop()















