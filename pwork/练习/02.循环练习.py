## 循环语句
    # 练习1：
    #     求100以内所有的奇数之和

    # 练习2：
    #     求100以内所有7的倍数之和，以及个数

    # 练习3： 
    #     水仙花数是指一个 n 位数（n≥3 ），它的每个位上的数字的 n 次幂之和等于它本身（例如：1**3 + 5**3 + 3**3 = 153）。
    #     求1000以内所有的水仙花数

    # 练习4：    
    #     获取用户输入的任意数，判断其是否是质数。质数是只能被1和它自身整除的数，1不是质数也不是合数。

    # 循环嵌套
    # 练习1：
    #     打印99乘法表
    #     1*1=1
    #     1*2=2 2*2=4
    #     1*3=3 2*3=6 3*3=9
    #     ...                 9*9=81

    # 练习2：
    #     求100以内所有的质数


# 求100以内所有的奇数之和
# i = 0
# num_sum = 0
# while i < 100 :
# 	if i % 2 != 0 :
# 		num_sum += i
# 	i += 1
# print('0-100之间所有的奇数和为：', num_sum)

#方法二
# i = 1
# num_sum = 0
# while i < 100 :
# 	num_sum += i
# 	i += 2
# print('0-100之间所有的奇数和为：', num_sum)


#求100以内所有7的倍数之和，以及个数
# i = 0
# n_sum = 0
# n_num = 0
# while i < 100 :
# 	if i % 7 == 0 :
# 		n_sum += i
# 		n_num += 1
# 	i += 1
# print('100以内共有', n_num, '个7的倍数，它们之和为：', n_sum)


# i = 100
# while i < 1000 :

# 	h = i // 100 #百位

# 	d = i // 10 % 10	#十位
	
# 	u = i % 10	#个位

# 	if h**3 + d**3 + u**3 == i :
# 		print(i)

# 	i += 1



#质数
# num = int(input('请输入一个任意大于1的数值：'))

# i = 2
# flag = True
# while i < num :
# 	if num % i == 0 :
# 		flag = False
# 		break
# 	i += 1

# if flag:
# 	print('是质数')
# else :
# 	print('不是质数')


#乘法表
# i = 1
# while i < 10 :
#     j = 1
#     while j <= i :
#         print(j,'*',i,'=',j*i,end=' ')
#         j += 1
#     i += 1
#     print()


#求100以内所有的质数
# 36的因数
#   2 18
#   3 12
#   4 9
#   6 6
#   因数一般都是成对出现，到某个位置后就不会出现因数了
#   所以可以缩小范围，这样可以优化提高程序的执行效率
#   一般到该数的开根号就可以 36 ** 0.5
#
#通过模块可以对Python进行扩展
#可以引入time模块，来统计程序执行的时间
from time import *

#time()获取当前的时间，返回的时秒
begin = time()

i = 2
while i <= 100000 :
    flag = True

    j = 2
    #缩小范围
    while j <= i ** 0.5 :
        if i % j == 0 :
            flag = False
            break
        j += 1

    if flag :
        pass
        # print(i)
        
    i += 1

end = time()

diff = end - begin;
print(diff)

#10000个数
# 15.019457340240479
#加上break 1.4913740158081055
#缩小范围，改进算法 0.05598878860473633

#100000个数
#都改进：1.663550853729248

#用for循环之后速度又提升了
