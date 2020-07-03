# 包：当模块中的代码过多时，或者一个模块需要被分解成多个模块式可以使用包
# 普通模块是个文件，包是文件夹，也要符合标识符规范
#	包中必须要一个一个__init__.py这个文件，这个文件中可以包含包中的主要内容

# __pycache__：模块的缓存文件
# py代码执行前，需要被解析器转化为机器码，然后再执行

# import hello
from hello import a,b



#<module 'hello' (namespace)>
# print(hello)
# hello.test()

print(a.a,b.b)