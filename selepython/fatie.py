# 导入
from selenium import webdriver
from time import sleep,strftime
from selenium.webdriver.support.select import Select

browser = webdriver.Firefox()
browser.get("http://127.0.0.1/upload/forum.php")
browser.maximize_window()

# 登录
browser.find_element_by_id("ls_username").send_keys("admin")
browser.find_element_by_id("ls_password").send_keys("123456")
# browser.find_element_by_xpath("//button[@class='pn vm']").click()
browser.find_element_by_css_selector("button.pn.vm").click()
sleep(1)

# 点击默认版块
browser.find_element_by_link_text("默认版块").click()
sleep(1)

# 快速发帖
ftime = strftime("%Y%m%d%H%M%S")
title = f"这是标题{ftime}"
browser.find_element_by_id("subject").send_keys(title)
browser.find_element_by_id("fastpostmessage").send_keys(f"这是内容{ftime}")
browser.find_element_by_id("fastpostsubmit").click()
sleep(2)

# 判断是否发帖成功
if browser.find_element_by_id("thread_subject").text == title:
    print("success")
else:
    print("fail")


# 退出
browser.find_element_by_link_text("退出").click()
sleep(1)

sleep(5)
browser.quit()