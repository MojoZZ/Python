# 导入
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select

browser = webdriver.Firefox()
browser.get("http://127.0.0.1/upload/forum.php")
browser.maximize_window()
# 隐式等待，针对所有元素，可以不用sleep
browser.implicitly_wait(5)

browser.find_element_by_id("ls_username").send_keys("admin")
browser.find_element_by_id("ls_password").send_keys("123456")
browser.find_element_by_xpath("//button[@class='pn vm']").click()
# 强制等待，可以用于程序调试
# sleep(1)

browser.find_element_by_link_text("设置").click()


# 关于select的操作
# 省份
resideprovince = browser.find_element_by_id("resideprovince")
pros = Select(resideprovince)
# option中的value
# pros.select_by_value("浙江省")
# select下拉框中的文本的显示
pros.select_by_visible_text("江苏省")
# sleep(1)

# 城市
residecity = browser.find_element_by_id("residecity")
Select(residecity).select_by_value("南京市")
# sleep(1)

# 州县
residedist = browser.find_element_by_id("residedist")
Select(residedist).select_by_value("玄武区")
# sleep(1)

#residecommunity
residecommunity = browser.find_element_by_id("residecommunity")
Select(residecommunity).select_by_value("孝陵卫街道")


# 暂停3秒
sleep(5)
# 浏览器关闭
browser.quit()

