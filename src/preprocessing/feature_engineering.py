import pandas as pd
from nltk.corpus import stopwords
from utils import lower_and_special
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import LabelEncoder
import contractions
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os
import sys 

if os.path.exists("src/preprocessing/train_test_data.pkl"):
    sys.exit()

data = pd.read_csv("data/cleaned.csv", names=['title', 'subtitle', 'content', 'categories'])

# Expand contractions. For example don't -> do not
data['title'] = data['title'].map(contractions.fix)
data['subtitle'] = data['subtitle'].map(contractions.fix)
data['content'] = data['content'].map(contractions.fix)
data['categories'] = data['categories'].map(contractions.fix)

# Remove special characters and convert to lower case
data['title'] = data['title'].map(lower_and_special)
data['subtitle'] = data['subtitle'].map(lower_and_special)
data['content'] = data['content'].map(lower_and_special)
data['categories'] = data['categories'].map(lower_and_special)

# Remove stopwords and lemmatize
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

data['title'] = data['title'].apply(lambda x: ' '.join([lemmatizer.lemmatize(word) for word in x.split() if word not in stop_words]))
data['content'] = data['content'].apply(lambda x: ' '.join([lemmatizer.lemmatize(word) for word in x.split() if word not in stop_words]))

# Encode categories
label_encoder = LabelEncoder()
data['category_encoded'] = label_encoder.fit_transform(data['categories'])

# Combine title, subtitle and content
data['full_text'] = data['title'] + " " + data['subtitle'] + " " + data['content']

# Split data into train and test
X_train, X_test, y_train, y_test = train_test_split(data['full_text'], data['category_encoded'], train_size=100000, test_size=2000, stratify=data['category_encoded'])

# Vectorize text
tfidf_vectorizer = TfidfVectorizer(max_features=500, ngram_range=(1,2), min_df=5)
X_train_vec = tfidf_vectorizer.fit_transform(X_train)
X_test_vec = tfidf_vectorizer.transform(X_test)

# Save the vectorizer, label encoder, and train-test data
with open("src/preprocessing/tfidf_vectorizer.pkl", "wb") as file:
    pickle.dump(tfidf_vectorizer, file)

with open("src/preprocessing/label_encoder.pkl", "wb") as file:
    pickle.dump(label_encoder, file)

pickle.dump((X_train_vec, X_test_vec, y_train, y_test), open(r"src/preprocessing/train_test_data.pkl", "wb"))
