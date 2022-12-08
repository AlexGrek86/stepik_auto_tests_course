from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    number1 = browser.find_element(By.ID, "num1")
    num1 = number1.text
    number2 = browser.find_element(By.ID, "num2")
    num2 = number2.text
    summa = int(num1) + int(num2)
    find_elem = browser.find_element(By.ID, "dropdown")
    select = Select(find_elem)
    result = select.select_by_value(str(summa))
    submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()