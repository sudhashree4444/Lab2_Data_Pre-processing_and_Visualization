# This Pyhton script shows the data from Ardurino rep2040(gyr/acc) in a CSV file and line graph with two axes.
#plot 6 axis of data,
#Adding labels for each axis (Acceleration (m.sq/s.sq), Time(seconds)),
#Turning on the grids,
#Adding legend on top right corner - the name of your plots should be Ax, Ay, Az, Gx, Gy, Gz.
#Author: TEJA SUDHASHREE DEVAGUPTAPU
#Date: 08-20-2025
# A.0.2: Motion logging-Gyr/Acc and collection.

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('C:/Users/sudha/Documents/accogyro.csv')

# Convert Date and Time to datetime and set as index

df['DateTime'] = df['Date'] + ' ' + df[' Time']
df.set_index('DateTime', inplace=True)
print(df.columns)

# Drop the original Date and Time columns
df.drop(columns=['Date', ' Time'], inplace=True)

# Plot the data
fig, ax = plt.subplots()

ax.plot(df.index, df[' Ax'], label=' Ax')
ax.plot(df.index, df[' Ay'], label=' Ay')
ax.plot(df.index, df[' Az'], label=' Az')
ax.plot(df.index, df[' Gx'], label=' Gx')
ax.plot(df.index, df[' Gy'], label=' Gy')
ax.plot(df.index, df[' Gz'], label=' Gz')

# Add labels and title
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Acceleration (m.sq/s.sq)')
ax.set_title('Sensor Data Over Time')

# Add grid
ax.grid(True)

# Add legend
ax.legend(loc='upper right')

# Show plot
plt.show()

