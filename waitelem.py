import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 30).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
if button == True:
    btn = browser.find_element(By.ID,"book")
    btn.click()
message = browser.find_element(By.ID, "book")

num = browser.find_element(By.CSS_SELECTOR,'[id=input_value]').text
y = calc(num)
input_form = browser.find_element(By.CSS_SELECTOR,"[id=answer]")
input_form.send_keys(str(y))
button = browser.find_element(By.ID, "solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
time.sleep(15)