# 集合 Set
#	- 与列表相似
#	- 集合中存储的对象是无序的（和插入的顺序无关）
#	- 集合中只能存储不可变对象
#	- 集合中不能出现重复的元素

# 创建
# 使用{}创建
# 使用set()函数创建

s = {10,2,3,4,1,1,1}
# {1, 2, 3, 4, 10} <class 'set'>
print(s, type(s))

# 创建一个空集合
s = set()
# {1, 2, 3, 34, 5, 7, 8}
s = set([1,2,34,5,1,2,3,7,8])
# {'l', 'e', 'o', 'h'}
s = set('hello')
# 将字典转为set，只取key，{'a', 'b', 'c'}
s = set({'a':1,'b':2,'c':3})
print(s)


s = {'a', 'b', 'c', 1, 3, 1}
# print('c' in s)	# True
# print(len(s)) # 5

# add()
s.add('hello')
# print(s)

# update
s1 = set('zooey')
s.update(s1)
s.update([10,20])
s.update((30,10))
s.update({10:'a',20:'b',666:'hello'})
print(s)

# 删除，随机的
s.pop()
print(s)

# 不存在会发生错误
s.remove(10)
# 不存在不会发生错误
s.discard(20)
s.discard(20000)
# s.clear()
print(s)



print('集合运算','-'*60)
# 集合的计算
s1 = {1,2,3,4,5,6}
s2 = {1,10,3,45,5,61}
s3 = {10,1,3}

# 交集 {1, 3, 5}
z = s1 & s2
print('s1 & s2:', z)
# 并集 {1, 2, 3, 4, 5, 6, 10, 45, 61}
z = s1 | s2
print('s1 | s2:', z)
# 差集 {2, 4, 6}
z = s1 - s2
print('s1 - s2:', z)
# 异或集 {2, 4, 6, 10, 45, 61}
z = s1 ^ s2
print('s1 ^ s2:', z)
# 检查一个集合是否是另一个集合的子集 
z = s1 <= s2 # False
z = s3 <= s2 # True
print('s1 <= s2:', z)
print({1,2,3} <= {1,2,3}) # True
print({1,2,3} < {1,2,3}) # False 真子集
# >和>=同上用法


# difference:返回多个集合的差集
# 元素包含在集合 s1 ，但不在集合 s2
# {2, 4, 6}
print(s1.difference(s2))
# {2, 4, 6}
print('s1-s2:',s1-s2)
# 元素包含在集合 s2 ，但不在集合 s1
# {10, 61, 45}
print(s2.difference(s1))
# intersection:返回集合的交集
# {1, 3, 5}
print(s1.intersection(s2))
# {1, 3}
print(s1.intersection(s2,s3))
# 返回两个集合中不重复的元素集合
# {2, 4, 6, 10, 45, 61}
print(s1.symmetric_difference(s2))
print(s1 ^ s2)


for x in s1:
	print(x)


