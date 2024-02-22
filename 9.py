import pandas as pd

# Sample sales data
data = {
    'Date': ['2024-02-01', '2024-02-01', '2024-02-02', '2024-02-02', '2024-02-03', '2024-02-03'],
    'Region': ['East', 'West', 'East', 'West', 'East', 'West'],
    'Manager': ['John', 'Doe', 'John', 'Doe', 'John', 'Doe'],
    'Salesman': ['Sam', 'Alice', 'Sam', 'Alice', 'Sam', 'Alice'],
    'Sales': [100, 150, 200, 250, 300, 350]
}

# Create DataFrame
sales_data = pd.DataFrame(data)

# Create Pivot table to find total sale amount region-wise, manager-wise, salesperson-wise
pivot_table = pd.pivot_table(sales_data, values='Sales', index=['Region', 'Manager', 'Salesman'], aggfunc='sum')

# Print pivot table
print("Pivot Table - Total Sale Amount:")
print(pivot_table)
