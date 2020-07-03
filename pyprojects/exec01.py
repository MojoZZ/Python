'''
1. 猜数字游戏,程序生成一个随机数，然后让用户猜
   如果用户猜的数字等于随机数，输出 “你真聪明”
   如果猜的数字小于随机数，输出“猜小了”
   如果猜的数字大于随机数，输出“猜大了”
提供7次机会给用户猜，每猜错一次，提示用户还剩几次机会
如果机会用完了，提示游戏结束，正确的数字是xx
生成随机数方法：import random
random_number = random.randint(1,100)
'''

# 引入模块
import random as rd

# 生成一个1-100之间的随机整数
rd_num = rd.randint(1, 100)
# 累积猜数的次数
guest_num = 7
print("*"*30, "欢迎来到猜数游戏", "*"*30)
print("*"*26, "请猜测一个1-100之间的整数", "*"*26)

# 判断是否还有机会
while guest_num >= 0:
    # 机会为0时，游戏结束
    if guest_num == 0:
        print("游戏结束，正确的数字是", rd_num)
        break

    num = int(input("请输入您猜测的数字："))
    # 判断是否与随机数相等
    if num != rd_num:
        # 次数减1
        guest_num -= 1
        if num > rd_num:
            print("猜大了，您还有", guest_num, "次机会")
        else:
            print("猜小了，您还有", guest_num, "次机会")
    else:
        print("恭喜您，猜对了")
        break

