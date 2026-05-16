# 🌦️ Year-Long Hourly Weather Data Analysis (Python, Pandas, NumPy, Matplotlib)

This project simulates the work of a **city weather station analyst**.  
Using an hourly weather dataset recorded over an entire year, this script performs:

- Data inspection and cleaning
- Data filtering and slicing with Pandas & NumPy
- Statistical analysis for research questions
- Multiple visualizations using Matplotlib

The dataset contains realistic synthetic weather readings for:
- Temperature (°C)
- Humidity (%)
- Windspeed (km/h)

---

## 📁 Dataset

File used: `synthetic_hourly_weather_2024.csv`

Contains **8,760 rows** (24 hours × 365 days) with columns:

| Column | Description |
|--------|-------------|
| datetime | Timestamp of observation |
| temperature_c | Temperature in Celsius |
| humidity_percent | Humidity percentage |
| windspeed_kmh | Wind speed in km/h |

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib

---

## 🔍 Tasks Performed

### 1. Data Inspection
- `head()`, `tail()`, `info()`, `describe()`

### 2. Data Filtering & Slicing
- January data extraction
- Rows where humidity > 35%
- Selecting only temperature & humidity columns
- Rows between Feb 1 and March 30
- Extreme condition filtering (low humidity, high windspeed)

### 3. NumPy Operations
- Convert temperature column to NumPy array
- Celsius → Fahrenheit conversion
- Statistical measures: max, min, mean, std
- Random row sampling

### 4. Research Analysis
- Average temperature per month
- Month with highest average humidity
- Top 10 hottest days of the year

### 5. Data Visualization
- Line plot: temperature trend across the year
- Scatter plot: temperature vs windspeed
- Bar chart: average monthly temperature
- Histogram: humidity distribution
- Combined subplots for summary visualization

---

## ▶️ How to Run

1. Clone the repository
2. Ensure the CSV file is in the same directory as the script
3. Install dependencies:

```bash
pip install pandas numpy matplotlib
```

4. Run the script:

```bash
python weather_analysis.py
```

---

## 📊 Output

The script prints analytical results in the console and generates multiple plots to visually understand yearly weather patterns.

---

## 🎯 Purpose of Project

This project demonstrates practical usage of:

- Real-world style data analysis workflow
- Pandas for time-series data handling
- NumPy for numerical analysis
- Matplotlib for visualization
- Research-oriented interpretation of weather data

