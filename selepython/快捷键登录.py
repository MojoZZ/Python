# 导入Keys
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("http://127.0.0.1/upload/forum.php")
browser.maximize_window()
# 隐式等待，针对所有元素，可以不用sleep
browser.implicitly_wait(5)

username = browser.find_element_by_id("ls_username")
username.send_keys("admin")

#tab 键
username.send_keys(Keys.TAB)

sleep(3)
browser.quit()