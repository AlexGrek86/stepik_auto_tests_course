from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    pole = browser.find_element(By.ID, "answer")
    pole.send_keys(y)
    checkbox_btn = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    checkbox_btn.click()
    radio_btn = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio_btn.click()
    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit_button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()