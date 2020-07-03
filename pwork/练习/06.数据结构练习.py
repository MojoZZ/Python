#1.输入5个数,按照从大到小的顺序输出
# n1 = float(input('请输入一个数：'))
# n2 = float(input('请输入一个数：'))
# n3 = float(input('请输入一个数：'))
# n4 = float(input('请输入一个数：'))
# n5 = float(input('请输入一个数：'))

# my_list = [n1,n2,n3,n4,n5]

# # 方法一
# # my_list.sort(reverse=True)

# #方法二
# # my_list.sort()
# # my_list.reverse()

# #方法三
# my_list.sort()
# my_list = my_list[::-1]

# print(my_list)


# 2.打印10行由*组成的三角形(三角形形状随意)
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * * * 
# * * * * * * * 
# * * * * * * * * 
# * * * * * * * * * 
# * * * * * * * * * *  
# for i in range(10) :
# 	for j in range(i+1) :
# 		print('*',end=' ')
# 	print()

# * * * * * * * * * * 
# * * * * * * * * * 
# * * * * * * * * 
# * * * * * * * 
# * * * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
# for i in range(10) :
# 	for j in range(10-i) :
# 		print('*',end=' ')
# 	print()


 #          * 
 #         * * 
 #        * * * 
 #       * * * * 
 #      * * * * * 
 #     * * * * * * 
 #    * * * * * * * 
 #   * * * * * * * * 
 #  * * * * * * * * * 
 # * * * * * * * * * * 
# for i in range(10):
#     for j in range(0, 10 - i):
#         print(end=' ')
#     for k in range(10 - i, 11):
#         print("*", end=' ')

#     print()


# 3.输入0-100的整数，90-100 评分为A，80-89评分为B，70-79评分为C，60-69评分为D，0-59评分为E。
# 要求能够重复输入
# 如果输入为负数，则转化为正数
# 如果输入为小数，则转化为整数
# 如果输入大于100或者小于-100，则游戏结束
while True:
	score = float(input('请输入你的成绩：'))
	score = abs(int(score))

	if score > 100:
		input('游戏结束，按回车键结束')
		break

	if score >= 90 and score <= 100 :
		print('='*10,'您的评分为A','='*10)
	elif score >= 80 and score < 90 :
		print('='*10,'您的评分为B','='*10)
	elif score >= 70 and score < 80 :
		print('='*10,'您的评分为C','='*10)
	elif score >= 60 and score < 70 :
		print('='*10,'您的评分为D','='*10)
	else :
		print('='*10,'您的评分为E','='*10)