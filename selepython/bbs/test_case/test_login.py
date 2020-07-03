import unittest
from selenium import webdriver


# 多个测试用例时，执行时放在类上面或者main方法代码块的地方，
# 若放在某个方法后面则只执行这个方法
# 执行顺序：setUp--测试用例1--tearDown setUp--测试用例2--tearDown
from bbs.mymodule.login import login


class LoginTestCase(unittest.TestCase):

    # 前置条件
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        self.browser.implicitly_wait(5)
        self.browser.get("http://127.0.0.1/upload/forum.php")

    # 测试步骤
    # 管理员登录
    def test_login1(self):
        browser = self.browser
        # browser.find_element_by_id("ls_username").send_keys("admin")
        # browser.find_element_by_id("ls_password").send_keys("123456")
        # browser.find_element_by_css_selector("button.pn.vm").click()
        login(browser, "admin", "123456")

        # 获取登录后的用户名
        user = browser.find_element_by_xpath("//a[@title='访问我的空间']").text
        # 断言
        self.assertEqual("admin", user)

    # 普通用户登录
    def test_login2(self):
        browser = self.browser
        # browser.find_element_by_id("ls_username").send_keys("test")
        # browser.find_element_by_id("ls_password").send_keys("123456")
        # browser.find_element_by_css_selector("button.pn.vm").click()
        login(browser, "test", "123456")
        # 获取登录后的用户名
        user = browser.find_element_by_xpath("//a[@title='访问我的空间']").text
        # 断言
        self.assertEqual("test", user)

    # 还原
    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()

