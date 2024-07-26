import numpy as np
import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(r"D:\FODS\Day-2\house_data.csv")

# Convert the DataFrame to a NumPy array
house_data = df.to_numpy()

# Filter rows where the number of bedrooms is greater than four
filtered_data = house_data[house_data[:, 0] > 4]

# Extract the sale prices from the filtered data
sale_prices = filtered_data[:, 2]

# Calculate the average sale price
average_sale_price = np.mean(sale_prices)

# Print the result
print("Average Sale Price of Houses with More Than Four Bedrooms:", average_sale_price)
