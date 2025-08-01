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

    for comment in comments:
        print(comment.get_text(strip=True))

# in this code, I used BeautifulSoup to parse the HTML content after scrolling to load comments. 
# Scrolling is done using Selenium, and I extract the comments using CSS selectors. 
# This approach allows for more flexibility in parsing and handling the HTML structure.