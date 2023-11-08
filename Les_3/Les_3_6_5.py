import pytest
import config
import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

result = ''
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(result)


@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_auth(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.get(link)
    # Авторизуемся
    browser.find_element(By.CSS_SELECTOR, "a.ember-view.navbar__auth.navbar__auth_login").click()
    browser.find_element(By.ID, "id_login_email").send_keys(config.auth_login)
    browser.find_element(By.ID, "id_login_password").send_keys(config.auth_pass)
    browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()
    # Считаем ответ
    answer = str(math.log(int(time.time())))
    # Ждём когда появится и запоминаем поле
    answer_field = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "textarea.ember-text-area")))
    # Отправляем ответ
    answer_field.send_keys(answer)
    # Ждём и нажимаем "Отправить"
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))).click()
    # Ждем получения ответа и считываем правильный ли ответ
    result_text = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint")))
    try:
        assert 'Correct' == result_text
    except AssertionError:
        global result
        result += result_text
