from selenium import webdriver
import math
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    button1 = browser.find_element_by_class_name("trollface.btn.btn-primary")
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    def calc(x):
        return str(math.log(abs(12 * math.sin(x))))

    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    submit_btn = browser.find_element_by_tag_name("button")
    submit_btn.click()

finally:
    time.sleep(10)
    browser.quit()