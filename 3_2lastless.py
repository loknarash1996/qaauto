from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time
import unittest

value=["Да", "Конечно", "Нет", "Отнюдь", "Естественно", "Ясен-красен", "Вовсе нет!"]
class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
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

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
    def test_abs2(self):
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

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()