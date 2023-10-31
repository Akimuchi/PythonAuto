from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    x_value = browser.find_element(By.ID, "input_value").text


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x_value)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    radio_button = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_button)
    radio_button.click()
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

finally:

    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
