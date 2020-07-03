# 导入
from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("http://127.0.0.1/upload/forum.php")

# css选择器定位
# input 中 id为ls_username的元素
# browser.find_element_by_css_selector("input#ls_username").send_keys("admin")
# 属性选择器
browser.find_element_by_css_selector("[name='username']").send_keys("admin")
# browser.find_element_by_css_selector("input#ls_password").send_keys("123456")
# 属性选择器
browser.find_element_by_css_selector("input[tabindex='902']").send_keys("123456")
# 类选择器
# browser.find_element_by_css_selector(".pn.vm").click()
# 父子元素
browser.find_element_by_css_selector(".pn.vm>em").click()

# 以什么开始
# print(browser.find_element_by_css_selector("div[id^=top]").get_attribute("innerHTML"))
# 以什么结束
# print(browser.find_element_by_css_selector("div[id$=db]").get_attribute("innerHTML"))


# 暂停3秒
time.sleep(5)
# 浏览器关闭
browser.quit()