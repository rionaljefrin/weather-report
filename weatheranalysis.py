# ==============================
# WEATHER DATA ANALYSIS SCRIPT
# ==============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# 1. LOAD CSV INTO DATAFRAME
# ------------------------------
df = pd.read_csv("synthetic_hourly_weather_2024.csv")

# Convert datetime column to datetime type
df['datetime'] = pd.to_datetime(df['datetime'])

# ------------------------------
# 2. BASIC INSPECTION
# ------------------------------
print("\nHEAD:\n", df.head())
print("\nTAIL:\n", df.tail())
print("\nINFO:\n")
print(df.info())
print("\nDESCRIBE:\n", df.describe())

# ------------------------------
# 3. NUMPY / DATA FILTERING TASKS
# ------------------------------

# January data only
january_data = df[df['datetime'].dt.month == 1]
print("\nJanuary Data Shape:", january_data.shape)

# Rows with humidity > 35
humidity_over_35 = df[df['humidity_percent'] > 35]
print("Rows with humidity > 35:", humidity_over_35.shape)

# Columns with temperature and humidity only
temp_humidity_cols = df[['temperature_c', 'humidity_percent']]
print("\nTemp & Humidity Columns:\n", temp_humidity_cols.head())

# Slice rows between Feb 1 and March 30
slice_data = df[(df['datetime'] >= '2024-02-01') & (df['datetime'] <= '2024-03-30')]
print("\nSlice Feb 1 to March 30:", slice_data.shape)

# Filter: humidity < 20 and windspeed > 15
filtered_rows = df[(df['humidity_percent'] < 20) & (df['windspeed_kmh'] > 15)]
print("\nFiltered extreme rows:", filtered_rows.shape)

# ------------------------------
# 4. NUMPY OPERATIONS ON TEMPERATURE
# ------------------------------
temp_array_c = df['temperature_c'].to_numpy()

# Convert Celsius to Fahrenheit
temp_array_f = (temp_array_c * 9/5) + 32

print("\nTemperature Stats (Fahrenheit):")
print("Max:", np.max(temp_array_f))
print("Min:", np.min(temp_array_f))
print("Mean:", np.mean(temp_array_f))
print("Std Dev:", np.std(temp_array_f))

# Random sample of rows
random_samples = df.sample(10)
print("\nRandom Sample Rows:\n", random_samples)

# ------------------------------
# 5. RESEARCH QUESTIONS
# ------------------------------

# Add month column
df['month'] = df['datetime'].dt.month
df['date'] = df['datetime'].dt.date

# Average temperature per month
avg_temp_month = df.groupby('month')['temperature_c'].mean()
print("\nAverage Temperature Per Month:\n", avg_temp_month)

# Month with highest average humidity
avg_humidity_month = df.groupby('month')['humidity_percent'].mean()
highest_humidity_month = avg_humidity_month.idxmax()
print("\nMonth with Highest Avg Humidity:", highest_humidity_month)

# Top 10 hottest days (by daily max temp)
daily_max = df.groupby('date')['temperature_c'].max()
top_10_hottest_days = daily_max.sort_values(ascending=False).head(10)
print("\nTop 10 Hottest Days:\n", top_10_hottest_days)

# ------------------------------
# 6. MATPLOTLIB VISUALIZATIONS
# ------------------------------

# Line plot: temperature across year
plt.figure(figsize=(12,6))
plt.plot(df['datetime'], df['temperature_c'], color='red')
plt.title("Temperature Trend Across the Year")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

# Scatter plot: temperature vs windspeed
plt.figure(figsize=(8,6))
plt.scatter(df['temperature_c'], df['windspeed_kmh'], color='blue', alpha=0.5)
plt.title("Temperature vs Windspeed")
plt.xlabel("Temperature (°C)")
plt.ylabel("Windspeed (km/h)")
plt.grid(True)
plt.show()

# Bar chart: average temp each month
plt.figure(figsize=(10,6))
avg_temp_month.plot(kind='bar', color='green')
plt.title("Average Temperature Each Month")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

# Histogram: humidity
plt.figure(figsize=(8,6))
plt.hist(df['humidity_percent'], bins=30, color='purple')
plt.title("Humidity Distribution")
plt.xlabel("Humidity (%)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# ------------------------------
# 7. SUBPLOTS (ALL TOGETHER)
# ------------------------------
fig, axs = plt.subplots(3, 1, figsize=(12, 15))

# Temp trend
axs[0].plot(df['datetime'], df['temperature_c'], color='red')
axs[0].set_title("Temperature Trend")
axs[0].set_xlabel("Date")
axs[0].set_ylabel("Temp (°C)")
axs[0].grid(True)

# Humidity histogram
axs[1].hist(df['humidity_percent'], bins=30, color='orange')
axs[1].set_title("Humidity Histogram")
axs[1].set_xlabel("Humidity (%)")
axs[1].set_ylabel("Frequency")
axs[1].grid(True)

# Wind scatter
axs[2].scatter(df['temperature_c'], df['windspeed_kmh'], color='blue', alpha=0.5)
axs[2].set_title("Temp vs Wind Scatter")
axs[2].set_xlabel("Temp (°C)")
axs[2].set_ylabel("Wind (km/h)")
axs[2].grid(True)

plt.tight_layout()
plt.show()