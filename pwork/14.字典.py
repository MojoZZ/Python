# 字典：属于新的数据结构，称为映射（mapping：key-value）。也是存储对象的容器。
#		查询数据时，字典的效率很快
#	1.可以保存多个对象，每个对象都有一个唯一的名字key，该对象为value
#	2.key+value-->item


# 创建字典，使用{}来创建
dict1 = {}

# 创建子字典，并初始化值
# key-可以是任意的不可变对象(int、str、bool、tuple...)，一般使用str，字典的键不能重复
# value-可以是任意类型的对象
# dict1 = {'name':'Mojo', 'age':18, 'gender':'男'}
dict1 = {
	'name':'Mojo', 
	'age':18, 
	'gender':'男'
}
print(dict1)
print(type(dict1))


# 多种创建方式，使用dict()创建
# 这里的key默认为str类型
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
# 
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
# 这里使用的双值子序列来创建
# 双值序列，序列中只有两个值，如[1,2]、{1,2}、'ab'
# 子序列，如果序列中的元素也是序列，则成为子序列。如[(1,2),(3,5)]
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)	# True

# 字典的遍历
# keys()-返回字典的所有的key
# values()-返回字典所有的值
# items()-返回字典所有的项，双值子序列
dict1 = {
	'name':'Mojo', 
	'age':18, 
	'gender':'男'
}
# dict_keys(['name', 'age', 'gender'])
# print(dict1.keys())

# for k in dict1.keys() :
# 	print('k-',k,'v-',dict1[k])

# for v in dict1.values() :
# 	print(v)

# for item in dict1.items() :
# 	print(item[0],item[1])

for k,v in dict1.items() :
	print(k, '=', v)


print('-'*60)

# 获取字典中键值对的个数
print(len(a))
# in和not in 检查字典中是否包含指定的键
print('hello' in d)
# 通过key获取value
print(dict1['name'],dict1['age'])
# 不存在的key会报错	KeyError
# print(dict1['abc'])
# get：也会根据key来获取value的值，若不存在则返回None
print(dict1.get('hello'))
# 若获取的值不存在，则可以指定一个默认值
print(dict1.get('hello','默认值'))





print('-'*60)
# 修改字典
dict1['name'] = 'Zooey'
dict1['age'] = 28
# 若是不存在的key则是向字典中添加项
dict1['address'] = '江苏南京'
# {'name': 'Zooey', 'age': 28, 'gender': '男'}
print(dict1)

# setdefault(key[,default])
# 若key已经存在，则返回key的值，不会对字典做任何操作
# 若key不存在，则向字典中添加该项，并设置和value
v1 = dict1.setdefault('name','Mojo')
print(v1, dict1)
v1 = dict1.setdefault('abc','hello')
print(v1, dict1)


# update([other])
# 将其他字典中的key-value添加到当前字典中
d1 = {'a':1,'b':2,'c':3}
d2 = {'d':4,'e':5,'f':6,'a':10}
d1.update(d2)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
print(d1)

# 删除字典元素 key不存在时报错
del dict1['name']
# {'age': 28, 'gender': '男'}
print(dict1)
# 删除整个字典
# del dict1

# popitem() 删除最后一个item，字典为空时报错
# ('f', 6) 返回一个元祖
result = d1.popitem()
print(result, d1)

# pop(key,[default])
# 返回该key的值
result = d1.pop('b')
# 不存在的key，指定了默认值，则不会报错并返回该默认值
result = d1.pop('z','abc')
print(result, d1)

# 清空字典
d1.clear()
print(d1)



# copy()：字典的浅复制
# 复制以后的对象，和原对象是独立的，修改一个不会影响另一个
# 注意：浅复制只会简单的复制对象的内部的值，若对值也是一个可变对象，这个可变对象不会被复制
d1 = {'a':1,'b':2,'c':3}
# 这里不是复制，是引用的同一个对象，
# 若一个变量对对象进行修改，则会影响另外的变量
# d2 = d1

d2 = d1.copy()
d1['a'] = 100

# d1= {'a': 100, 'b': 2, 'c': 3} 19434224
# d2= {'a': 1, 'b': 2, 'c': 3} 19434304
print('d1=',d1,id(d1))
print('d2=',d2,id(d2))


d1 = {'a':{'name':'Mojo','age':18},'b':2,'c':3}
d2 = d1.copy()
# 此时原对象也会进行修改，内部对象的引用直接使用原来的
d2['a']['name'] = 'Zooey'

# d1= {'a': {'name': 'Zooey', 'age': 18}, 'b': 2, 'c': 3} 58231576
# d2= {'a': {'name': 'Zooey', 'age': 18}, 'b': 2, 'c': 3} 58231536
print('d1=',d1,id(d1))
print('d2=',d2,id(d2))

