# 1.获取用户输入的整数，显示该数是基数还是偶数
# 2.检查一个年份是否是闰年
#	如果一个年份可以被4整除不能被100整除，或者可以被400整除，这个年份就是闰年
# 3.我家的狗5岁了，5岁的狗相当于多大年龄的人呢？
#         其实非常简单，狗的前两年每一年相当于人类的10.5岁，然后每增加一年就增加四岁。
#         那么5岁的狗相等于人类的年龄就应该是10.5+10.5+4+4+4 = 33岁
# 4.
#         从键盘输入小明的期末成绩:
#             当成绩为100时，'奖励一辆BMW'
#             当成绩为[80-99]时，'奖励一台iphone'
#             当成绩为[60-79]时，'奖励一本参考书'
#             其他时，什么奖励也没有

# 5.
#         大家都知道，男大当婚，女大当嫁。那么女方家长要嫁女儿，当然要提出一定的条件：
#             高：180cm以上; 富:1000万以上; 帅:500以上;
#             如果这三个条件同时满足，则:'我一定要嫁给他'
#             如果三个条件有为真的情况，则:'嫁吧，比上不足，比下有余。'
#             如果三个条件都不满足，则:'不嫁！'



# num = int(input('请输入一个整数：'))
# if num % 2 == 0 :
# 	print('该数为偶数')
# else :
# 	print('概数为奇数')



# year = int(input('请输入你现在的年份：'))

# leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
# if leap_year :
# 	print('今年是闰年')
# else :
# 	print('今年不是闰年')


# dog_age = float(input('你家的狗狗几岁了：'))
# if dog_age < 0 :
# 	print('你不要骗我哦！')
# else :
# 	if dog_age <= 2 :
# 		pe_age = dog_age * 10.5
# 	else :
# 		pe_age = 2 * 10.5 + (dog_age - 2) * 4
# 	print(f'哇塞，它相当于人类 {pe_age} 岁了呢！')


# score = float(input('小明，年级期末成绩考了多少分哈(0-100)：'))
# if 0 <= score <= 100 :
# 	if score == 100 :
# 		print('考得不错，奖励你一辆BMW')
# 	elif score >= 80 :
# 		print('考得还可以，奖励你一台iPhone')
# 	elif score >= 60 :
# 		print('下次好好努力，奖励一本参考书')
# 	else :
# 		print('小明你活在大家的心中！')
# else :
# 	print('请输入合理的成绩范围（0-100）')


height = float(input('身高多少（CM）：'))
year_salary = float(input('年薪呢（单位：W）'))
handsome_score = float(input('觉得有多帅哈：'))

if height >= 180 and year_salary >= 1000 and handsome_score >= 500 :
	print('我一定要嫁给你')
elif height >= 180 or year_salary >= 1000 or handsome_score >= 500 :
	print('嫁吧，比上不足，比下有余')
else :
	print('不嫁！')