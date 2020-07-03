# 求100以内所有的奇数之和
# n_sum = 0
# for i in range(100) :
# 	if i % 2 != 0 :
# 		n_sum += i
# print('0-100之间所有的奇数和为：', n_sum)

# 方法二
# n_sum = 0
# for i in range(1,100,2) :
# 	n_sum += i
# print('0-100之间所有的奇数和为：', n_sum)


#求100以内所有7的倍数之和，以及个数
# n_sum = 0
# n_num = 0
# for i in range(7,100,7) :
# 	n_sum += i
# 	n_num += 1
# print('100以内共有', n_num, '个7的倍数，它们之和为：', n_sum)


#乘法表
# i = 1
# while i < 10 :
#     j = 1
#     while j <= i :
#         print(j,'*',i,'=',j*i,end=' ')
#         j += 1
#     i += 1
#     print()
# for i in range(1,10) :
# 	for j in range(1,i+1) :
# 		print(j,'*',i,'=',j*i,end=' ')
# 	print()



#求100以内所有的质数
# i = 2
# while i <= 100000 :
#     flag = True

#     j = 2
#     #缩小范围
#     while j <= i ** 0.5 :
#         if i % j == 0 :
#             flag = False
#             break
#         j += 1

#     if flag :
#         pass
#         # print(i)
        
#     i += 1


from time import *

begin = time()

for i in range(2,100001) :
	flag = True
	j =2
	while j <= i ** 0.5 :
		if i % j == 0 :
			flag = False
			break
		j += 1

	if flag :
		pass

		# print(i)


end = time()

diff = end - begin;
print(diff)



