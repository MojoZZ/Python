import os
from pprint import pprint

# os.listdir()-获取指定目录的目录结构
# 需要一个路径作为参数，获取到该路径下的目录结构，默认路径为 . 当前目录
r = os.listdir()

# os.getcwd()-获取当前所在的目录
r = os.getcwd()

# os.chdir()-切换当前所在的目录
# os.chdir('..')
# os.chdir('c:/')

# os.mkdir()-创建目录
# os.mkdir('aa')

# os.rmdir()-删除目录
# os.rmdir('aa')

# 删除文件
# os.remove('aa.txt')

# os.rename('旧名字','新名字')
# 名字也可以是完整的路径名，这时相当于剪切文件
# os.rename('aa.txt','bb.txt')
# os.rename('aa.txt','C:\Users\Administrator\Desktop\bb.txt')
pprint(r)