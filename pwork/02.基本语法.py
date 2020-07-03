# 每行不要字符过长（规范建议为80个字符）
# 若过长，可以使用\结尾表示换行
print('111111111111111111111111111111111111111111111111111111111111111111111111111111111')
print('aaa\
	bbb\
	ccc')
print(1234)
# 这是一个单行注释
print('abc') 
#print打印语句默认输出换行，若不想换行，可以添加参数end=''
print('11',end='') 
print('22') 

'''
这是多行注释
'''

"""
这也是多行注释
"""
a = 123
a = True
a = 'hello'
print(a)


a = 10
b = 'hello'
c = True
print(a)
print(b)
print(c)

#同时为多个变量赋值
a = b = c = 1
print(a,b,c)
#可以为多个对象指定多个变量
a, b, c = 1, 2.5, "Mojo"
print(a,b,c)
