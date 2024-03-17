from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
browser = webdriver.Chrome()
link = "https://suninjuly.github.io/redirect_accept.html"
browser.get(link)
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

button1 = browser.find_element(By.TAG_NAME, "button")
button1.click()
time.sleep(2)
browser.switch_to.window(browser.window_handles[1])

num = browser.find_element(By.CSS_SELECTOR,'[id=input_value]').text
y = calc(num)
input_form = browser.find_element(By.CSS_SELECTOR,"[id=answer]")
input_form.send_keys(str(y))
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
time.sleep(3)