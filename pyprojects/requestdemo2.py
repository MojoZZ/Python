import re,requests,time

i = 1
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
for number in range(0, 226, 25):
    r1 = requests.get('https://movie.douban.com/top250?start='+str(number), headers=headers)
    # print(r1.text)
    time.sleep(1)
    url_list = re.findall('src="(.*\.jpg)',r1.text)
    for url in url_list:
        r = requests.get(url,headers=headers)
        f1 = open('c:/test/'+str(i)+'.jpg','wb')
        f1.write(r.content)
        f1.close()
        i+=1
