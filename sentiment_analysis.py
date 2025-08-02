from transformers import pipeline

# # Use a pipeline as a high-level helper
# from transformers import pipeline

# pipe = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment-latest")

# def analyze_sentiment(text):
#     result = pipe(text)
#     print("Result")
#     print(result)
#     print("-----------------------------------------")
#     sentiment = result[0]['label']
#     return sentiment

####################################################################################

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def analyze_sentiment(text):
    candidate_labels = ["positive", "negative", "neutral"]

    # Get the initial sentiment classification result
    result = classifier(text, candidate_labels)

    highest_score_idx = result['scores'].index(max(result['scores']))
    highest_score_label = result['labels'][highest_score_idx]
    highest_score = result['scores'][highest_score_idx]

    return highest_score_label