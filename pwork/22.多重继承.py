class A(object) :

	def test1(self):
		print('AAA')


class B(object) :

	def test1(self):
		print('B中的test2')
	
	def test2(self):
		print('BBB')


# 多重继承，Python支持多重继承
# 在开发中没有特殊情况，应该尽量避免使用多重继承
class C(B, A) :
	
	pass





# 类名.__bases__这个属性可以用来获取当前类的所有父类
# 是个元祖 ： (<class '__main__.B'>, <class '__main__.A'>)
# print(C.__bases__)


c = C()
# 若存在多重继承，若类中存在方法重名的，则会优先调用第一个类中的方法，这里也就是B
c.test1()	#B中的test2
c.test2()