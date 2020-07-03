# 封装是面向对象的三大特性之一
# 封装指的时隐藏对象中一些不希望被外部所访问到的属性或方法
# 如何隐藏一个对象中的属性
# 	将对象的属性名，修改为一个外部不知道的名字
# 如何获取（修改）对象中的属性
#	需要一个getter和setter方法供外部访问属性
# 使用封装增加了数据的安全性


class Dog :

	def __init__(self, name, age) :
		self.hidden_name = name
		self.hidden_age = age

	# 修改属性值
	def set_name(self, name) :
		self.hidden_name = name

	# 可以对一些数据进行检查，增强了数据的合理性，或者做一些操作
	def set_age(self, age) :
		if age > 0 :
			self.hidden_age = age

	# 获取属性值
	def get_name(self) :
		return self.hidden_name

	def get_age(self) :
		return self.hidden_age

	def running(self) :
		print(f'{self.hidden_name} is running...')



mojo = Dog('mojo', 3)
# mojo.running()

# print(mojo.get_name())

mojo.set_name('旺财')
# print(mojo.get_name())

mojo.set_age(-10)
# print(mojo.get_age())	# 这里还是3










# 可以为对象的属性使用双下划线开头，__xx
# 双下划线开头的属性，是对象的隐藏属性，隐藏属性只能在类的内部访问，对象不能访问
# 隐藏属性是Python自动为属性修改了一个名字，改为 _类名_属性名
class Rectangle :

	def __init__(self, width, height):
		self.__width = width
		self.__height = height


	def get_width(self) :
		return self.__width

	def get_height(self) :
		return self.__height

	def set_width(self, width):
		self.__width = width

	def set_height(self, height):
		self.__height = height

	def calc_area(self) :
		return self.__height * self.__width




r = Rectangle(5, 2)
# r.__width = 10 # 不能修改，面积任然为10
# print(r.calc_area())

# print(r._Rectangle_width)

# r.set_height(10)
# r.set_width(20)
# print(r.calc_area())






# 这里使用 _ 开头的属性
# 表示这里的属性是私有属性，没有特殊需要不要修改私有属性
# class Person :

# 	def __init__(self, name):
# 		self._name = name

# 	def get_name(self) :
# 		return self._name

# 	def set_name(self, name) :
# 		self._name = name



# p = Person('Mojo')
# print(p._name)







# property的使用
class Person :

	def __init__(self, name, age):
		self._name = name
		self._age = age

	# property装饰器，用来将一个get方法转换为对象的属性
	# 方法名和属性名要一样
	# 在使用了装饰器后，若对象的属性只有get没有set，则不允许修改属性的值
	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name) :
		self._name = name

	@property
	def age(self) :
		return self._age

	@age.setter
	def age(self, age) :
		self._age = age



p = Person('Mojo', 20)

# 调用get方法
# 在使用了装饰器后，调用get方法为以下方式p.name
# 而不是原来的p.get_name()
print(p.name)

# 调用set方法
p.name = 'Zooey'
print(p.name)