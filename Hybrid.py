import time
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with Chrome() as driver:
    wait = WebDriverWait(driver, 15)
    driver.get("https://www.youtube.com/watch?v=pgPUesOIgm0")

    # Scroll to load comments
    for _ in range(3):  # increase for more comments
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(5)

    # Get page source after scrolling
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # Parse comments with BeautifulSoup
    comments = soup.select("#content-text")
    timestamps = soup.select("#published-time-text")
    users = soup.select("#author-text span")

    for comment, timestamp, user in zip(comments, timestamps, users):
        print(comment.get_text(strip=True), " : ", timestamp.get_text(strip=True), "by", user.get_text(strip=True))
