from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    num1 = browser.find_element(By.CSS_SELECTOR, "[id=num1]").text
    num2 = browser.find_element(By.CSS_SELECTOR, "[id=num2]").text
    res = int(num1)+int(num2)
    res = str(res)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(res)
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