import pandas as pd

# Sample sales data
data = {
    'Date': ['2024-02-01', '2024-02-01', '2024-02-02', '2024-02-02', '2024-02-03', '2024-02-03'],
    'Item': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Sales': [100, 150, 200, 250, 300, 350]
}

# Create DataFrame
sales_data = pd.DataFrame(data)

# Create Pivot table to find unit sold item-wise
pivot_table = pd.pivot_table(sales_data, values='Sales', index='Item', aggfunc='sum')

# Print pivot table
print("Pivot Table - Unit Sold Item-wise:")
print(pivot_table)
