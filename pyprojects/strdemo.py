# 字符串：不可变序列，一些序列的操作都支持
s = "hello"
# print(s[0])

# sl = list(s)
# print(sl)

# print(s.startswith("h"))
# print(s.endswith("o"))
# print(s.lower())
# print(s.upper())

# 去除空格
s = " hello world "
# print(s.lstrip())
# print(s.rstrip())
# print(s.strip())

# 字符串分割
s = "h l l o 0"
# 不加参数默认是空格
print(s.split())
s = "h,l,l,o,1,20,30"
# print(s.split(","))
print(s.split(sep=","))

# 字符串合并
print("+".join("1234"))
print("+".join(["1","2","3","4"]))

