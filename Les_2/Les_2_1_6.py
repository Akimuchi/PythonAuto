from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
try:
    link = "https://suninjuly.github.io/math.html"
    browser.get(link)

    x_value = browser.find_element(By.CSS_SELECTOR, "span#input_value").text


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x_value)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()

finally:

    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
