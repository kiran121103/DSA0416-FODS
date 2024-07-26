import pandas as pd

# Sample data
data = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'age': [25, 30, 22, 25, 30, 35, 40, 22, 25, 30],
    'purchase_amount': [100, 150, 200, 100, 150, 200, 250, 100, 150, 200],
    'purchase_date': ['2024-07-01', '2024-07-02', '2024-07-03', '2024-07-04', '2024-07-05', '2024-07-06', '2024-07-07', '2024-07-08', '2024-07-09', '2024-07-10']
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate frequency distribution of ages
age_distribution = df['age'].value_counts().sort_index()

print("Frequency distribution of ages:")
print(age_distribution)
