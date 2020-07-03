from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.get("http://127.0.0.1/upload/forum.php")
browser.maximize_window()

# 当前窗口句柄
print("当前窗口：", browser.current_window_handle)
# 所有窗口句柄
print("所有窗口：", browser.window_handles)

# 点击活动
browser.find_element_by_link_text("活动").click()
sleep(1)

# 当前窗口句柄
print("点击活动后当前窗口：", browser.current_window_handle)
# 所有窗口句柄
print("点击活动后所有窗口：", browser.window_handles)


# 切换到新窗口
browser.switch_to_window(browser.window_handles[1])
sleep(1)

browser.find_element_by_id("scform_srchtxt").clear()
browser.find_element_by_id("scform_srchtxt").send_keys("find")


print("切换后当前窗口：", browser.current_window_handle)


sleep(3)
browser.quit()