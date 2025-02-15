#This python script shows the 1.Based on the instruction on the distribution transformation, transform the "calories" column to take the shape of a distribution close to normal distribution.
#2.Making a copy of each participent and visualize the "age", "height", and "weight" of the participants.
#3.Visualizing "steps", "heart_rate", and "calories" of the first three participants in three plots.
#4.Normalize the "age", "height", and "weight", and Standardize "steps" and "heart rate" columns in a separate column.
#5.Split the dataset into three categories with the following distribution: Train (70%), Validation (15%), and Test (15%).
#Author: TEJA SUDHASHREE DEVAGUPTAPU
#Date: 14-02-2025
# A2.3:Digital Health IOT Dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

# Read the dataset from CSV
df = pd.read_csv('C:/Users/sudha/Documents/Apple_and_Fitbit_data/aw_fb_data.csv')

#1.Transform the "calories" column to take the shape of a distribution close to normal distribution

transforms = df.copy()

# Apply log transformations to the "calories" column
transforms['calories_log'] = np.log1p(transforms['calories'])

# Plot the histograms for log transforms
transforms['calories_log'].hist(bins=30, edgecolor='k', alpha=0.7)
plt.title('Log Transformation')
plt.xlabel('Log Calories')
plt.ylabel('Frequency')
plt.show()

# 2. Make a copy of the original dataframe and keep one sample from each participant in a csv
df_copy = df.copy()
df_unique = df_copy.drop_duplicates(subset=['age','height','weight'], keep='first')
df_unique.to_csv('unique_participants.csv', index=False)

# 3,Visualize "steps", "heart_rate", and "calories" of the first three participants in three plots with subplots
first_three_participants = df_unique.head(3)
# Filter the data for the first three participants
filtered_data = df[df[['age', 'height', 'weight']].apply(tuple, axis=1).isin(first_three_participants[['age', 'height', 'weight']].apply(tuple, axis=1))]

# Plotting
fig, axs = plt.subplots(3, 1, figsize=(10, 15), sharex=True)

# Plot steps
for i, participant in first_three_participants.iterrows():
    participant_data = filtered_data[(filtered_data['age'] == participant['age']) &
                                     (filtered_data['height'] == participant['height']) &
                                     (filtered_data['weight'] == participant['weight'])]
    axs[0].plot(participant_data.index, participant_data['steps'], label=f'Participant {i+1}')
axs[0].set_title('Steps')
axs[0].legend(loc='upper right')

# Plot heart_rate
for i, participant in first_three_participants.iterrows():
    participant_data = filtered_data[(filtered_data['age'] == participant['age']) &
                                     (filtered_data['height'] == participant['height']) &
                                     (filtered_data['weight'] == participant['weight'])]
    axs[1].plot(participant_data.index, participant_data['hear_rate'], label=f'Participant {i+1}')
axs[1].set_title('Heart Rate')
axs[1].legend(loc='upper right')

# Plot calories
for i, participant in first_three_participants.iterrows():
    participant_data = filtered_data[(filtered_data['age'] == participant['age']) &
                                     (filtered_data['height'] == participant['height']) &
                                     (filtered_data['weight'] == participant['weight'])]
    axs[2].plot(participant_data.index, participant_data['calories'], label=f'Participant {i+1}')
axs[2].set_title('Calories')
axs[2].legend(loc='upper right')

plt.xlabel('Index')
plt.show()

# 4. Normalize the "age", "height", and "weight", and Standardize "steps" and "heart rate" columns
scaler = MinMaxScaler()
df[['normalized_age', 'normalized_height', 'normalized_weight']] = scaler.fit_transform(df[['age', 'height', 'weight']])

standardizer = StandardScaler()
df[['standardized_steps', 'standardized_heart_rate']] = standardizer.fit_transform(df[['steps', 'hear_rate']])
df.to_csv('Normalize_standardize_csv_file.csv', index=False)

#5.Split the dataset into three categories: Train (70%), Validation (15%), and Test (15%)
X_train, X_test = train_test_split(df, test_size=0.3, random_state=42)#create 70% train data and 30% tesT data
x_test, y_test = train_test_split(X_test, test_size=0.5, random_state=42)#split 30% test data into two equal sets one validation and one for test

print(f"Train set: {len(X_train)} rows")
print(f"Validation set: {len(y_test)} rows")
print(f"Test set: {len(x_test)} rows")