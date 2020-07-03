from selenium import webdriver
from time import sleep,strftime

browser = webdriver.Firefox()
browser.get("http://127.0.0.1/html/alert.html")
browser.maximize_window()
browser.implicitly_wait(5)


# 弹出框的操作
browser.find_element_by_id("alert").click()
sleep(1)

# 切换弹出框
browser.switch_to.alert.accept()
sleep(1)

# confirm
browser.find_element_by_id("confirm").click()
sleep(1)
# 确定
# browser.switch_to.alert.accept()
# 取消
browser.switch_to.alert.dismiss()

browser.refresh()


# prompt
browser.find_element_by_id("prompt").click()
browser.switch_to.alert.send_keys("test")
sleep(1)
browser.switch_to.alert.accept()




sleep(3)
browser.quit()
