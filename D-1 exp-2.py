import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
data = {
    'SmokingHabits': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    'LungCancerRates': [1, 3, 5, 6, 9, 10, 12, 14, 17, 20]
}
df = pd.DataFrame(data)

# Calculate the Pearson correlation coefficient
correlation, _ = pearsonr(df['SmokingHabits'], df['LungCancerRates'])
print(f'Correlation Coefficient: {correlation}')

# Create a scatter plot
plt.scatter(df['SmokingHabits'], df['LungCancerRates'])
plt.title('Scatter Plot of Smoking Habits vs Lung Cancer Rates')
plt.xlabel('Smoking Habits (cigarettes per day)')
plt.ylabel('Lung Cancer Rates (cases per 1000 individuals)')
plt.show()
