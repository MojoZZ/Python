# 导入
from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("http://127.0.0.1/upload/forum.php")

# 查找a元素 并点击
browser.find_element_by_link_text("立即注册").click()
# 查找a元素，内容是text中的一部分，模糊查找
# browser.find_element_by_partial_link_text("注册").click()

# browser.find_element_by_xpath("//div/a[text()='立即注册']")
# browser.find_element_by_xpath("//td/a[text()='立即注册']")

# 也可以用一个大点范围的随机数
ftime = time.strftime("%Y%m%d%H%M%S")
username = "u"+ftime
browser.find_element_by_id("TwQ1h2").send_keys(username)
browser.find_element_by_id("Y54tYW").send_keys("123456")
browser.find_element_by_id("fk4710").send_keys("123456")
browser.find_element_by_id("Tkniac").send_keys(username+"@126.com")
browser.find_element_by_id("registerformsubmit").click()
# 暂停3秒
time.sleep(5)
# 浏览器关闭
browser.quit()