# 导入
from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.get("http://127.0.0.1/upload/forum.php")

# 通过name定位
browser.find_element_by_name("username").send_keys("admin")
browser.find_element_by_name("password").send_keys("123456")


# 暂停3秒
sleep(3)
# 浏览器关闭
browser.quit()