import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
try:
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной

    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    browser.find_element(By.ID, "book").click()
    x_value = browser.find_element(By.ID, "input_value").text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x_value)
    browser.find_element(By.ID, "answer").send_keys(y)
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]")
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()
