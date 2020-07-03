# 导入
from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.get("http://127.0.0.1/upload/forum.php")

# 浏览器中可以选中元素，复制xpath
# 绝对路径查找
browser.find_element_by_xpath("/html/body/div[5]/div/div[1]\
    /form/div/div/table/tbody/tr[2]/td[3]/button/em").click()

# 相对路径查找 查找登录按钮上的文字元素
emt = browser.find_element_by_xpath("//button[@class='pn vm']/em").text
print(emt)

# 暂停3秒
sleep(3)
# 浏览器关闭
browser.quit()