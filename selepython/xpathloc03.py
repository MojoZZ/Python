# 导入
from selenium import webdriver
from time import sleep

# 自动登录
browser = webdriver.Firefox()
browser.get("http://127.0.0.1/upload/forum.php")

# 相对路径定位
browser.find_element_by_xpath("//input[@id='ls_username']").send_keys("admin")
browser.find_element_by_xpath("//input[@name='password']").send_keys("123456")
browser.find_element_by_xpath("//button[@class='pn vm']").click()

# 设置时间差
sleep(3)

# 定位登录之后的用户名
# 判断是否与预期结果一致
user = browser.find_element_by_xpath("//a[@title='访问我的空间']").text
if user == "admin":
    print("success")
else:
    print("fail")


# 点击退出
# Xpath模糊匹配
# contains方法
# starts-with方法
# text方法
# browser.find_element_by_xpath("//a[contains(@href, 'logout')]").click()
# browser.find_element_by_xpath("//a[starts-with(@href, 'member.php?mod=l')]").click()
browser.find_element_by_xpath("//a[text()='退出']").click()


sleep(3)
# 浏览器关闭
browser.quit()