# Gathering stock data for analysis
import pandas as pd
import yfinance as yf
import os

startDate = "1993-01-29"
endDate = "2024-03-01"

ticker = ["MSFT", "AAPL", "SPY"]

df = yf.download(ticker, startDate, endDate)

download_path = os.path.join(os.path.expanduser("~"), "Downloads")

file_path = os.path.join(download_path, "stock_data.csv")

# Save the DataFrame to CSV
df.to_csv(file_path)

print("File saved to:", file_path)
