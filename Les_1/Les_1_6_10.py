from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.CSS_SELECTOR, "div.first_block input.first").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "div.first_block input.second").send_keys("Ivanov")
    browser.find_element(By.CSS_SELECTOR, "div.first_block input.third").send_keys("d.akinfiev@oneliya.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
