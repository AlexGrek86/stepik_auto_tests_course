from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your name']")
    first_name.send_keys("Ivan")
    email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    email.send_keys("vasya@pizdabol.com")
    phone = browser.find_element(By.XPATH, "//input[@placeholder='Input your phone']")
    phone.send_keys("937-99-92")
    adress = browser.find_element(By.XPATH, "//input[@placeholder='Input your address']")
    adress.send_keys("Canada")

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()