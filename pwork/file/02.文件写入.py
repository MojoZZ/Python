file_name = 'demo1.txt'


# 使用open()打开的文件时必须要指定打开文件所需要做的操作（读、写、追加）
# 如果不指定操作类型，则默认为读取文件
# r 只读
# w 可写，如果文件不存在会创建文件，如果文件存在则会截断文件（删除文件中原来的所有内容）
# a 追加，如果文件不存在会创建文件，如果文件存在则会向文件中追加内容
# x 用来新建文件，如果文件不存在则创建，存在则报错
# + 为操作符增加功能，如
#	r+ 可读可写，但是文件不存在会报错
#	w+ 可写可读
#	a+ 可追加可读
# with open(file_name, mode='w', encoding='utf-8') as file_obj:
with open(file_name, mode='x', encoding='utf-8') as file_obj:
	# write()向文件中写入内容
	# 如果操作的时一个文本文件的话，则write()需要传递一个字字符串作为参数
	# 可以多次写入
	# 返回写入内容字符的个数
	file_obj.write('hello mojo,how are you!')
	file_obj.write('hello mojo,how are you!\n')
	file_obj.write('hello mojo,how are you!')
	file_obj.write(str(123))
	r = file_obj.write(str(123456))
	print(r)