import pandas as pd
import os
from text_preprocessing import preprocess_text

def save_excel(comments, timestamps, users, filename="youtube_comments.xlsx"):
    if os.path.exists(filename):
        df = pd.read_excel(filename)
    else:
        df = pd.DataFrame(columns=["Timestamp", "User", "Comment", "Sentiment"])

    for comment, timestamp, user in zip(comments, timestamps, users):
        try:
            # Get the raw comment text
            raw_comment = comment.get_text(strip=True)
            
            # Apply text preprocessing
            processed_comment = preprocess_text(str(raw_comment))
            
            # print(processed_comment, " - ", timestamp.get_text(strip=True), "by", user.get_text(strip=True))
            new_data_df = pd.DataFrame([{"Timestamp": timestamp.get_text(strip=True), "User": user.get_text(strip=True), "Comment": processed_comment}])

            # Concatenate the existing data with the new data
            df = pd.concat([df, new_data_df], ignore_index=True)

        except Exception as e:
            print(f"Error, Skipped index: {e}")
            continue

    df.to_excel("youtube_comments.xlsx", index=False)
    print(f"Data saved!")






