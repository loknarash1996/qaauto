from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


num = browser.find_element(By.CSS_SELECTOR,'[id=input_value]').text
print(num)
y = calc(num)
input_form = browser.find_element(By.CSS_SELECTOR,"[id=answer]")
input_form.send_keys(str(y))
checker = browser.find_element(By.CSS_SELECTOR,"[for='robotCheckbox']")
checker.click()
browser.execute_script("return arguments[0].scrollIntoView(true);", checker)
browser.find_element(By.CSS_SELECTOR,"[id=robotsRule]").click()
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
time.sleep(3)