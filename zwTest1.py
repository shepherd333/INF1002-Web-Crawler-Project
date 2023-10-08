import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv
data = pd.read_csv(r"C:\Users\tohzh\PycharmProjects\INF1002-Web-Crawler-Project\UsedCars_20sep.csv")

#print(data.shape)
cor_2 = data.corr()
print(cor_2)

dr_2 = pd.DataFrame(cor_2)
#dr_2.to_csv('C:\\Users\\tohzh\\PycharmProjects\\INF1002-Web-Crawler-Project\\ABC.csv')










