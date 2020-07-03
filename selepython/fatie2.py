# 导入
from selenium import webdriver
from time import sleep,strftime
from selenium.webdriver import ActionChains


browser = webdriver.Firefox()
browser.get("http://127.0.0.1/upload/forum.php")
browser.maximize_window()
browser.implicitly_wait(5)

# 登录
browser.find_element_by_id("ls_username").send_keys("admin")
browser.find_element_by_id("ls_password").send_keys("123456")
browser.find_element_by_css_selector("button.pn.vm").click()
sleep(1)

# 点击默认版块
browser.find_element_by_link_text("默认版块").click()
sleep(1)

# 鼠标移动到发帖按钮上

ele1 = browser.find_element_by_id("newspecial")
# css ul#newspecial_menu>li>a
ele2 = browser.find_element_by_xpath("//ul[@id='newspecial_menu']/li/a[text()='发表帖子']")
# 定位不到??
# ele2 = browser.find_element_by_link_text("发表帖子")
# print(fatie.is_displayed())
ActionChains(browser).move_to_element(ele1).click(ele2).perform()
sleep(1)

# subject
ftime = strftime("%Y%m%d%H%M%S")
title = f"这是标题{ftime}"
browser.find_element_by_id("subject").send_keys(title)
sleep(1)
#
# # 切换框架
browser.switch_to.frame("e_iframe")
browser.find_element_by_tag_name("body").send_keys(f"这是内容{ftime}")
sleep(1)

# 切换框架
browser.switch_to.default_content()
#
# 提交 #postsubmit.pn.pnc
# browser.find_element_by_id("postsubmit").click()
# browser.find_element_by_css_selector("button#postsubmit.pn.pnc").click()
browser.find_element_by_css_selector("#postsubmit[type='submit']").click()
# sleep(1)

# 退出
browser.find_element_by_link_text("退出").click()

sleep(5)
browser.quit()
