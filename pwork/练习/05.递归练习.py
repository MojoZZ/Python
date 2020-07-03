# 创建一个函数，来为任意数字做幂运算
# 10 ** 5 = 10 * 10 ** 4
# 10 ** 4 = 10 * 10 ** 3
# ...
# 10 ** 1 = 10
def my_fn(num, i) :
	'''
		为任意数字做幂运算
		参数：
			num-要做幂运算的数字
			i-要做幂运算的次数
	'''
	# 基线条件 求1次幂
	if i == 1 :
		return num

	return num * my_fn(num, i - 1)


print(my_fn(8, 5))



# 创建一个函数，来检查一个任意的字符串是否是回文字符串。如abcba
# abcdefgfedcba
# bcdefgfedcb
# cdefgfedc
# defgfed
# ......
# g

def my_fn(s) :

	# 基线条件
	# 若检查的字符到最后长度小于2，则字符串一定是回文
	if len(s) < 2 :
		return True
	# 若第一个字符和最后一个字符不相等，则肯定不是回文
	elif s[0] != s[-1] :
		return False

	# 递归
	return my_fn(s[1:-1])



s = 'abcdefgfedcba'
print(my_fn(s))