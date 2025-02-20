# News Classification Project

## Project Overview
This project aims to classify news articles scraped from a website. The pipeline involves scraping, preprocessing, feature engineering, and training a machine learning model to classify news articles into predefined categories.

## Project Structure
```
project_directory/
│-- data/
│   │-- raw.csv                 # Raw scraped articles
│   │-- cleaned.csv              # Cleaned and preprocessed articles
│
│-- src/
│   │-- scraping/
│   │   │-- scraper.py          # Script to scrape news articles
│   │   │-- utils.py            # Helper functions for scraping
│   │
│   │-- preprocessing/
│   │   │-- clean_data.py       # Script to clean and preprocess data
│   │   │-- feature_engineering.py  # Script for feature extraction
│   │   │-- utils.py            # Helper functions for preprocessing
│   │
│   │-- models/
│   │   │-- train.py            # Train the classification model
│   │   │-- evaluate.py         # Evaluate the trained model
│
│-- main.py                     # Main script to run preprocessing and model training
│-- README.md                    # Project documentation
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/MohammeddAlmahsery/NewsClassificationProject.git
   cd NewsClassificationProject/
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

## Usage
### 1. Scraping Data
Run the scraper to collect news articles:
```bash
python src/scraping/scraper.py
```
This will generate `raw.csv` in the `data/` folder.

### 2. Preprocessing and Feature Engineering
- Run the preprocessing script to clean the data:
```bash
python src/preprocessing/clean_data.py
```

This will generate `cleaned.csv` in the `data/` folder.

- Run feature engineering script to transform data and pre-process columns:
```bash
python src/preprocessing/feature_engineering.py
```

This will generate `tfidf_vectorizer.pkl`, `label_encoder.pkl`, and `train_test_split.pkl` in the `src/preprocessing/` folder.

### 3. Training the Model
Train the model using:
```bash
python src/models/train.py
```
### 4. Evaluating the Model
Evaluate the trained model:
```bash
python src/models/evaluate.py
```

### 5. Running the Full Pipeline
You can run the entire pipeline using `main.py` :
```bash
python main.py
```

## Configuration
- Modify `scraper.py` to change the scraping source or parameters.
- Adjust preprocessing steps in `clean_data.py` and `feature_engineering.py` as needed.
- Configure model parameters in `train.py`.

## Dependencies
Ensure you have the following Python libraries installed:
```
- pandas
- numpy
- scikit-learn
- beautifulsoup4
- requests
- nltk
- subprocess
- contractions
```

## Author
**Mohammed Saadeh**

