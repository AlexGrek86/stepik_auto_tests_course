from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, 'firstname').send_keys('Vasya')
    browser.find_element(By.NAME, 'lastname').send_keys('Pupkin')
    browser.find_element(By.NAME, 'email').send_keys('vasya_pyos@gmail.com')

    file_path= os.path.abspath('file.html')
    # current_dir = os.path.abspath(os.path.dirname(__file__))
    # file_path = os.path.join(current_dir, 'file.html')
    upload_btn = browser.find_element(By.NAME, 'file')
    upload_btn.send_keys(file_path)

    submit_button = browser.find_element(By.CSS_SELECTOR,
                                         "button[type='submit']")
    submit_button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()