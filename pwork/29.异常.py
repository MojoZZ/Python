# 异常
# 异常处理
#	try:
#		代码块（可能出现的错误的语句）
#	except 异常类型1 as 异常名1:
#		代码块（出现错误以后的处理方式）
#	except 异常类型2 as 异常名2:
#		代码块（出现错误以后的处理方式）
#	......
#	except Exception as e:
#		代码块
#	else:
#		代码块（没有出错要执行的语句）
#	finally:
#		代码块
#
#	try 是必须的，else可有可无
#	except和finally至少有一个

# 异常的传播
# 	当在函数中异常时，如果在函数中对异常进行了处理，则异常不会继续传播
#	若没有处理，则继续向函数的调用处传播

# 抛出异常：使用raise语句抛出异常
# 自定义异常类


# try:
# 	print(10/0)
# except:
# 	print('除数不能为0')
# else:
# 	print('继续执行程序')

# print('执行结束')





def fn():
	try:
		print('hello fn')
		# print(10/0)
		1 + 'hello'

	# 如果except后不跟任何的内容，则此时会捕获所有的异常
	# 若后面跟了一个异常类型，那么只会捕获该类型的异常
	# except 可以写多个
	except NameError:
		print('出现NameError。。。')
	except ZeroDivisionError:
		print('出现ZeroDivisionError。。。')
	# 只写一个except相当于except:Exception
	# Exception是所有异常的父类
	except Exception as e:
		# 打印异常信息
		# unsupported operand type(s) for +: 'int' and 'str' 
		# <class 'TypeError'>
		print(e, type(e))
		print('出现了未知异常。。。')
	# 该代码块总会执行
	finally:
		print('finally')


def fn2():
	print('hello fn2')
	fn()

def fn3():
	print('hello fn2')
	fn2()


# fn3()



# 自定义异常类
class MyError(Exception):
	pass



def add(a,b):
	# 如果a或者b中有负数，就向调用处抛出异常
	if a < 0 or b < 0:
		raise MyError('自定义异常')
	r = a + b
	return r


print(add(123,-456))
