# 导入ActionChains 动作链
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

browser = webdriver.Firefox()
browser.get("http://127.0.0.1/html/mousedrag.html")
browser.maximize_window()

# 鼠标拖动
source = browser.find_element_by_id("dragger")
target1 = browser.find_element_by_xpath("//div[text()='Item 1']")
target2 = browser.find_element_by_xpath("//div[text()='Item 2']")
target3 = browser.find_element_by_xpath("//div[text()='Item 3']")
target4 = browser.find_element_by_xpath("//div[text()='Item 4']")


ActionChains(browser).drag_and_drop(source, target1).perform()
sleep(1)
ActionChains(browser).drag_and_drop(source, target2).perform()
sleep(1)
ActionChains(browser).drag_and_drop(source, target3).perform()
sleep(1)
ActionChains(browser).drag_and_drop(source, target4).perform()


sleep(3)
browser.quit()

