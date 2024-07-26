import pandas as pd

# Sample data
data = {
    'WEATHER_CONDITION': ['Sunny', 'Rainy', 'Cloudy', 'Snowy', 'Windy'],
    'OCCURRENCES': [120, 80, 100, 20, 50]
}

# Create DataFrame
df = pd.DataFrame(data)

# Find the most common weather condition
most_common_weather = df.loc[df['OCCURRENCES'].idxmax()]

print(f"The most common weather condition is {most_common_weather['WEATHER_CONDITION']} with {most_common_weather['OCCURRENCES']} occurrences.")
