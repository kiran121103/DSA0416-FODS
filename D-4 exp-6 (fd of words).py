import pandas as pd
from collections import Counter
import re

# Sample data
data = {
    'review_id': [1, 2, 3, 4],
    'review_text': [
        "Really good product, I love it!",
        "Perfect dress, fits well and looks great.",
        "Love it, very comfortable and stylish.",
        "Awesome quality, highly recommend!"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Function to clean and tokenize text
def clean_and_tokenize(text):
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text).lower()
    # Split text into words
    words = text.split()
    return words

# Apply the function to the review_text column
df['words'] = df['review_text'].apply(clean_and_tokenize)

# Flatten the list of words
all_words = [word for words_list in df['words'] for word in words_list]

# Calculate frequency distribution
word_freq = Counter(all_words)

print("Frequency distribution of words:")
print(word_freq)
