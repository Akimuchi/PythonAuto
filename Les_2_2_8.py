from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()
try:
    link = "https://suninjuly.github.io/file_input.html"
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "input[name=\"firstname\"]").send_keys("Piska")
    browser.find_element(By.CSS_SELECTOR, "input[name=\"lastname\"]").send_keys("Popka")
    browser.find_element(By.CSS_SELECTOR, "input[name=\"email\"]").send_keys("piska-popka@test.ru")

    element = browser.find_element(By.CSS_SELECTOR, "input[type=\"file\"]")
    # получаем путь к директории текущего исполняемого скрипта lesson2_7.py
    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)

    # имя файла, который будем загружать на сайт
    file_name = "piska.txt"

    # получаем путь к file_example.txt
    file_path = os.path.join(current_dir, file_name)
    # отправляем файл
    element.send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()
finally:

    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()