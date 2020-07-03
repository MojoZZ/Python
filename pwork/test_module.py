# print('我是test_module模块')
# print(__name__)

# 定义属性
a = 10
b = 20
# 模块中的私有属性
# 在变量名前面加上_
# 模块中的其他对象也一样
_c = 30

# 定义方法
def test_add(a,b):
	return a+b

def test():
	print('test')

# 定义类
class Person:

	def __init__(self,name):
		self._name = name

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name




# 编写的测试代码
# 当模块被其他模块引入时，不需要执行
# 所以可以加个判断
if __name__ == '__main__':
	print('sdsdsds')
	test()