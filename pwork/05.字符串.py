##字符串
# 在Python中，字符串需要引号引起来，可以是单引号也可以是双引号，但是不要混用'hello"
# 如果没有引号，则表示引用了一个变量
s = "hello"
s = 'world'
print(type(s))

#相同的引号之间不可以嵌套
s = "子曰：'乐不思蜀'"


#长字符串 单引号和双引号不能跨行使用
s = '锄禾日当午，\
汗滴禾下土，\
谁知盘中餐，\
粒粒皆辛苦。'

s = '锄禾日当午，\n汗滴禾下土，\n谁知盘中餐，\n粒粒皆辛苦。'

#使用三重引号来表示一个长字符串 ''' """
#可以换行，并且保留字符串中的格式
s = '''锄禾日当午，
汗滴禾下土，
谁知盘中餐，
粒粒皆辛苦。'''


#转义字符 可以表示一些特殊的内容
# \'	\"	\t	\n 	\\
# \uxxxx 表示Unicode编码
s = "子曰：\"学而识之\""

s = '\u16A1'	#网上可以找到Unicode的编码对照表
#print(s)




##格式化字符串
str = 'hello'
#print('str='+str)	#这种写法在Python中不常见

#字符串之间可以进行加法运算，会自动将相加的字符串进行拼接
#字符串不能和其他的类型进行加法运算
# str = 'abc' + 'haha'
#str = 123
#print('str = ', str)


#在创建字符串时，可以在字符串中指定占位符
b = 'Hello %s'%'Mojo'
b = 'Hello %s 你好 %s'%('Mojo','Mojo')

#字符最小为3个，不够空格填充
b = 'Hello%3s'%'aa'
#字符串长度限制为3-5之间
b = 'Hello %3.5s'%'aavvvvdfdfd'

b = 'Hello %3s'%123.5

#%f表示浮点数
b = 'Hello %.2f'%123.534

#%d表示整数
b = 'Hello %d'%123.55
#print(b)


a = 'hello'
print('a = %s'%a)


#格式化字符串，可以通过在字符串前加一个f来创建一个格式化字符串
c = f'hello'
#在格式化字符串中可以直接嵌入变量
c = f'hello {a} {b}'
#print(c)

#print(f'a={a}')



#复制字符串（将字符串和数字相乘）
a = 'abc'
a = a * 2
print(a)
