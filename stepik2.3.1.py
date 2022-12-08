from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return math.log(abs(12*math.sin(int(x))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    alert = browser.switch_to.alert
    alert.accept()

    number = browser.find_element(By.ID, 'input_value').text
    result = calc(number)
    browser.find_element(By.ID, 'answer').send_keys(result)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

