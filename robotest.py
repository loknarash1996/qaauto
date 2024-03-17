from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import math
import time
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    treasure = browser.find_element(By.CSS_SELECTOR, "[id='treasure']")
    x_element = treasure.get_attribute("valuex")
    x = x_element
    y = calc(x)
    input_field = browser.find_element(By.CSS_SELECTOR,"input[id=answer]")
    input_field.send_keys(y)
    checker = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    checker.click()
    radio = browser.find_element(By.CSS_SELECTOR,"[id='robotsRule']")
    radio.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()