import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Edge()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    time.sleep(7)

except Exception as e:
    print("Something went wrong")
    print(e)

