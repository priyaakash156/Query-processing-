import pandas as pd
data = {
    'Date': ['2024-02-01', '2024-02-01', '2024-02-02', '2024-02-02', '2024-02-03', '2024-02-03'],
    'Item': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Sales': [100, 150, 200, 250, 300, 350]
}
sales_data = pd.DataFrame(data)
pivot_table = pd.pivot_table(sales_data, values='Sales', index='Item', aggfunc=['min', 'max'])
print("Pivot Table:")
print(pivot_table)
max_sale = pivot_table[('max', 'Sales')].max()
min_sale = pivot_table[('min', 'Sales')].min()

print("\nMaximum Sale Value:", max_sale)
print("Minimum Sale Value:", min_sale)
