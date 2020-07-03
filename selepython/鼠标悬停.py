# 导入ActionChains 动作链
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

browser = webdriver.Firefox()
browser.get("http://127.0.0.1/upload/forum.php")
browser.maximize_window()

reg_obj = browser.find_element_by_xpath("//div/a[text()='立即注册']")
# False
# print("悬停前：", reg_obj.is_displayed())


# ActionChains对象，参数为浏览器
ac = ActionChains(browser)
# 鼠标悬停到导航上
# 获取快速导航对象，传递给ac，并调用执行动作方法perform()
# ac.move_to_element(browser.find_element_by_id("qmenu")).perform()

# True
# print("悬停后：", reg_obj.is_displayed())

# 悬停后点击立即注册
ac.move_to_element(browser.find_element_by_id("qmenu")).click(reg_obj).perform()

sleep(3)
browser.quit()

