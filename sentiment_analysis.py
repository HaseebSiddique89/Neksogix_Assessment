from transformers import pipeline

# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment-latest")

def analyze_sentiment(text):
    result = pipe(text)
    print("Result")
    print(result)
    print("-----------------------------------------")
    sentiment = result[0]['label']
    return sentiment

text = "I Love programming! It's so much interesting."
sentiment = analyze_sentiment(text)
print(f"Sentiment: {sentiment}")