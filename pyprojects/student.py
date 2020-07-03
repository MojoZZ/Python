# 定义类 默认继承object
class Student(object):
    '''
        类的初始化方法
        property装饰器，用来将一个get方法转换为对象的属性
        方法名和属性名要一样
        在使用了装饰器后，若对象的属性只有get没有set，则不允许修改属性的值
    '''
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @name.setter
    def age(self, age):
        self._age = age

    def introduce(self):
        print("我的名字：", self._name, "，年龄是：", self._age)

    def study(self, course):
        print(self._name, "正在学习", course)


class LittleStudent(Student):
    def play(self, game):
        print(self._name, "正在玩", game)


s1 = Student("mojo", 18)
# 调用了get方法
# s1.name = "zooey"
s1.introduce()
s1.study("Python")

s2 = LittleStudent("mm", 16)
s2.introduce()
s2.play("三国杀")

