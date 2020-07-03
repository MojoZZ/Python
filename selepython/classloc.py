# 导入
from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.get("http://127.0.0.1/upload/forum.php")

# 通过class定位元素
browser.find_element_by_class_name("xg1").send_keys("find")

# 可能会有多个元素都是同一个class，这里只会找第一个
browser.find_element_by_class_name("px.vm").send_keys("admin")
browser.find_element_by_class_name("px.vm").send_keys("123456")


# 暂停3秒
sleep(3)
# 浏览器关闭
browser.quit()