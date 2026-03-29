import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
# skiprows=2 skips the extra header lines
data = pd.read_csv("NVIDIA_STOCK.csv", skiprows=2)

# Rename columns to make them clean and simple
data.columns = ["Date", "Adj Close", "Close", "High", "Low", "Open", "Volume"]

# Show first rows to check everything is correct
print("First 5 rows:")
print(data.head())

# Show column names
print("\nColumns:")
print(data.columns)

# Convert Date column to datetime format
data["Date"] = pd.to_datetime(data["Date"])

# Make sure Close column is numeric
data["Close"] = pd.to_numeric(data["Close"], errors="coerce")

# Remove rows with missing values (if any)
data = data.dropna()

print("\nData cleaned successfully!")

sorted_data = data.sort_values(by="Close", ascending=False)

# Get the highest closing price (first row)
highest_close = sorted_data.iloc[0]

print("\n--- Question 1 ---")
print("Highest closing price:")
print(highest_close["Close"])
print("Date:", highest_close["Date"])

average_close = data["Close"].mean()

print("\n--- Question 2 ---")
print("Average closing price:")
print(average_close)

# QUESTION 3: Day with highest trading volume

# Make sure Volume is numeric
data["Volume"] = pd.to_numeric(data["Volume"], errors="coerce")

# Sort by Volume (descending)
volume_sorted = data.sort_values(by="Volume", ascending=False)

# Get the row with highest volume
highest_volume_day = volume_sorted.iloc[0]

print("\n--- Question 3 ---")
print("Highest trading volume:")
print(highest_volume_day["Volume"])
print("Date:", highest_volume_day["Date"])

# STRETCH CHALLENGE: Graph of closing price over time

# Sort by date so the graph goes in the correct order
data = data.sort_values(by="Date")

# Create the graph
plt.figure(figsize=(12, 6))
plt.plot(data["Date"], data["Close"])

# Add title and labels
plt.title("NVIDIA Closing Price Over Time")
plt.xlabel("Date")
plt.ylabel("Closing Price")

# Make layout cleaner
plt.tight_layout()

# Show the graph
plt.show()