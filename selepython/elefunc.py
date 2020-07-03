# 导入
from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.get("http://127.0.0.1/upload/forum.php")
browser.maximize_window()

# 对元素的一些操作
username = browser.find_element_by_id("ls_username")
# 赋值
username.send_keys("123456")
sleep(2)
# 清除元素中的文本
username.clear()
sleep(2)

username.send_keys("djsdjsijdsids")

# 获取属性的值
print(username.get_attribute("tabindex"))
print(username.get_attribute("autocomplete"))
print(username.get_attribute("value"))

# 查看元素是否可见
#True //td/a[text()='立即注册']
print(browser.find_element_by_xpath("//td/a[text()='立即注册']").is_displayed())
#False
print(browser.find_element_by_xpath("//div/a[text()='立即注册']").is_displayed())



sleep(4)
browser.quit()


