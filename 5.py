import pandas as pd
import matplotlib.pyplot as plt

# Assuming 'date' is the column name for the date and 'volume' is the column name for trading volume
# Load the stock data into a Pandas DataFrame
# Replace 'path_to_csv_file' with the actual path to your CSV file containing the stock data
alphabet_stock_data = pd.read_csv('C:/Users\Nivas\Downloads\input [MConverter.eu].csv')

# Convert the date column to datetime format
alphabet_stock_data['date'] = pd.to_datetime(alphabet_stock_data['date'])

# Define the specific date range
start_date = '2023-01-01'
end_date = '2023-12-31'

# Filter the DataFrame for the specified date range
filtered_data = alphabet_stock_data[(alphabet_stock_data['date'] >= start_date) & (alphabet_stock_data['date'] <= end_date)]

# Plotting the trading volume as a bar plot
plt.figure(figsize=(10, 6))
plt.bar(filtered_data['date'], filtered_data['volume'], color='blue')
plt.title('Trading Volume of Alphabet Inc. Stock')
plt.xlabel('Date')
plt.ylabel('Trading Volume')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
