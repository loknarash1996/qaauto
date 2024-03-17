from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time
value=["Да", "Конечно", "Нет", "Отнюдь", "Естественно", "Ясен-красен", "Вовсе нет!"]
try:
    link = "http://suninjuly.github.io/registration2.html"
    #link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    firstname = browser.find_element(By.XPATH,"/html/body/div/form/div[1]/div[1]/input")
    firstname.send_keys(random.choice(value))
    lastname = browser.find_element(By.XPATH,"/html/body/div/form/div[1]/div[2]/input")
    lastname.send_keys(random.choice(value))
    email = browser.find_element(By.XPATH,"/html/body/div/form/div[1]/div[3]/input")
    email.send_keys(random.choice(value))


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
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()