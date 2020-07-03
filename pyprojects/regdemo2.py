import re

# 读文件
f = open("./file/maoyan.txt", "r")
content = f.read()
# print(content)
# pattern = re.compile('https.*\.jpg')
# pattern = re.compile('src="(.*\.jpg)')
# 直接使用括号中的内容
pattern = re.compile("src=\"(.*\.jpg)")

url_list = pattern.findall(content)

f.close()

for url in url_list:
    print(url)
