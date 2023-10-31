from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser.get(link)

    x_value = browser.find_element(By.ID, "num1").text
    y_value = browser.find_element(By.ID, "num2").text

    def calc(x, y):
        return str(x + y)

    z = calc(int(x_value), int(y_value))
    Select(browser.find_element(By.CSS_SELECTOR, "select.custom-select")).select_by_value(z)
    browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()

finally:

    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
