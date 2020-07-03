# 多态是面向对象的三大特性之一
# 使用多态保证了程序的灵活性
class A:

	def __init__(self,name):
		self._name = name

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self,name):
		self._name = name
	


class B:

	def __init__(self,name):
		self._name = name

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self,name):
		self._name = name




a = A('AA')
b = B('BB')

# obj可以是任意类型，只要有name属性
def say_hello(obj):
	print('hello %s'%obj.name)


# say_hello(a)
# say_hello(b)







class Animal :

	def __init__(self, name, age):
		self._name = name
		self._age = age

	@property
	def name(self):
		return self._name

	@property
	def age(self):
		return self._age

	@name.setter
	def name(self,name):
		self._name = name
	
	@age.setter
	def name(self,age):
		self._age = age


	def run(self):
		print('animal is running...')


	def eat(self):
		print('animal is eatting...')

	def shout(self):
		print('animal is shoutting...')




class Dog(Animal):

	def __init__(self, name, age):
		super().__init__(name,age)

	def shout(self):
		print('汪汪汪...')

	def eat(self):
		print('喵，我的磨牙棒呢？')



class Cat(Animal):

	def __init__(self, name, age):
		super().__init__(name,age)

	def shout(self):
		print('喵~~~~~~')

	def eat(self):
		print('喵，我的小鱼干呢？')





# 所谓的多态，会结合继承来一起呈现
# 属于同一个父类，但是也会表现出不同的形态和动作
def show_animal_work(animal):
	# if isinstance(animal, Animal) :
		animal.eat()
		animal.shout()

	# else:
		# print('你又不是Animal！')



dog = Dog('旺财', 4)
cat = Cat('咪咪', 5)


show_animal_work(dog)
show_animal_work(cat)
# show_animal_work(123)