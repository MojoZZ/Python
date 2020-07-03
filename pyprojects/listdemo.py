# 列表
my_list = []
# <class 'list'>
# print(my_list, type(my_list))

my_list = [10, 20, 30, 11, 19, 101, 23]
for l in my_list:
    # print(l)
    pass

print(my_list[1])
print(my_list[-1])

# 成员判断
print('10在不在：', 10 in my_list)
print('123在不在：', 123 in my_list)
print('19不在：', 19 not in my_list)



my_list.extend([16, 89])
# print(my_list)

my_list.append(33)
print(my_list)

my_list.insert(2, 28)
print(my_list)


# 列表切片
print(my_list[1:6])
print(my_list[1:6:2])
print(my_list[:6])
print(my_list[:])
print(my_list[6:-1])


print(my_list[::-1])
print(my_list[-1:-6:-2])


# 删除
my_list.pop()
print(my_list)
my_list.pop(1)
print(my_list)

my_list.remove(28)
print(my_list)

del my_list[-1]
print(my_list)
# 删除整个列表
# del my_list
# 清空
# my_list.clear()

print(len(my_list))
print(my_list.count(11))

# 排序
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)
my_list.reverse()
print(my_list)


# list函数
print(list("hello"))
print(list(range(1, 10, 1)))
print(list((1, 2, 3, 4)))


alist = [1, 2, 3, [4, 5, 6]]
print(alist[3][0])