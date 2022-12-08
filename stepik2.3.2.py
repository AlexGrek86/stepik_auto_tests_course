from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return math.log(abs(12*math.sin(int(x))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    number = browser.find_element(By.ID, 'input_value').text
    result = calc(number)
    browser.find_element(By.ID, 'answer').send_keys(result)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

