import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
# skiprows=2 skips the extra header lines in the CSV file
data = pd.read_csv("NVIDIA_STOCK.csv", skiprows=2)

# Rename columns to make them clean and easier to use
data.columns = ["Date", "Adj Close", "Close", "High", "Low", "Open", "Volume"]

# Show the first 5 rows to make sure the dataset loaded correctly
print("First 5 rows:")
print(data.head())

# Show the column names
print("\nColumns:")
print(data.columns)

# Convert Date column to datetime format so I can work with dates correctly
data["Date"] = pd.to_datetime(data["Date"])

# Convert Close column to numeric values
# errors="coerce" changes invalid values into NaN
data["Close"] = pd.to_numeric(data["Close"], errors="coerce")

# Convert Volume column to numeric values
data["Volume"] = pd.to_numeric(data["Volume"], errors="coerce")

# Remove rows with missing values
data = data.dropna()

print("\nData cleaned successfully!")

# --------------------------------------------------
# QUESTION 1:
# What is the highest closing price of NVIDIA stock?
# Importance:
# This question helps me find the maximum value the stock reached
# at the end of a trading day, which shows the stock's peak performance.
# --------------------------------------------------

# Sort the data by Close price from highest to lowest
sorted_data = data.sort_values(by="Close", ascending=False)

# Get the first row, which contains the highest closing price
highest_close = sorted_data.iloc[0]

print("\n--- Question 1 ---")
print("Highest closing price:")
print(round(highest_close["Close"], 4))
print("Date:", highest_close["Date"])

# --------------------------------------------------
# QUESTION 2:
# What is the average closing price of NVIDIA stock?
# Importance:
# This question helps me understand the general value of the stock
# over time instead of looking at only one specific day.
# --------------------------------------------------

# Calculate the average closing price
average_close = data["Close"].mean()

print("\n--- Question 2 ---")
print("Average closing price:")
print(round(average_close, 3))

# --------------------------------------------------
# QUESTION 3:
# On which day was the trading volume the highest?
# Importance:
# This question shows the day with the most market activity.
# A high volume can mean strong investor interest in the stock.
# --------------------------------------------------

# Sort the data by Volume from highest to lowest
volume_sorted = data.sort_values(by="Volume", ascending=False)

# Get the first row, which contains the highest trading volume
highest_volume_day = volume_sorted.iloc[0]

print("\n--- Question 3 ---")
print("Highest trading volume:")
print(highest_volume_day["Volume"])
print("Date:", highest_volume_day["Date"])

# --------------------------------------------------
# STRETCH CHALLENGE:
# Create a graph of closing price over time
# This helps visualize trends and changes in NVIDIA's stock price.
# --------------------------------------------------

# Sort the data by date so the graph shows the timeline correctly
data = data.sort_values(by="Date")

# Create the graph
plt.figure(figsize=(12, 6))
plt.plot(data["Date"], data["Close"])

# Add title and axis labels
plt.title("NVIDIA Closing Price Over Time")
plt.xlabel("Date")
plt.ylabel("Closing Price")

# Make the graph layout cleaner
plt.tight_layout()

# Show the graph
plt.show()