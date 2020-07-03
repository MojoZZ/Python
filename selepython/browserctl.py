# 导入
from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.get("http://127.0.0.1/upload/forum.php")
sleep(1)

# 设置窗口大小
browser.set_window_size(480, 600)
sleep(1)

#设置窗口最大化
browser.maximize_window()
sleep(1)

# 点击群组
browser.find_element_by_partial_link_text("群组").click()
sleep(2)

# 后退
browser.back()
sleep(1)

#前进
browser.forward()
sleep(2)

# 刷新
browser.refresh()

sleep(4)
browser.quit()


