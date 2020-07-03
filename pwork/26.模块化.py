# 模块化：将程序分解为一个一个小的模块，编写成多个文件
#	1.方便开发和维护
#	2.方便复用

# 	在Python中一个py文件就是一个模块
#	模块化名要符合标识符的命名规范
#	引入：
#		import 模块名（不需要加上.py）
#		import 模块名 as test
#		from 模块名 import 变量,变量...
#		from 模块名 import 变量 as 别名
#		from test_module import *（引入模块中的全部内容，除去模块中的私有对象）
#
#		import 可以放在程序的任意位置，但是一般情况下，都放在程序的开头部分
#		在每一个模块内部都有一个__name__属性，通过这个属性可以获取这个模块的名字
#		__name__属性值为__main__模块是主模块，一个程序中只会有一个主模块，是直接通过Python执行的模块


# 引入
# import test_module
# 别名引入
# import test_module as test
# 部分引入
# from test_module import Person,test_add
# 引入全部，模块过大，一般不建议使用
# 如果有重名的情况，模块中的内容会覆盖当前模块中的内容
from test_module import *
# from test_module import Person,test_add as mtest



# 打印模块信息
# <module 'test_module' from 'E:\\Zooey\\学习\\python\\pwork\\test_module.py'>
# print(test_module)
# print(test.__name__)
# __main__
# print(__name__)

# 调用模块中的属性
# print(test.a, test.b)

# 调用模块中的方法
# r = test.test_add(10,20)
# print(r)

# test.test()

# p = test.Person('Mojo')
# print(p.name)

# 直接使用
# p = Person('Mojo')
# print(p.name)

# 模块中变量的别名使用
# r = mtest(10,20)
# print(r)

# 访问不到
# print(test._c)

