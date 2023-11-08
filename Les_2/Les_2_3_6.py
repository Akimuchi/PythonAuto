from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pyperclip

browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()
    browser.switch_to.window(browser.window_handles[1])

    x_value = browser.find_element(By.ID, "input_value").text


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x_value)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()

    text = browser.switch_to.alert.text.replace(
        'Congrats, you\'ve passed the task! Copy this code as the answer to Stepik quiz:', '')
    pyperclip.copy(text)
    print(text)

finally:

    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()