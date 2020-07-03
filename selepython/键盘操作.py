# 导入Keys
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("http://127.0.0.1/upload/forum.php")
browser.maximize_window()

username = browser.find_element_by_id("ls_username")
username.send_keys("admin")
sleep(1)
# 删除键
username.send_keys(Keys.BACK_SPACE)

# 全选复制
username.send_keys(Keys.CONTROL, "a")
username.send_keys(Keys.CONTROL, "c")
sleep(1)

# 粘贴
browser.find_element_by_id("scbar_txt").send_keys(Keys.CONTROL, "v")
sleep(1)

# 回车
# browser.find_element_by_id("ls_password").send_keys("123456")
# browser.find_element_by_css_selector("button.pn.vm").send_keys(Keys.ENTER)



sleep(3)
browser.quit()