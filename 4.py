import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Define the start and end dates
start_date = '2023-01-01'
end_date = '2024-01-01'

# Fetch historical stock price data for Alphabet Inc. (ticker symbol: GOOGL) from Yahoo Finance
stock_data = web.DataReader('GOOGL', data_source='yahoo', start=start_date, end=end_date)

# Create a line plot of the historical stock prices
plt.figure(figsize=(10, 6))
plt.plot(stock_data.index, stock_data['Close'], color='blue', linestyle='-', linewidth=1.5)
plt.title('Historical Stock Prices of Alphabet Inc. (GOOGL)')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.grid(True)
plt.show()
