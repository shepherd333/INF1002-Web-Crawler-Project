import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv
import tkinter as tk
from tkinter import simpledialog, messagebox

# data source
data = pd.read_csv(r"C:\Users\tohzh\PycharmProjects\INF1002-Web-Crawler-Project\ProcessedData.csv")

#print(data.shape)
#cor_2 = data.corr()
#print(cor_2)

#dr_2 = pd.DataFrame(cor_2)
#dr_2.to_csv('C:\\Users\\tohzh\\PycharmProjects\\INF1002-Web-Crawler-Project\\ABC.csv')

data = pd.read_csv('ProcessedData.csv')
#print(data['Vehicle Type'].unique())
print(data["Price"].mean())
print(data["Price"].median())
print(data["Price"].describe())




