# 一个标准的类的结构
class Person :

	# 公共的属性

	# 在类中可以定义一些特殊方法（魔术方法）
	# 特殊方法都是：__方法名__这种名称
	# 特殊方法不需要自己调用， 会在特殊的时刻自动调用

	# init方法每次创建实例的时候会执行
	# 调用类创建对象时，类后面的所有参数都会依次传递到init中
	def __init__(self, name) :
		# print('..init...')
		self.name = name


	# 自定义的方法
	def say_hello(self):
		print('hello, %s'%self.name)



# 创建对象
zhangsan = Person('张三')
lisi = Person('李四')

# print(zhangsan.name)
# lisi.say_hello()






# 自定义一个Dog的类
class Dog :

	def __init__(self, name, age, gender, weight) :
		self.name = name
		self.age = age
		self.gender = gender
		self.weight = weight


	def barking(self) :
		print(f'{self.name} is wangwang...')

	def biting(self) :
		print(f'{self.name} is biting...')

	def running(self) :
		print(f'{self.name} is running...')



mojo = Dog('mojo', 3, 'male', '15kg')
# 可以通过 对象.属性 的方式来修改属性的值，这种方式导致对象中的属性可以随意修改，这种方式不安全
# mojo.name = '小黑'
mojo.running()