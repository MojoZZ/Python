# 元组：tuple 不可变序列 操作和列表基本一致，修改更新的操作不可用
# 希望数据不会改变时，使用元组；其他情况使用列表

# 创建元组，使用()创建
my_tuple = ()
# <class 'tuple'>
print(type(my_tuple))


my_tuple = (1,2,3,4,5)
# 元组不为空时，可以省略括号
my_tuple = 1,2,3,4,5
#(1, 2, 3, 4, 5)	3	(1, 2, 3)
print(my_tuple, my_tuple[2], my_tuple[0:3])

# 如果元组不为空时，里面至少要有一个逗号
my_tuple = (10)		# <class 'int'>
print(type(my_tuple))
my_tuple = (10,)	# <class 'tuple'>
print(type(my_tuple))

# 元组拼接
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
# (12, 34.56, 'abc', 'xyz')
print(tup1 + tup2)

# 删除
del tup1
# print(tup1)

# 迭代
for i in tup2 :
	print(i, end=' ')
print()

# tuple():将可迭代系列转化为元组
tup1 = tuple('hello')
# ('h', 'e', 'l', 'l', 'o')
print(tup1)

my_tuple = (10,20,30,40)
# 序列都可以解包
# 元组的解包（解构）：将元组的每一个元素都赋值给一个变量
# 变量数量不能多于或少于元组的元素个数
a,b,c,d = my_tuple
print('a=',a,'b=',b,'c=',c,'d=',d)
# 数量不确定时，可以使用*，此时的c为一个列表
# 但不能同时出现多个*变量
a,b,*c = my_tuple
print('a=',a,'b=',b,'c=',c)
a,*b,c = my_tuple
print('a=',a,'b=',b,'c=',c)
*a,b,c = my_tuple
print('a=',a,'b=',b,'c=',c)





a = 100
b = 300
print(a,b)
# 根据上面的解包特点可以交换变量的值
a , b = b , a
print(a,b)
