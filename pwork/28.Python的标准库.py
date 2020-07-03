# 开箱即用
# Python提供了一个模块的标准库
# 在标准库中，有很多强大的模块我们可以直接使用


# sys模块：提供了一些变量和函数，可以获取到Python解析器的信息
# pprint模块，可以给打印的内容进行简单的格式化
# os模块可以对操作系统进行访问

import sys
import pprint
import os


# print(sys)
# sys.argv 代码执行时，命令行运行时的参数
# ['28.Python的标准库.py']
# 命令函执行该py文件： python 28.Python的标准库.py 参数1 参数2 参数3...
# print(sys.argv)


# sys.modules
# 获取当前程序中引入的所有模块
# 是一个字典，key是模块名，value是模块对象
# pprint.pprint(sys.modules)


# sys.path
# 是一个列表，是一个模块的搜索路劲
# ['E:\\Zooey\\学习\\python\\pwork',
#  'C:\\Program Files (x86)\\Python\\Python38\\python38.zip',
#  'C:\\Program Files (x86)\\Python\\Python38\\DLLs',
#  'C:\\Program Files (x86)\\Python\\Python38\\lib',
#  'C:\\Program Files (x86)\\Python\\Python38',
#  'C:\\Program Files (x86)\\Python\\Python38\\lib\\site-packages']
# pprint.pprint(sys.path)


# sys.platform-运行的平台
# 'win32'
# print(sys.platform)


# sys.exit()-退出程序
# sys.exit()
# sys.exit('程序出现异常，请联系管理员')


# os.environ
# pprint.pprint(os.environ)
# pprint.pprint(os.environ['path'])


# os.system()-可以执行操作系统的命令
# os.system('notepad')