##流程控制
#包括：
#	条件判断（if语句）
#		if 条件表达式 : 语句
#	或	if 条件表达式 : 
#			代码块
#		默认情况下，if语句只会控制紧随其后的那条语句；若有多个，可以使用代码块（换行缩进）
#		缩进一般用tab或者空格（4个空格）
#		注：Python是缩进严格的语言
#	循环

num = 20
#这里只有一个语句
#if num > 10 : print('hello')

#这里是代码块的形式，换行并且缩进
if num > 10 :
	print('hello')
	print('world')

#这里不属于代码块
print('总会打印')



##输入函数inpt()
#	返回值永远是一个字符串
# username = input('输入用户名:')
# print('username=', username)

# if username == 'admin' : 
# 	print('welcome admin!')

# 可以用于阻止程序结束
# input('按回车结束程序...')


# if-else语句
# 语法
#	if 条件表达式:
#		代码块
#	else :
#		代码块
# age = input('请输入你的年龄:')
# age = int(age)
# if age > 17 :
# 	print('你可以喝酒了')
# else :
# 	print('小朋友是不是有很多问号？你只能喝养乐多。')



# if-elif-else语句
#	if 条件表达式 :
#		代码块
#	elif 条件表达式 :
#		代码块
#	elif 条件表达式 :
#		代码块
#	else :
#		代码块
salary = input('亲，请输入你的月薪资：')
salary = int(salary)

if salary > 50000 :
	print('虽然不能住在故宫旁边，但应该在中心地带吧')
elif salary > 40000 :
	print('三环拥有一席之地')
elif salary > 30000 :
	print('退一环海阔天空')
elif salary > 20000 : 
	print('啊~~啊~~，五环....')
else :
	print('我还不想秃头！')


