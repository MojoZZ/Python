# 序列：Python中最基本的一种数据结构，包含可变序列和不可变序列
##   列表：是Python中的一个对象，是一个可变的对象、可变序列，存储的是多个数据，是有序的
##	 之前的字符串（字符串也是一个序列，是不可变的），数值都是不可变的对象，存储的时单一的数据
	# 可变序列：元素可以改变
	# 	列表
	# 不可变序列：元素不能改变
	# 	字符串（str）
	# 	元祖（tuple）

# 列表：是Python中的一个对象，是一个可变的对象、可变序列，
# 存储的是多个数据，是有序的	
# 列表存储数据的性能很好，但是查询数据的性能很差
# 通过[]来创建列表
# 创建了一个空列表
my_list = []
# <class 'list'>
print(my_list, type(my_list))




s = 'hello'
# 字符串序列不允许修改元素
# s[0] = 'ab'
# 可以将字符串序列转化为一个list序列
s_sq = list(s)
s_sq[0] = 'Mojo'
print(s_sq)


# 列表中存储的数据成为元素，一个列表中可以存储多个元素
# 也可以在创建列表时来指定列表中的元素
# len()函数可以获取列表的长度
my_list = [10,20,30,40,50]
print(my_list, len(my_list))

# 可以放任意类型，但是一般情况下都放相同的数据类型
my_list = [10,20,30,True,'hello',None]
print(my_list)


## 列表的通用操作
# 元素的顺序按照插入的顺序排列
# 可以通过索引获取列表中的元素，从0开始
my_list = [10,20,30,40,50,10,70,10]

# 获取某个索引位的元素
print(my_list[1])
# 索引位负数时，表示的方向为从右向左
print(my_list[-2])

# in 和 not in
#False
print('1000在不在列表中：',1000 in my_list)
#True
print('1000在不在列表中：',1000 not in my_list)

# max 和 min
print(max(my_list), min(my_list))

# index 和 count
# 获取元素第一次出现的索引
print('10在my_list中的索引为：', my_list.index(10))
# 从哪个位置开始查找
print('10在my_list中的索引为：', my_list.index(10,2))
# 从开始位置到结束位置-1查找
print('10在my_list中的索引为：', my_list.index(10,0,5))
print('10出现的次数', my_list.count(10))

# 对列表的更新操作
# 重新给某个索引位置上的元素赋值
my_list[3] = 100
print(my_list)
# 通过切片赋值 必须需传递序列
my_list[0:2] = [20,10]
# 索引位为0的位置插入元素
my_list[0:0] = [666]
print('切片赋值后：', my_list)
# 删除某个元素
del my_list[4]
# 也可以通过切片和步长来删除列表中的元素，用法都一样
# del my_list[0:2]
print('删除第五个元素后：', my_list)
# 插入新元素
# my_list.insert(len(my_list), 60)
# print('插入新元素后：',my_list)
# 在元素的末尾添加，也可以直接使用append
my_list.append(60)
print('插入新元素后：',my_list)
# 在末尾一次性追加一个序列
my_list.extend([101,102,103])
print('插入一个新序列之后：',my_list)

my_list.insert(2,200)
print('再次插入新元素后：', my_list)

# 移除列表中的元素,并返回该元素的值
print('移除元素：', my_list.pop(0), my_list)
# 移除列表中某个值的第一个匹配项
my_list.remove(20)
print('移除元素：', my_list)
my_list.reverse()
print('反转列表：', my_list)
my_list.sort()#改变了列表的值
#降序排列
# my_list.sort(reverse=True)
print('序列排序：', my_list)
# sorted 不改变原来的列表的值
new_list = sorted(my_list)

my_copy_list = my_list.copy()
print('复制序列：', my_copy_list)
my_copy_list.clear()
print('清空列表：', my_copy_list)




print('-' * 60)
## 列表的运算
list1 = [1,2,3]
list2 = [4,5,6]
my_list = list1 + list2
# 相加 [1, 2, 3, 4, 5, 6]
print('list1 + list2 : ', my_list)
# 相乘表示复制[1, 2, 3, 1, 2, 3, 1, 2, 3]
my_list = list1 * 3
print('list1 * 3 : ', my_list)



print('-' * 60)
## 列表的切片：从现有列表中获取一个字列表
my_list2 = [10,20,30,40,50]

# 返回从开始位置到结束位置-1的所有的元素的一个新的列表
# 截取时索引超出范围，默认按照列表的索引位置来
# 不会影响原来的列表
list1 = my_list2[2:4]
# [30, 40]
print(list1, type(list1))

# 省略开始位置，则会从第一个元素开始截取
# 省略结束位置，则会一直截取到最后
# 都省略，则是原来列表的一个副本
list1 = my_list2[2:]
#list1 = my_list2[:4]
print(list1)

# 步长 列表[start:end:step]
# 每次截取元素的间隔，默认为1，不能是0，但可以是负数
# [20, 40]
list1 = my_list2[1:4:2]
print('步长测试：',list1)
list1 = my_list2[::3]
print('步长测试：',list1)
# [50, 40, 30, 20, 10] 步长为负数，则方向从右向左
list1 = my_list2[::-1]
print('步长负数测试：',list1)



print('-' * 60)
## 遍历元素
# 使用for循环来进行遍历
for x in my_list2 : 
	print(x)



print('-' * 60)
# range()可以用来生成一个自然数的序列
# 参数：其实位置（可以省略，默认为0），结束位置，步长（可以省略，默认为1）
# 可以和for配合使用
# 练习，将之前的while练习改为for循环
arr = range(5)
arr = range(0,10,2)
arr = range(10,0,-1)
print(list(arr))

for i in range(10) :
	print(i)


for s in 'hello' :
	print(s)



