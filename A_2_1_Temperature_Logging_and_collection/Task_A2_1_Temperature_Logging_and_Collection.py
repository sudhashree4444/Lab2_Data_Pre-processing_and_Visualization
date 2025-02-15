#This Python script shows the recorded temperature data from Ardurino rp2040 in CSV and visualize the data in line graph.
#The color of the line should be orange
#Add labels for each axis (Temperature (degrees Celsius), Time(seconds)),
#Turn on the grids
#Adding legend on the top right corner - temperature
#Author: TEJA SUDHASHREE DEVAGUPTAPU
#Date: 08-20-2025
# A.0.1: Temperature logging and collection.


import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('C:/Users/sudha/Documents/Temprature_15.csv')

df.plot(x='Timesteps' , y='Temperature', kind='line' ,title='Temperature Logging',xlabel='Timestep(sec)',ylabel='Temperature(celsius)', grid=True, color='orange')
plt.legend(['Temperature'], loc='upper right')

plt.show() #show graph

