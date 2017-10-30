from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

usr = "A@K.com"
pwd = "password"

driver = webdriver.Chrome()

driver.set_window_size(1024, 600)
driver.maximize_window()

driver.get('http://linkedin.com')
data = driver.find_element_by_id('login-email')
data.send_keys(usr)
data = driver.find_element_by_id('login-password')
data.send_keys(pwd)
data.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 3.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


