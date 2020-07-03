# 字典
# 定义
my_dict = {}
# <class 'dict'>
# print(my_dict, type(my_dict))

my_dict = {
    'name':'Mojo',
	'age':18,
	'gender':'男'
}
# 访问
# print(my_dict['name'])

# 新增 key不存在会新增，存在则更新值
my_dict['addr'] = "江苏南京"
# print(my_dict)
my_dict['addr'] = "江苏南京市"
# print(my_dict)

# 删除
# del my_dict['addr']
# del my_dict
# my_dict.pop("addr")
# print(my_dict)
# my_dict.popitem()
# print(my_dict)

# 迭代
# for k in my_dict.keys() :
# 	print('k-',k,',v-',my_dict[k])

# for v in my_dict.values() :
# 	print(v)

# for item in my_dict.items() :
# 	print(item[0],item[1])

# for k,v in my_dict.items() :
# 	print(k, '=', v)