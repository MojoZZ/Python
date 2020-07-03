# 高阶函数：高阶函数至少要符合以下两个特点中的一个
#	 -接收一个或多个函数作为参数
#	 -将函数错位返回值返回

def fn_odd(i) :
	'''
		验证是否为偶数
	'''
	if i % 2 == 0 :
		return True
	return False


def fn_com_five(i) :
	'''
		验证是否大于某个数值
	'''
	if i > 5 :
		return True
	return False


def my_fn1(func, lst) :

	'''
		可以将制定列表中的所有偶数取出，并返回一个新的列表

		参数：
			lst-要进行筛选的列表
	'''
	new_lst = []

	for n in lst :
		if func(n) :
			new_lst.append(n)


	return new_lst


# 这里传递一个函数作为参数
l = [1,2,3,4,5,6,7,8]
new_lst = my_fn1(fn_com_five, l)
# print(new_lst)


# filter()
#	可以从序列中过滤出符合条件的元素，保存到一个新的序列中
#	参数：
#		1.函数
#		2.需要过滤的序列
#	返回值：过滤后的系列

# print(list(filter(fn_com_five, l)))


# 匿名函数 lambda 函数表达式
#	lambda函数表达式专门用来创建一些简单的函数，是创建函数的另一种方式
#	语法：
#		lambda 参数列表 ： 返回值
#	匿名函数一般作为参数使用，其他地方一般不适用

# <function <lambda> at 0x0177A388>
# print(lambda a,b : a + b)

# 调用
# print((lambda a,b : a + b)(10,20))

# 也可以将匿名函数赋值给变量
lf = lambda a,b : a + b
# print(lf(23,45))

# 这里就可以用lambda传递
# print(list(filter(lambda i : i % 3 == 0, l)))


# map() 函数：可以对可迭代对象中的所有元素进行制定的操作，然后返回一个新的可迭代对象
r = map(lambda i : i + 1, l)
# print(list(r))


# sort()：对列表中的元素进行排序，默认比较元素的大小
#		也可以接收一个关键字参数，key-需要一个函数作为参数
l = ['bcc','bad','ee','ea','aa','fsd','g']
# l.sort()
# print(l)

# l.sort(key=len)
# print(l)

l = [2,5,6,'1',7,'3',3]
# l.sort(key=int)
# print(l)


# sorted()：可以对任意序列进行排序
#	不会影响原来的对象，而是返回一个新的对象
r = sorted(l,key=int)
# print(r)



# 闭包：将函数作为返回值返回
#	通过闭包可以创建一些只有当前函数能访问的变量
#	可以将一些私有的数据藏到闭包中

def my_fn() :

	a = 10

	# 内部函数
	def my_inner() :
		print('my_inner', a)

	return my_inner


# r此时为一个函数，是在my_fn内部定义的并不是全局函数
# 所以这个函数可以访问到my_fn函数内的变量
r = my_fn()
# <function my_fn.<locals>.my_inner at 0x0370A1D8>
# print(r)
# r()


# nums = [30,56,89,100]

# print(sum(nums) / len(nums))



# 形成闭包的条件：
#	1.函数嵌套
#	2.将内部函数作为返回值返回
#	3.内部函数必须使用外部函数的变量
def make_avg() :

	nums = []

	def avg(n) :
		nums.append(n)

		return sum(nums) / len(nums)

	return avg

avg = make_avg()

# print(avg(10))
# print(avg(20))
# print(avg(30))




# 装饰器
# 若对已经定义的函数进行一些修改
#	1.函数过多，修改麻烦
#	2.不方便后期维护
#	3.违反开闭原则（OCP-程序的设计要求对程序的扩展，要关闭对程序的修改）

def add(a, b) :
	r = a + b
	return r


def mul(a, b) :
	r = a * b
	return r

def pp() :
	print('this is pp')


# r = add(124,897)
# print(r)


def new_add(a, b) :
	print('开始计算...')
	r = add(a, b)
	print('计算结束...')
	return r


# print(new_add(10,45))


# 装饰器函数
# 一般使用@来对函数进行装饰
# 可以为一个函数设置多个装饰器函数
def decorator(func) :

	'''
		对其他函数进行扩展，对函数的执行开始和结束做个打印
	'''
	def new_fun(*args, **kwargs) :
		print('start...')
		# 调用被扩展的函数
		r = func(*args, **kwargs)
		print('end...')
		return r

	return new_fun



def decorator1(func) :

	'''
		对其他函数进行扩展，对函数的执行开始和结束做个打印
	'''
	def new_fun(*args, **kwargs) :
		print('decorator1 start...')
		# 调用被扩展的函数
		r = func(*args, **kwargs)
		print('decorator1 end...')
		return r

	return new_fun



# f = decorator(add)
# r = f(123,234)
# print(r)

# f = decorator(pp)
# f()


# 一般都是这么使用
@decorator
@decorator1
def say_hello() :
	print('hello')


say_hello()




