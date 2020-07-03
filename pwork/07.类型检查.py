#通过类型检查，可以检查数值（变量）的类型
#type() 函数，用来检查值得类型

a = 123
b = '123'

print(type(a))	#<class 'int'>
print(type(b))	#<class 'str'>

print(type(0.152))	#<class 'float'>

print(type(True))	#<class 'bool'>

print(type(None))	#<class 'NoneType'>



#类型转换 将一个类型的对象转换为其他对象
#类型转换不是改变对象本身的类型，而是根据当前对象的值创建一个新对象
#int() float() str() bool() 函数

#int()规则：
#	布尔值：True-1	False-0
#	浮点数：取整
#	字符串：合法的整数字符串
#	None：不支持
a = True
a = int(a)
print('a =', a)

a = '123'
a = int(a)
print('a =', a)

a = 123.456
a = int(a)
print('a =', a)

a = None;
#a = int(a)
#print('a =', a)

#float()规则基本和int()一致
b = 209
b = float(b)
print('b =', b);
print('b的类型', type(b))


#str()
s = 123
s = str(123)
#print('s =', s)
#print('s的类型', type(s))


#bool()	任何对象都可以转为布尔值
#所有表示空性的对象都会转为False，其余的转为True
#空性的有如：0  None 	''
n = ''
n = bool(n)
print('n=', n)