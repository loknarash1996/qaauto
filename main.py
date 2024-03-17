from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string
letters = string.ascii_lowercase
value=["Да", "Конечно", "Нет", "Отнюдь", "Естественно", "Ясен-красен", "Вовсе нет!"]
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements(By.CSS_SELECTOR,'input[type="text.txt"]')
    print(elements)
    for element in elements:
        element.send_keys(random.choice(value))

    button = browser.find_element(By.XPATH, "/html/body/div/form/div[6]/button[3]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла