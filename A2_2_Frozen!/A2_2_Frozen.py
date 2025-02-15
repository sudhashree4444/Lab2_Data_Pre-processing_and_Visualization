#This python script shows visualize the indoor and outdoor temperature over 5 months.
#These modifications on the dataframe made from the csv dataset.
#Change the "In" and "Out" text of the "Out\In" column to 1 and 0 respectively.
#Separate the date and time in the "noted_date" column, into two separate columns.
#Keep only the data of the last day 08-12-2018, and remove the rest of the rows with the appropriate function
#Author: TEJA SUDHASHREE DEVAGUPTAPU
#Date: 13-02-2025
# A2.2: Frozen!

import matplotlib.pyplot as plt
import pandas as pd

#read from csv file and its location
df = pd.read_csv('C:/Users/sudha/Documents/IOT-temp.csv')
df['noted_date'] = pd.to_datetime(df['noted_date'], format='%d-%m-%Y %H:%M')
start_date = pd.to_datetime('02-12-2018 00:00', format='%d-%m-%Y %H:%M')
end_date = pd.to_datetime('08-12-2018 23:59', format='%d-%m-%Y %H:%M')
df_last_week = df[(df['noted_date'] >= start_date) & (df['noted_date'] <= end_date)]

# using two variables to filter in and outdoor temperatures from last week dates
indoor_temps = df_last_week[df_last_week['out_in'] == 'In']
outdoor_temps = df_last_week[df_last_week['out_in'] == 'Out']


plt.plot(indoor_temps['noted_date'], indoor_temps['temp'],label='Indoor Temperature', color='blue')
plt.plot(outdoor_temps['noted_date'], outdoor_temps['temp'],label='Outdoor Temperature', color='orange')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45, ha='right')#rotating xlables so they do not overlap on each other
plt.show()


# Change the "In" and "Out" text to 1 and 0 respectively
df['out_in'] = df['out_in'].map({'In': 1, 'Out': 0})

# Separate the date and time in the "noted_date" column into two separate columns
df['date'] = df['noted_date'].dt.date
df['time'] = df['noted_date'].dt.time

# Keep only the data of the last day 08-12-2018
df_last_day = df[df['date'] == pd.to_datetime('08-12-2018', format='%d-%m-%Y').date()]

# Drop the original 'noted_date' column
df_last_day = df_last_day.drop(columns=['noted_date'])

# Save the modified dataframe to a new CSV file
df_last_day.to_csv('C:/Users/sudha/Documents/modified_temp_log.csv', index=False)

print("The modified csv can be found here 'C:/Users/sudha/Documents/modified_temp_log.csv'.")