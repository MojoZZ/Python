from selenium import webdriver
from time import sleep,strftime

browser = webdriver.Firefox()
browser.get("http://127.0.0.1/upload/forum.php")
# browser.set_window_size(400,600)
browser.implicitly_wait(5)
sleep(1)

# js = "document.getElementById('ls_username').value='admin'"
# js = "window.scrollTo(100,300)"
js = "function aa(){alert(111)} aa();"
browser.execute_script(js)

sleep(3)
browser.quit()