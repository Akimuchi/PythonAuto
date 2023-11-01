from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import pytest


class TestAbs(unittest.TestCase):

    def test_abs1(self):
        try:
            browser = webdriver.Chrome()
            link = "http://suninjuly.github.io/registration1.html"
            browser.get(link)
            browser.find_element(By.CSS_SELECTOR, "div.first_block input.first").send_keys("Ivan")
            browser.find_element(By.CSS_SELECTOR, "div.first_block input.second").send_keys("Ivanov")
            browser.find_element(By.CSS_SELECTOR, "div.first_block input.third").send_keys("d.akinfiev@oneliya.ru")
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            time.sleep(1)
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, )
        finally:
            browser.quit()

    def test_abs2(self):
        try:
            browser = webdriver.Chrome()
            link = "http://suninjuly.github.io/registration2.html"
            browser.get(link)
            browser.find_element(By.CSS_SELECTOR, "div.first_block input.first").send_keys("Ivan")
            browser.find_element(By.CSS_SELECTOR, "div.first_block input.second").send_keys("Ivanov")
            browser.find_element(By.CSS_SELECTOR, "div.first_block input.third").send_keys("d.akinfiev@oneliya.ru")
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            time.sleep(1)
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, )
        finally:
            browser.quit()


if __name__ == "__main__":
    unittest.main()
