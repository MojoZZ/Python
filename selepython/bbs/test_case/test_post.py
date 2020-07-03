import unittest
from selenium import webdriver
from time import sleep, strftime
from selenium.webdriver import ActionChains

from bbs.mymodule.login import login


class PostTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        browser = self.browser
        browser.maximize_window()
        browser.implicitly_wait(5)
        browser.get("http://127.0.0.1/upload/forum.php")
        # 登录
        # browser.find_element_by_id("ls_username").send_keys("admin")
        # browser.find_element_by_id("ls_password").send_keys("123456")
        # browser.find_element_by_css_selector("button.pn.vm").click()
        login(browser, "admin", "123456")
        sleep(1)
        # 点击默认版块
        browser.find_element_by_link_text("默认版块").click()

    def test_post1(self):
        browser = self.browser
        ftime = strftime("%Y%m%d%H%M%S")
        title = f"这是标题{ftime}"
        browser.find_element_by_id("subject").send_keys(title)
        browser.find_element_by_id("fastpostmessage").send_keys(f"这是内容{ftime}")
        browser.find_element_by_id("fastpostsubmit").click()
        real_title = browser.find_element_by_id("thread_subject").text
        self.assertEqual(title, real_title)

    def test_post2(self):
        browser = self.browser
        ele1 = browser.find_element_by_id("newspecial")
        ele2 = browser.find_element_by_xpath("//ul[@id='newspecial_menu']/li/a[text()='发表帖子']")
        ActionChains(browser).move_to_element(ele1).click(ele2).perform()
        sleep(1)
        ftime = strftime("%Y%m%d%H%M%S")
        title = f"这是标题{ftime}"
        browser.find_element_by_id("subject").send_keys(title)
        browser.switch_to.frame("e_iframe")
        browser.find_element_by_tag_name("body").send_keys(f"这是内容{ftime}")
        # sleep(1)
        browser.switch_to.default_content()
        browser.find_element_by_css_selector("#postsubmit[type='submit']").click()

        real_title = browser.find_element_by_id("thread_subject").text
        self.assertEqual(title, real_title)

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
