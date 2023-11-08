from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
try:
    # подготовка для теста
    # открываем страницу первого товара
    # данный сайт не существует, этот код приведен только для примера
    browser.get("https://market.yandex.ru/product--yandex-stantsiia-2-umnaia-kolonka-s-alisoi/1488561450?sku=10152363"
                "4768&showUid=16983370458697506708306008&cpc=_Q8UvVvoeMLitaxZ1YdrOsb_XZ0bpseKKLD55a5X0mTGRiAcRRDUO8cj"
                "wAxxenUdXSb7dQ9oeCLvNX0s12rxXqC7xz53hchmawwMaF8T9e6gAC6EqpNOrQX6ZvWXwCp0iTYksGCRuIOXBwtslB26MVkgacD3"
                "_hJQFFUnCXh79CJwmHto7vttL6ivinwW-Nn4N9_JDrXW4-MG8_q4b7TWuzl_nUkGpXsx8Mn7WNkAgjGG2Ihi-BSP6HiqPLJsMRcx"
                "G1PRwCnytoGvgouhFiAXDx5OlDcLAIhoVcZxMADwnoZQjkhXNTqOIeg2rSbzXqAB&from=search&cpa=1&uniqueId=924574&"
                "do-waremd5=-TNreRQZtukfdNIStedvHg")
    # добавляем товар в корзину
    browser.find_element(By.CSS_SELECTOR, "button._2AMPZ._2zbuI._3_b2k._390_8._3Nc4D.v_z7D.pvpsJ._2E5lP._2Eisd").click()
    # ждем открытия модального окна
    sleep(2)
    # Продолжаем покупки
    browser.find_element(By.CSS_SELECTOR, "button._2AMPZ._1tgZz._3rgh4>span").click()
    # открываем страницу второго товара
    browser.get("https://market.yandex.ru/product--igrovoi-nabor-zuru-metal-machines-trek-s-mashinkoi-krokodil/89360"
                "6413?sku=101254781927&showUid=16983370458727572645506012&cpc=_Q8UvVvoeML6T2_os6B3SlBMgPumeZmu7-XFi8"
                "SUvl5Y_RKF4VX0GDCZjpGkMvBa4H3-YsG4DhYyhSq4AKHNgOV9hCoiJ54rqIYzaVoeAp8hoHuhPI_80QjlYgXszLKWxIiyMOdbg"
                "y2VWK6y9iDIsckgvmupbcXi3cKmY3DZGZNYK-kt1F9TXTeO1F8_5nEer7vt4R95UJ9JSaUnpukYBF9LHkq8xHOK2-VPINY33FVP"
                "-iu2fhMeqZ_qemh3R7YToXyUzzdNg0G-gycIU2XH-gJZQE_TMUCdYasNkA57vEvGC0zBTXEeX5gPA3NGfT4X&from=search&cp"
                "a=1&uniqueId=924574&do-waremd5=qYk5e-wfldk48AOxuhrqqA")
    # добавляем товар в корзину
    browser.find_element(By.CSS_SELECTOR, "button._2AMPZ._2zbuI._3_b2k._390_8._3Nc4D.v_z7D.pvpsJ._2E5lP._2Eisd").click()
    # ждем открытия модального окна
    sleep(2)
    # открываем корзину
    browser.find_element(By.CSS_SELECTOR, "a[data-auto=\"go-to-cart-button\"]").click()
    # ищем все добавленные товары
    goods = browser.find_elements(By.CSS_SELECTOR, "div[data-auto=\"CartOffer\"]")
    # проверяем, что количество товаров равно 2
    if len(goods) == 2:
        print("true")
    else:
        print("false")

finally:
    sleep(2)
    browser.close()
    browser.quit()
