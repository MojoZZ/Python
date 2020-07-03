# 通过Python程序来对计算机中的各种文件进行操作
# I/O

# 文件操作步骤：
#	1.打开文件
#	2.读写文件
#	3.关闭文件


# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# 使用open函数打开一个文件
# 参数：
#	file-要打开的文件（路径）
# 返回值：
#	返回一个对象，这个对象代表了当前打开的文件

# 以下是几种文件在不同位置的情况
# 当前目录
file_name = 'demo.txt'
# 当前目录下的文件夹
# 文件分隔符可以使用/或者\\也或者使用原始字符串r
# file_name = 'ff1/demo11.txt'
# 原始字符串的使用，防止\解释成转义字符
# file_name = r'ff1\demo11.txt'
# 上级目录
# file_name = '../ff2/demo22.txt'
# 绝对路径
# file_name = r'C:\Users\Administrator\Desktop\demo33.txt'


# 获取文件对象
file_obj = open(file_name)
# <_io.TextIOWrapper name='demo.txt' mode='r' encoding='cp936'>
# print(file_obj)


# 通过文件对象来进行各种操作
# read()方法，读取文件中的内容
content = file_obj.read()
# print(content)

# 关闭文件
file_obj.close()




# with ... as 语句
# 使用open()打开的文件时必须要指定打开文件所需要做的操作（读、写、追加）
# 如果不指定操作类型，则默认为读取文件
# 文件只能在with中使用，with结束，文件会自动关闭
# file_name = 'ff1/demo11.txt'
# with open(file_name) as file_obj:
# 	print(file_obj.read())


# with ... as 优化下
# file_name = 'ff1/demo11.txt'
# try:
# 	with open(file_name) as file_obj:
# 		print(file_obj.read())
# except FileNotFoundError:
# 	print(f'{file_name}文件不存在')





# 含有中文的文件读取
# 调用open函数打开一个文件，可以将文件分为两种类型
# 1.纯文本文件（使用utf-8等编码编写的文件）
# 2.二进制文件（图片、mp3、ppt等）
# open打开文件默认是已纯文本方式来打开文件的，但是open的编码默认为None

# file_name = 'demo_ch.txt'
# try:
# 	with open(file_name,encoding='utf-8') as file_obj:
# 		# 直接调用read会全部读取文件中的内容
# 		# read()就默认为read(-1)：读取所有
# 		# read(size)：读取指定size长度的内容
# 		chunk = 50
# 		while True:
# 			content = file_obj.read(chunk)
# 			if not content:
# 				break

# 			print(content,end='')
# except:
# 	print('读取文件出错')





import pprint
# readline()方法--一行一行读取
# readlines()方法--一行一行读取，读取的内容会以列表的形式返回
file_name = 'demo.txt'
try:
	with open(file_name,encoding='utf-8') as file_obj:
		# readline
		# while True:
		# 	content = file_obj.readline()
		# 	if not content:
		# 		break

		# 	print(content,end='')


		# readlines
		r = file_obj.readlines()
		pprint.pprint(r)
		pprint.pprint(r[0])


		# for循环
		# for c in file_obj:
		# 	print(c)
except:
	print('读取文件出错')






# 二进制文件读取
# t 读取文本文件（默认值）
# b 读取二进制文件
file_name = r'C:\Users\Administrator\Desktop\五月天-拥抱.mp3'
with open(file_name, 'rb') as file_obj:
	# 这里表示字节
	# print(file_obj.read(100))

	new_file_name = 'aa.mp3'

	with open(new_file_name, 'wb') as new_file_obj:
		# 100K
		chunk = 1024 * 100
		while True:

			content = file_obj.read(chunk)

			if not content:
				break

			new_file_obj.write(content)