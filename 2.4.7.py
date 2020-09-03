from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    book_button = browser.find_element_by_id("book")

    element1 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    book_button.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(x))))

    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    submit_btn = browser.find_element_by_id("solve")
    submit_btn.click()

finally:
    time.sleep(10)
    browser.quit()