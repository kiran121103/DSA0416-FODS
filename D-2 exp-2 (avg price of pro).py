import numpy as np

# Assuming the sales_data array is as follows:
# Each row represents a different product, and each column represents a different sale.
sales_data = np.array([
    [100, 150, 200],
    [120, 180, 240],
    [130, 170, 210]
])

# Calculate the average price of all products sold
average_price = np.mean(sales_data)

print("Average price of all products sold:", average_price)
