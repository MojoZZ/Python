# 循环语句 while和for
# while 条件表达式 :
# 	代码块
# else :


# i = 0
# while i < 5 :
# 	print('i=', i)
# 	i += 1
# else :
# 	# 在条件表达式为False时执行
# 	print('结束循环')


#循环的嵌套
# i = 0
# while i < 5 :
# 	j = 0
# 	while j < 5 :
# 		print('*', end='')
# 		j += 1
# 	print()
# 	i += 1



# i = 0
# while i < 5 :
# 	j = 0
# 	while j < i + 1 :
# 		print('*', end='')
# 		j += 1
# 	print()
# 	i += 1


#break 可以用来立刻退出当前的循环（包括else）
# i = 0
# while i < 5 :
# 	if i == 3 :
# 		break
# 	print(i)
# 	i += 1
# else :
# 	print('循环结束')



#continue 可以跳过当次循环
# i = 0
# while i < 5 :
	
# 	i += 1

# 	if i == 3 :
# 		continue

# 	print(i)
# else :
# 	print('循环结束')


#pass是用来在判断和循环语句中占位的
#当循环体或者if代码块中没有写任何代码运行会报错，可以加上pass
i = 0
if i < 5 :
	pass