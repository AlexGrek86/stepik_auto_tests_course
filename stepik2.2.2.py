from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try:
    link = " http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(int(x))
    pole = browser.find_element(By.ID, "answer")
    pole.send_keys(y)
    submit_button = browser.find_element(By.CSS_SELECTOR,
                                         "button[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);",
                                          submit_button)
    checkbox_btn = browser.find_element(By.ID, "robotCheckbox")
    checkbox_btn.click()
    radio_btn = browser.find_element(By.ID, "robotsRule")
    radio_btn.click()
    submit_button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()