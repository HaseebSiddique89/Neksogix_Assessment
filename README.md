# YouTube Comment Sentiment Analysis Project

A comprehensive machine learning project that scrapes YouTube comments, performs sentiment analysis, and builds predictive models to classify comment sentiments.

## Features

- **YouTube Comment Scraping**: Automated scraping of YouTube comments using Selenium and BeautifulSoup
- **Sentiment Analysis**: Zero-shot classification using Facebook's BART model for sentiment detection
- **Text Preprocessing**: Advanced text cleaning including emoji handling, spell checking, and contraction expansion
- **Machine Learning Models**: Logistic Regression implementation for sentiment prediction
- **Data Management**: Excel-based data storage and retrieval system
- **Hybrid Approach**: Combines rule-based preprocessing with ML-based sentiment analysis

## Project Structure

```
Neksogix_Assessment/
├── main.ipynb                 # Main Jupyter notebook with workflow
├── Hybrid.py                  # YouTube comment scraping functionality
├── sentiment_analysis.py      # Sentiment analysis using transformers
├── Logistic_Regression.py     # ML model implementation
├── save_data.py              # Data saving and management utilities
├── text_preprocessing.py     # Text cleaning and preprocessing
├── stack_overflow.py         # Additional utility functions
├── Model/
│   └── logistic_model.joblib # Trained model file
├── SQLite db/
│   └── youtube_comments.db   # Database storage
├── resources/
│   ├── requirements.txt      # Python dependencies
│   └── resources.txt        # Additional resources
└── youtube_comments.xlsx    # Sample data file
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Neksogix_Assessment
   ```

2. **Install dependencies**
   ```bash
   pip install -r resources/requirements.txt
   ```

3. **Install Chrome WebDriver** (for Selenium)
   - Download ChromeDriver from: https://chromedriver.chromium.org/
   - Add it to your system PATH

## Dependencies

- **Data Processing**: `pandas`, `openpyxl`
- **Web Scraping**: `selenium`, `beautifulsoup4`
- **Text Processing**: `contractions`, `emoji`, `pyspellchecker`
- **Machine Learning**: `scikit-learn`, `transformers`, `torch`
- **Natural Language Processing**: `transformers` (Hugging Face)

## Usage

### 1. Scraping YouTube Comments

```python
from Hybrid import scrape_youtube_comments
from save_data import save_excel

# Scrape comments from a YouTube video
url = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
comments, timestamps, users = scrape_youtube_comments(url)

# Save to Excel file
save_excel(comments, timestamps, users, filename="youtube_comments.xlsx")
```

### 2. Sentiment Analysis

```python
from sentiment_analysis import analyze_sentiment

# Analyze sentiment of a single comment
sentiment = analyze_sentiment("This video is amazing!")
print(sentiment)  # Output: positive, negative, or neutral
```

### 3. Text Preprocessing

```python
from text_preprocessing import preprocess_text

# Clean and preprocess text
cleaned_text = preprocess_text("This is gr8! 😊")
print(cleaned_text)  # Output: "this is great"
```

### 4. Machine Learning Model

```python
# Run the logistic regression model
python Logistic_Regression.py
```

## 🔧 Key Components

### Text Preprocessing Pipeline
- **Contraction Expansion**: Converts "don't" to "do not"
- **Emoji Handling**: Converts emojis to text descriptions
- **Spell Checking**: Corrects spelling errors
- **Special Character Removal**: Cleans non-alphanumeric characters
- **Case Normalization**: Converts to lowercase

### Sentiment Analysis
- Uses Facebook's BART-large-MNLI model for zero-shot classification
- Classifies comments into: positive, negative, neutral
- Provides confidence scores for predictions

### Data Management
- Excel-based storage with automatic data merging
- SQLite database backup option
- Structured data format with timestamps, users, and comments

## Sample Output

The system generates Excel files with the following columns:
- **Timestamp**: When the comment was posted
- **User**: Username of the commenter
- **Comment**: The actual comment text (preprocessed)
- **Sentiment**: Predicted sentiment (positive/negative/neutral)


## 🔍 Troubleshooting

- **ChromeDriver Issues**: Make sure ChromeDriver is in your PATH
- **Memory Issues**: For large datasets, consider processing in batches
---