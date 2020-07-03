from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.get("http://127.0.0.1/upload/forum.php")
browser.maximize_window()


browser.find_element_by_link_text("默认版块").click()
sleep(1)

a_list = browser.find_elements_by_css_selector("a.xst")
# ??
# th.common>a
# th[class='common']>a
# a_list = browser.find_elements_by_css_selector(".common>a")


print(len(a_list))

# for a in a_list:
#     if a.text == "111":
#         a.click()
#         break


sleep(3)
browser.quit()