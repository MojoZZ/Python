# 定义函数
def say_hello():
    '''
    函数名：say_hello
    作用：输出你好
    :return:None
    '''
    print("Hello")

def say_hello1(times):
    for i in range(times):
        print("Hello")


def my_sum(a, b):
    return a+b



# 每一个python文件都有__name__的属性，1个值为__main__，另一个为文件名
# 在被导入的时候，__name__=文件名
# 在本地执行的时候，__name__=__main__
# print("__name__：", __name__)
if __name__ == "__main__":
    # 调用函数
    say_hello()
    say_hello1(2)
    print(my_sum(10,20))
