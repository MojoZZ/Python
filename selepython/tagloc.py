# 导入
from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.get("http://127.0.0.1/upload/forum.php")

# 通过tag 标签名 定位元素
# browser.find_element_by_tag_name("input").send_keys("find")



# 暂停3秒
sleep(3)
# 浏览器关闭
browser.quit()