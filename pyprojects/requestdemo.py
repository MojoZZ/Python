import requests,time,re

# r = requests.get("http://163.com")
# 响应的状态码
# print(r.status_code)
# 文本
# print(r.text)

# 添加请求头
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
# r = requests.get("https://maoyan.com/films/1277939", headers=headers)
# print(r.text)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
# r = requests.get("https://p0.meituan.net/moviemachine/b2c5c74d33e45745fd3462e44b3698e18336620.jpg@464w_644h_1e_1c", headers=headers)
# f = open("file/001.jpg","wb")
# f.write(r.content)
# f.close()

# 抓取图片
# f = open("./file/maoyan.txt", "r")
# content = f.read()
# pattern = re.compile("src=\"(.*\.jpg)")
# url_list = pattern.findall(content)
# f.close()
#
# for url in url_list:
#
#     r = requests.get(url, headers=headers)
#     file_name = "file/"+time.strftime("%Y%m%d%H%M%S")+".jpg"
#     f1 = open(file_name, "wb")
#     f1.write(r.content)
#     f1.close()





# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
# f = open('file/maoyan.txt')
# # print(f.read())
# url_list = re.findall('src="(.*\.jpg)',f.read())
# i= 1
# for url in url_list:
#     r = requests.get(url,headers=headers)
#     f1 = open('file/my'+str(i)+'.jpg','wb')
#     f1.write(r.content)
#     f1.close()
#     i+=1
# f.close()





