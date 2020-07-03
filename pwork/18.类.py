#Python：面向对象的语言	Object
#对象实际上就是一个容器，就是内存中专门用来存储指定数据的一块区域
#有可变对象和不可变对象
#对象的结构
#	id：对象标识，由解析器生成的，在Cpython中，id就是对象的内存地址
#		标识对象的唯一性
#		可以通过id()函数来查看对象的id
#	type：对象类型，决定了对象有哪些功能
#		Python是强类型语言，对象一旦创建不能修改
#	value：对象数据
#		可变对象的数据可修改，不可变对象的数据不可修改


#Python中有一些内置的类 ，小写的

a = int(10) # 创建一个int类的实例
s = str('hello') # 创建一个str类的实例


## 自定义类
#定义一个简单的类，使用关键字class
#class 雷鸣([父类]) :
#	pass

# 这里为一个最简单的类
class MyClass() :
	pass

# <class '__main__.MyClass'>
# print(MyClass)
# 16091016 <class 'type'>
# print(id(MyClass), type(MyClass))

# 也可以重新给MyClass赋值,相当于给变量重新赋值，这里重新赋值为字符串
# MyClass = 'hello'
# print(MyClass);


# 使用MyClass来创建对象
mc = MyClass()
# <__main__.MyClass object at 0x01391F88>
# <class '__main__.MyClass'>
# print(mc, type(mc))


# 用来检查一个对象是否是一个类的实例
# 如果这个类是这个对象的父类，也会返回True
# 所有的对象都是object的实例
r = isinstance(mc, MyClass)
# r = isinstance(mc, str)
# print(r)
# print(isinstance(print, object))	# True
# print(isinstance(mc, object))	# True




## 对象的创建流程
# 此时创建的MyClass对象都是空对象
# 可以用对象添加属性，但是只在当前对象中
# 一般不建议在对象中肆意添加属性，应该统一抽象到类中
mc = MyClass()
mc1 = MyClass()

mc.name = 'mojo'
# print(mc.name)
# print(mc1.name) # 这里报错






class Person :
	# 可以在类中定义变量和属性（所有的实例都可以调用到公共的属性和变量）
	# a = 10
	# b = 20
	name = 'mojo'	#类属性

	# 类中定义的函数成为方法
	# 方法中的每次调用，解析器都会自动传递一个参数
	# 第一个参数时调用方法的对象本身，一般命名为self
	def say_hello(self) :
		print('你好，我是 %s' %self.name)


zhangsan = Person()
lisi = Person()

# print(zhangsan.name)

zhangsan.name = '张三'
lisi.name = '李四'

# 调用方法：对象.方法名()
# 方法调用和函数调用的区别：
#	1.函数调用：有几个参数传几个参数
#	2.方法调用：调用时会默认传递一个参数，所以要求方法中要有一个形参
# lisi.say_hello()
# zhangsan.say_hello()





# 类的方法和属性
class A(object):
	# 类属性
	count = 0
	
	'''
		self这边是实例属性
		只能通过实例对象来访问和修改，类对象无法访问和修改
	'''
	def __init__(self):
		self.name = 'mojo'

	'''
		 实例方法
		 在类中定义，以self为第一个参数的方法
		 实例方法在调用时，Python会将调用对象作为self传入
		 实例方法可以实例和类对象调用
			类调用：不会自动传递self，但需要手动传递参数
			实例调用：自动传递self
	'''
	def test(self):
		print('test，这是一个实例方法。。。', self)


	'''
		类方法
		在类内部使用@classmethod来修饰的方法属于类方法
		类方法的第一个参数是cls，也是自动传递，cls就是当前的类对象
		类方法可以通过类对象和实例对象调用，主要是参数不一样
	'''
	@classmethod
	def test_2(cls):
		print('test_2，这是一个类方法。。。')
		print(cls.count)


	'''
		静态方法
		在类中使用@staticmethod来修饰的方法属于静态方法
		基本上是一个和当前类无关的方法，它只是一个保存到当前类中的方法
		一般都是一些工具方法
		静态方法可以不用参数
		可以通过类对象和实例对象调用
	'''
	@staticmethod
	def test_3():
		print('test_3,这是一个静态方法')


a = A()

# 实例属性
# 在对象中添加了一个count属性，是实例属性，不影响类中值
# a.count = 10
# 这个时候是修改了类的属性	
# A.count = 20	
# print(a.count)
# print(A.count)

# print(a.name)
#这里报错，类访问板锉
# print(A.name)

# 实例方法调用
# a.test()
# A.test(a)


# 类方法
# A.test_2()
# a.test_2()


# 静态方法
A.test_3()
a.test_3()

# help(A)




