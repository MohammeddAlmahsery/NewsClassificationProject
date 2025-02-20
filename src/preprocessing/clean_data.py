import pandas as pd
import os
import sys 

if os.path.exists("data/cleaned.csv"):
    sys.exit()

# Load raw data from CSV
data = pd.read_csv("data/raw.csv", names=['title', 'subtitle', 'content', 'category', 'error_pages'])

# Drop pages that does not contain any content
data = data[data['error_pages'].isnull()]
data = data.drop('error_pages', axis=1)

# Strip Data
data['title'] = data['title'].fillna('').str.strip()
data['subtitle'] = data['subtitle'].fillna('').str.strip()
data['content'] = data['content'].fillna('').str.strip()
data['category'] = data['category'].fillna('').str.strip()

data['category'] = data['category'].map(lambda x: x.split(' ', 1)[0])

# Filter out categories with fewer than 100 occurrences
category_counts = data['category'].value_counts()
data = data[data['category'].isin(category_counts[category_counts > 100].index)]

# Remove duplicate rows
data = data.drop_duplicates()   

# Drop rows with missing values
data = data.replace('', pd.NA).dropna(how='any')

# Save cleaned data to a new CSV file
data.to_csv("data/cleaned.csv", index=False, header=False)
