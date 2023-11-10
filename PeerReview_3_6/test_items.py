import time
from selenium.webdriver.common.by import By


def test_check_add_to_cart_button_is_available(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    add_to_cart_button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert len(add_to_cart_button) > 0, "Add to cart button is not displayed"

