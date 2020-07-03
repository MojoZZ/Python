#数据类型：变量值的类型
#Python数值分为三种：整数、浮点数、复数

#在Python中，所有的整数都是int类型
#整数大小没有限制，可以是无限大的整数
a = 10
b = 20
c = 9999999999999999999 ** 100

c = 123
print(type(c))
c = 123.333
print(type(c))

#如果数字的长度过大，可以使用下划线作为分隔符
c = 123_456_789_098

#print(a)
#print(b)
#print(c)

#其他进制的整数   数字打印的时候都是以十进制的形式显示的
#d = 0123 十进制不能以0开头

#二进制 以0b开头
num = 0b10
#八进制 以0o开头
num = 0o10
#十六进制 以0x开头
num = 0x10

#也可以通过运算符来对数字进行运算，并且可以保证整数运算的精确
num = -100
num = num + 3


#浮点数（小数），在Python中所有的小数都是float类型
#对浮点数进行运算时，可能会得到一个不精确的结果
num = 1.23
num = 3.55

num = 0.1 + 0.2 #0.30000000000000004

# print(num)


# print(sum((1,20)))









#1.学生成绩(0到100)评级规则如下:[90,100]为优秀,[80,90)为良好,[70,80)为一般,[60,70)为及格,[0,60)为不及格,其他情况提示输入错误
# score = input('请输入你的成绩：')
# score = int(score)
# if score >= 90 and score <= 100 :
# 	print('优秀')
# elif score >= 80 and score < 90 :
# 	print('良好')
# elif score >= 70 and score < 80 :
# 	print('一般')
# elif score >= 60 and score < 70 :
# 	print('及格')
# elif score >= 0 and score < 60 : 
# 	print('不及格')
# else :
# 	print('输入错误！')


# 2.输入三个数,求最大值
# num_1 = input('请输入数值1：')
# num_2 = input('请输入数值2：')
# num_3 = input('请输入数值3：')

# num_1 = float(num_1)
# num_2 = float(num_2)
# num_3 = float(num_3)

# max_num = num_1 if num_1 > num_2 else num_2
# max_num = max_num if max_num > num_3 else num_3
# print(f'最大值为 {max_num}')




# 3.输入两个整数，如果2个数相等则输出“这两个数相等”,否则判断两个数的乘积，如果大于30则输出“这两个数的积大于30”,否则输出“这两个数的积不大于30”
# num_1 = input('请输入整数1：')
# num_2 = input('请输入整数2：')

# num_1 = int(num_1)
# num_2 = int(num_2)

# if num_1 == num_2:
# 	print('这两个数相等')
# else:
# 	num_product = num_1 * num_2
# 	if num_product > 30:
# 		print('这两个数的积大于30')
# 	else:
# 		print('这两个数的积不大于30')



# 4.输入一个三位数，百位、十位、个位 分别存到a,b,c中,输出：“百位是a,十位是b,个位是c”
# num = input('请输入一个三位数的整数：')
# if len(num)!=3:
# 	print('请输入一个三位数的整数')
# else:
# 	num_list = list(num)
# 	print(f'百位是{num_list[0]}，十位是{num_list[1]}，个位是{num_list[2]}')



# num = int(input('请输入一个三位数的整数：'))
# if num > 99 and num < 1000:
# 	n1 = int(num / 100)
# 	n2 = int(num / 10 % 10)
# 	n3 = num % 10
# 	print(f'百位是{n1}，十位是{n2}，个位是{n3}')
# else:
# 	print('请输入一个三位数的整数')





