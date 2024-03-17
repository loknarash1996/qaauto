from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os

import time

current_dir = os.path.abspath(os.path.dirname(__file__))
try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    name = browser.find_element(By.CSS_SELECTOR,"input[name='firstname']")
    name.send_keys("пупа")
    secondName = browser.find_element(By.CSS_SELECTOR,"input[name='lastname']")
    secondName.send_keys("Чпоков")
    email = browser.find_element(By.CSS_SELECTOR,"input[name='email']")
    email.send_keys("lololo@ya.ru")
    file = browser.find_element(By.ID,"file")
    file_path = os.path.join(current_dir, 'text.txt')
    file.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)
    browser.quit()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()