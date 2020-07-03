'''
登录方法
browser--浏览器对象
username--用户名
password--密码
'''
def login(browser, username, password):
    browser.find_element_by_id("ls_username").send_keys(username)
    browser.find_element_by_id("ls_password").send_keys(password)
    browser.find_element_by_css_selector("button.pn.vm").click()