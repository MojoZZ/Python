from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.get("http://127.0.0.1/html/checkbox.html")
browser.maximize_window()

# 获取一组元素
# list = browser.find_elements_by_tag_name("input")
list = browser.find_elements_by_xpath("//input[@type='checkbox']")

print(list, type(list))

for i in list:
    i.click()

sleep(3)
browser.quit()