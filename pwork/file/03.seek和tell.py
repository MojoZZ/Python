file_name = 'demo.txt'
with open(file_name,'rb') as file_obj:
	# print(file_obj.read(100))

	# seek()可以修改当前读取位置
	# 两个参数
	# 1.要切换到的位置
	# 2.计算位置的方式
	#		0-从头计算
	#		1-当前位置
	#		2-从最后位置开始
	file_obj.seek(55)
	file_obj.seek(80,0)
	file_obj.seek(70,1)
	file_obj.seek(-1,2)

	# 从55后面开始读取
	print(file_obj.read(10))

	# tell()-当前读取的位置
	print('当前读取到了-->',file_obj.tell())



# 文本文件的读取会发生问题，文本文件中若有中文字符会发生截取的错误
with open('demo_ch.txt','rt',encoding='utf-8') as file_obj:

	file_obj.seek(11)

	# 从55后面开始读取
	print(file_obj.read())

	# tell()-当前读取的位置
	print('当前读取到了-->',file_obj.tell())