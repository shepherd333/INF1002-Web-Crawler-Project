import csv
import time
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter
import os

import requests
from PIL import Image,ImageTk
from customtkinter import CTkFrame, CTkEntry
import pyshorteners

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
    # Check if there are any recommendations
    #if not recommendations:
        #messagebox.showerror("No Recommendations", "No recommendations to display.")
        #return

    # Get user preferences from GUI inputs
    try:
        max_budget = float(max_budget_entry.get())
        max_mileage = float(max_mileage_entry.get())
        max_year_difference = float(max_year_difference_entry.get())
        max_num_owners = float(max_num_owners_entry.get())
        max_engine_capacity = float(max_engine_capacity_entry.get())
        max_power = float(max_power_entry.get())
        max_curb_weight = float(max_curb_weight_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numerical values for preferences.")
        return

    # Check for negative values
    if any(value < 0 for value in [max_budget, max_mileage, max_year_difference,
                                   max_num_owners, max_engine_capacity,
                                   max_power, max_curb_weight]):
        results_text.delete("1.0", tk.END)
        results_text.insert(tk.END, "Please enter non-negative values for preferences.")
        return

    # Recommend cars based on buyer's preferences
    recommendations = recommend_cars(cars, max_budget, max_mileage, max_year_difference, max_num_owners,
                                    max_engine_capacity, max_power, max_curb_weight)

    # Display recommendations in the GUI
    display_results(recommendations)


# Function to shorten a URL using TinyURL
def shorten_url_tiny(url):
    try:
        s = pyshorteners.Shortener()
        return s.tinyurl.short(url)
    except requests.exceptions.ReadTimeout:
        print("Error: Read timeout while shortening the URL. Please try again later.")
        return url  # Return the original URL if shortening fails
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while shortening the URL: {e}")
        return url  # Return the original URL if shortening fails

def display_results(recommendations):
    # Display recommendations in the results_text widget
    results_text.delete("1.0", tk.END)
    for i, recommendation in enumerate(recommendations):
        shortened_url = shorten_url_tiny(recommendation[2])
        results_text.insert(tk.END,
                            f"{i + 1}. {recommendation[0]} {recommendation[1]} {shortened_url} (Score: {recommendation[3]:.2f})\n")


def save_to_csv(recommendations):
    # Save recommendations to a CSV file
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if file_path:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Brand", "Listing ID", "Listing URL", "Shortened URL", "Score"])
            for recommendation in recommendations:
                shortened_url = shorten_url_tiny(recommendation[2])
                writer.writerow(
                    [recommendation[0], recommendation[1], recommendation[2], shortened_url, recommendation[3]])

        '''
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Brand", "Listing ID", "Listing URL", "Score"])
            for recommendation in recommendations:
                writer.writerow([recommendation[0], recommendation[1], recommendation[2], recommendation[3]])
'''

# GUI display
root = tk.Tk()
root.title("Car Recommendation System")

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

file_path=os.path.dirname(os.path.realpath(__file__))
image1=customtkinter.CTkImage(Image.open(file_path+"/rThumbsUp.png"),size=(28,28))
image2=customtkinter.CTkImage(Image.open(file_path+"/rDownload.png"),size=(28,28))

# user inputs
frame = CTkFrame(root)
frame.pack(expand=True)

buyer_preferences_label = customtkinter.CTkLabel(frame, text="Buyer Preferences", width=120, font=("Arial-BoldMT", 24.8), height=25)
buyer_preferences_label.grid(row=0, column=0, columnspan=2, pady=(10,5), sticky="ew")

customtkinter.CTkLabel(frame, font=("Arial-BoldMT",15), text="Max Budget($): ").grid(row=1, column=0, padx=(15, 0), pady=10)
max_budget_entry = CTkEntry(frame)
max_budget_entry.grid(row=1,column=1,padx=(15, 0), pady=10)

customtkinter.CTkLabel(frame, font=("Arial-BoldMT", 15), text="Max Mileage(km):").grid(row=2, column=0, padx=(15, 0), pady=10)
max_mileage_entry = customtkinter.CTkEntry(frame)
max_mileage_entry.grid(row=2, column=1, padx=(15, 0), pady=10)

customtkinter.CTkLabel(frame, font=("Arial-BoldMT",int(15)), text="Max Year(s) Difference:").grid(row=3, column=0, padx=(15, 0), pady=10)
max_year_difference_entry = customtkinter.CTkEntry(frame)
max_year_difference_entry.grid(row=3, column=1, padx=(15, 0), pady=10)

customtkinter.CTkLabel(frame, font=("Arial-BoldMT",int(15)), text="Max Number of Owners:").grid(row=4, column=0, padx=(15, 0), pady=10)
max_num_owners_entry = customtkinter.CTkEntry(frame)
max_num_owners_entry.grid(row=4, column=1, padx=(15, 0), pady=10)

customtkinter.CTkLabel(frame, font=("Arial-BoldMT",int(15)), text="Max Engine Capacity(cc): ").grid(row=5, column=0, padx=(15, 0), pady=10)
max_engine_capacity_entry = customtkinter.CTkEntry(frame)
max_engine_capacity_entry.grid(row=5, column=1, padx=(15, 0), pady=10)

customtkinter.CTkLabel(frame, font=("Arial-BoldMT",int(15)), text="Max Power(kW):").grid(row=6, column=0, padx=(15, 0), pady=10)
max_power_entry = customtkinter.CTkEntry(frame)
max_power_entry.grid(row=6, column=1, padx=(15, 0), pady=10)

customtkinter.CTkLabel(frame, font=("Arial-BoldMT",int(15)), text="Max Curb Weight(kg) :").grid(row=7, column=0, padx=(15, 0), pady=10)
max_curb_weight_entry = customtkinter.CTkEntry(frame)
max_curb_weight_entry.grid(row=7, column=1, padx=(15, 0), pady=10)


# Btn to show top 10 recommendations
recommend_button = customtkinter.CTkButton(frame, text="Recommend!", image=image1, compound="right", command=display_recommendations)
recommend_button.grid(row=8, column=0, columnspan=2, pady=10)

results_text = tk.Text(frame, width=80, height=15, state="normal")
results_text.grid(row=9, column=0, columnspan=2, pady=10)

save_button = customtkinter.CTkButton(frame, text="Download", image=image2, compound="right", command=lambda: save_to_csv(recommendations))
save_button.grid(row=10, column=0, columnspan=2, pady=10)

''''''
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

root.update_idletasks()  # Update the idle tasks to calculate the frame size
frame_width = frame.winfo_reqwidth()
frame_height = frame.winfo_reqheight()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - frame_width) // 2
y_coordinate = (screen_height - frame_height) // 2
root.geometry(f"{frame_width}x{frame_height}+{x_coordinate}+{y_coordinate}")

root.mainloop()