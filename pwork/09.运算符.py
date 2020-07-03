##运算符
#	算数运算符
#	赋值运算符
#	比较运算符（关系运算符）
#	逻辑运算符
#	条件运算符（三元运算符）
#   位运算


a = 10 + 5
a = 10 - 5

a = 'hello' + 'world'
a = 4 + True

a = a -2
print('a =', a)


#除法运算，总是得到一个浮点数
b = 10 / 2
#	// 整除运算符，只保留计算后的整数位
b = 10 // 3
#	** 幂次运算 
b = 2 ** 16
#	** 0.5	求某数的平方根
b = 16 ** 0.5
print('b =', b)



#赋值运算符
c = 10
c += 5

c **= 5
c //= 5
c %= 5
print('c =', c)


#关系运算符	> 	<	>=	<=	==	!=
#比较两个值之间的关系，总会返回一个布尔值
n1 = 10
n2 = 20
result = n1 != n2

#对字符串进行比较时，实际上比较的是字符串的Unicode的编码
#比较Unicode编码时，是逐位比较的，一位一位的比较，若已经有结果了，就不会比较后面的
#利用该特性可以对字符串按照字母顺序进行排序，如姓名的排序等
#若不希望按照Unicode编码比较，则需要转为为整数进行比较
result = '2' > '1'	#True
result = '2' > '11'	#True
result = 'a' > 'b'	#False
result = 'ab' > 'b'	#False
result = 'abc' > 'ab'	#True
print('result =', result)


#	==和!= 比较的都是对象的值，而不是对象的id
#	对象的比较用：is和not
a = 1
b = True
result = 1 == True
result = a is b
result = a is not b
print('result =', result)
#都是针对中间的数字进行比较的
result = 1 < 2 < 3	#相当于 1 < 2 and 2 < 3
result = 10 < 20 > 15
print('result =', result)



##逻辑运算符
#	not
#		对于布尔值，非运算则是取反
#		对于非布尔值，则会先转换为布尔值，再运算
#		空性的有如：0  None 	''
#	and
#		与运算是找False
#		Python中的与运算是短路的，如果第一个为False，则第二个不会运算
#	or
#		或运算是找True
#		Python中的或运算是短路的，如果找到True，后面的则不会运算

a = True
a = not a

n1 = 10
n2 = 20
n3 = 30

result = 'abc' > 'bcd' and 'abc' < 'dc'
result = n1 > n2 and n2 < n3
print('result =', result)

#与运算的短路特性
False and print('会打印么？')
#或运算的短路特性
True or print('会打印么？')

#非布尔值的与或运算
#	当对非布尔值进行与或运算，Python会将其当做布尔值运算，最终返回原值
#	与运算：当第一个值为True时，返回第二个值
#			当第一个值为False时，则返回第一个值（短路，第二个不会运算）
#			总结：如果第一个是False，则返回第一个，否则返回第二个
#	或运算：
#			总结：如果第一个是True，则返回第一个，否则返回第二个

result = 0 and 1	#0
result = 1 and 0	#0
result = 1 and 2	#2
result = 0 and None	#0
print('result =', result)

result = 0 or 1	#1
result = 1 or 0	#1
result = 1 or 2	#1
result = 0 or None	#None
print('result =', result)




##条件运算符
#语法：	语句1 if 条件表达式 else 语句2

#print('你好') if True else print('Hello')

a = 30
b = 20
c = 15
#print('a的值比较大！') if a > b else print('b的值比较大')

max_num = a if a > b else b
max_num = max_num if max_num > c else c

max_num = a if a > b else (b if b > c else c)
#max_num = a if (a > b and a > c) else (b if b > c else c)
print('max_num=',max_num)



#运算符的优先级
a = 1 or 2 and 3	#1
print('a =', a)