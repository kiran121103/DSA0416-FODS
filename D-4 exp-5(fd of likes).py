import pandas as pd

# Sample data
data = {
    'post_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'likes': [10, 20, 10, 30, 20, 10, 40, 30, 20, 10]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate frequency distribution of likes
likes_distribution = df['likes'].value_counts().sort_index()

print("Frequency distribution of likes:")
print(likes_distribution)
