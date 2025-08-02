import time
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os

#########################################################################################################

def scrape_youtube_comments(url):
    try:
        with Chrome() as driver:
            wait = WebDriverWait(driver, 15)
            driver.get(url)

            # Scroll to load comments
            for _ in range(8):
                try:
                    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
                    time.sleep(5)

                except Exception as e:
                    print(f"Error during scrolling: {e}")
                    continue

            # Get page source after scrolling
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")

            # Parse comments with BeautifulSoup
            comments = soup.select("#content-text")
            timestamps = soup.select("#published-time-text")
            users = soup.select("#author-text span")

            return comments, timestamps, users
        
    except Exception as e:
        print(f"Error during scraping: {e}")
        return [], [], []

    

#########################################################################################################

# url = "https://www.youtube.com/watch?v=pgPUesOIgm0"
# comments, timestamps, users = scrape_youtube_comments(url)

# #########################################################################################################

# if os.path.exists("youtube_comments.xlsx"):
#     df = pd.read_excel("youtube_comments.xlsx")
# else:
#     df = pd.DataFrame(columns=["Timestamp", "User", "Comment"])

# #########################################################################################################

# for comment, timestamp, user in zip(comments, timestamps, users):
#     # print(comment.get_text(strip=True), " - ", timestamp.get_text(strip=True), "by", user.get_text(strip=True))
#     new_data_df = pd.DataFrame([{"Timestamp": timestamp.get_text(strip=True), "User": user.get_text(strip=True), "Comment": comment.get_text(strip=True)}])

#     # Concatenate the existing data with the new data
#     df = pd.concat([df, new_data_df], ignore_index=True)

#########################################################################################################

# df.to_excel("youtube_comments.xlsx", index=False)