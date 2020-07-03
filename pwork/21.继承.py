# 继承：面向对象的三大特性之一
# 使用继承保证了对象的可扩展性
# 父类
class Animal :

	def run(self) :
		print('animal is running...');

	def sleep(self):
		print('animal is sleeping...')




# 子类
# 括号中为集成的父类
# 若创建类的时候没有写继承的父类，则默认为object
# object为所有对象的父类
class Dog(Animal) :

	'''
		override：重写或者覆盖了父类中的run方法
	'''
	def run(self) :
		print('Dog is running...')

	def bark(self):
		print('Dog is barking....')



# 子类
class Hashiqi(Dog) :

	def chai_jia(self) :
		print('对，没错，我是哈士奇，我正在拆家！')





d = Dog()
# 调用本类中的方法
# d.bark()
# 子类中重写了父类中方法，则调用子类自己中的方法
# d.run()
# 调用父类中方法
# d.sleep()

h = Hashiqi()
# h.chaijia()
# h.bark()


# r = isinstance(d, Dog) # True
# r = isinstance(d, Animal) # True
# print(r)

# 检查是否为子类
# r = issubclass(Person, object)	#True
# print(r)





# 当我们调用一个对象的方法时
# 会优先去当前对象中寻找，没有，则到父类
class A(object):

	def __init__(self, name) :
		self._name = name

	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, name):
		self._name = name

	def test_a(self) :
		print('AAA')


class B(A):

	def __init__(self, name, age) :
		# self._name = name
		# self._age = age
		# super()可以用来获取当前类的父类
		super().__init__(name)
		self._age = age

	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, name):
		self._name = name

	@property
	def age(self):
		return self._age
	
	@age.setter
	def age(self, age):
		self._age = age
	
	def test_b(self) :
		print('BBB')



b = B('小红', 18)
print(b.name, b.age)