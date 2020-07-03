from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.get("http://127.0.0.1/html/frame/frame_main.htm")
browser.maximize_window()

# 先切换框架
browser.switch_to.frame("LeftframeId")
browser.find_element_by_name("name").send_keys("test left")

# 先跳出当前框架，再可以跳转到其他框架
browser.switch_to.default_content()

# 先切换框架
browser.switch_to.frame("RightframeId")
browser.find_element_by_name("name").send_keys("test right")


sleep(3)
browser.quit()
