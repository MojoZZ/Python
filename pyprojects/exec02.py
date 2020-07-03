'''
2.输入一句英文（不含标点），统计其中每个单词出现的次数
程序运行结果如下：
请输入一句英文：I like python I like java
统计结果如下：
单词I出现2次
单词like出现2次
单词pyton出现1次
单词java出现1次
'''
# 输入
sentence = input("请输入一句英文：")
# 分割
s_list = sentence.split()
# 去重重复的
s_set = set(s_list)
# 遍历并统计次数
for w in s_set:
    print("单词", w, "出现了", s_list.count(w), "次")


