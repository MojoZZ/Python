# 导入
from selenium import webdriver
from time import sleep

# 调用webdriver模块下的Chrome或者Firefox类，生成一个浏览器对象
# browser = webdriver.Chrome()
browser = webdriver.Firefox()
# 访问一个url
browser.get("http://127.0.0.1/upload/forum.php")

# 定位元素 通过id定位
ls_username = browser.find_element_by_id("ls_username")
# 给元素赋值
ls_username.send_keys("admin")

browser.find_element_by_id("ls_password").send_keys("123456")


# browser.find_element_by_class_name("pn.vm").click()


# 暂停3秒
sleep(3)
# 浏览器关闭
browser.quit()