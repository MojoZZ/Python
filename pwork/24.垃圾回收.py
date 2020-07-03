## 垃圾回收
# 	程序运行过程中产生的垃圾会影响到程序运行的性能
# 	python中有自动的垃圾回收机制，会自动将这些没有被引用的对象删除

# 程序中没有被引用的对象为垃圾
# 

class A:

	def __init__(self):
		self.name = 'A'

	# del是一个特殊方法，会在对象被垃圾回收前调用
	def __del__(self):
		print('A()对象被删除', self)


a = A()
b = a
print(a.name)

# 将a设置为None，此时没有任何的变量对A进行引用，它就变成垃圾
# a = None
# b = None

# 使用del也可以
# del a
# del b


# 按了回车键，程序结束，也会自动回收垃圾对象
input('按回车键结束...')