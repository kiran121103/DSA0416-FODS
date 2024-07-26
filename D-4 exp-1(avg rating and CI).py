import pandas as pd
import numpy as np
from scipy import stats

data = {
    'product_title': ['Pineapple slicer', 'Levis Jeans Pant', 'Wallet', 'Salwar'],
    'product_category': ['Apparel', 'Apparel', 'Apparel', 'Apparel'],
    'star_rating': [4, 5, 5, 5],
    'review_headline': ['Really good', 'Perfect Dress', 'Love it', 'Awesome'],
    'review_date': ['2013-01-14', '2014-04-22', '2015-07-28', '2015-06-12']
}

df = pd.DataFrame(data)

apparel_df = df[df['product_category'] == 'Apparel']

average_rating = apparel_df['star_rating'].mean()

confidence_level = 0.95
degrees_freedom = len(apparel_df) - 1
sample_mean = np.mean(apparel_df['star_rating'])
sample_standard_error = stats.sem(apparel_df['star_rating'])
confidence_interval = stats.t.interval(confidence_level, degrees_freedom, sample_mean, sample_standard_error)

print(f"Average Rating: {average_rating}")
print(f"95% Confidence Interval: {confidence_interval}")
