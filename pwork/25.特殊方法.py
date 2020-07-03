# 特殊方法
# 在类中可以定义一些特殊方法（魔术方法）
	# 特殊方法都是：__方法名__这种名称
	# 特殊方法不需要自己调用， 会在特殊的时刻自动调用

class Person :

	# init方法每次创建实例的时候会执行
	# 调用类创建对象时，类后面的所有参数都会依次传递到init中
	def __init__(self, name, age) :
		# print('..init...')
		self.name = name
		self.age = age

	# str会在尝试将对象转换为字符串时调用
	def __str__(self):
		return 'Person [name=%s,age=%d]' %(self.name,self.age)

	# repr：在对当前对象使用repr()方法时调用
	# 指定对象在交互模式中直接输出的结果
	def __repr__(self):
		return 'hello'

	# object.__lt__(self, other)
	# object.__le__(self, other)
	# object.__eq__(self, other)
	# object.__ne__(self, other)
	# object.__gt__(self, other)
	# object.__ge__(self, other)

	# 对象做大于比较时调用，返回值将作为结果
	def __gt__(self,other):
		return self.age > other.age

	# bool方法
	def __bool__(self):
		# return self.name != None
		return self.age > 18

	# 一些列运算，都可以自己重写
	# object.__add__(self, other)
	# object.__sub__(self, other)
	# object.__mul__(self, other)
	# object.__matmul__(self, other)
	# object.__truediv__(self, other)
	# object.__floordiv__(self, other)
	# object.__mod__(self, other)
	# object.__divmod__(self, other)
	# object.__pow__(self, other[, modulo])
	# object.__lshift__(self, other)
	# object.__rshift__(self, other)
	# object.__and__(self, other)
	# object.__xor__(self, other)
	# object.__or__(self, other)

	# 自定义的方法
	def say_hello(self):
		print('hello, %s'%self.name)




p1 = Person('Mojo',18)
p2 = Person('Wendy',20)

# <__main__.Person object at 0x038EB0E8>
# 调用了__str__()
# print(p1)
# 调用str方法也会调用该方法
# print(str(p1))

# 调用repr方法
# print(repr(p1))

# 调用__gt__方法
# print(p1 > p2)

# 调用bool方法
# print(bool(p1))

# if p1:
# 	print(p1.name,'已经成年了')
# else:
# 	print(p1.name,'未成年')



