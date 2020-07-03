# 注意文件的目录分隔符
# 当前目录下的文件夹
# 文件分隔符可以使用/或者\\也或者使用原始字符串r
# file_name = 'ff1/demo11.txt'
# 原始字符串的使用，防止\解释成转义字符
# file_name = r'ff1\demo11.txt'
# 上级目录
# file_name = '../ff2/demo22.txt'
# 绝对路径
# file_name = r'C:\Users\Administrator\Desktop\demo33.txt'
file_name = "./file/a.txt"

# 打开一个文件，默认只读，文件不存在报错；若是w或者a，文件不存在不会报错，会创建文件
file_obj = open(file_name)
# print(file_obj)
# 读取所有内容
# content = file_obj.read()
# 按字节读取
content = file_obj.read(2)
print(content)
# 移动文件指针
file_obj.seek(0)
content = file_obj.read(2)
print(content)

# 关闭文件 文件句柄泄漏
file_obj.close()

