import datetime


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 1000  # 以两个下划线开始的变量是私有变量

    def test(self):
        self.__money += 10  # 在这里可以访问私有属性

    def get_money(self):
        print(f'{datetime.datetime.now()}查询了余额')
        return self.__money

    def set_money(self, qian):
        if type(qian) != int:
            print('设置的余额不合法')
            return
        print('修改余额了')
        self.__money = qian


p = Person('zhangsan', 18)
p.test()
print(p.name, p.age)  # 可以直接获取到
# print(p.__money) # 不可以直接获取到私有变量
# 获取私有变量的方式：
# 1. 使用 对象._类名__私有变量名 获取
# print(p._Person__money)

# 2. 定义get和set方法来获取
print(p.get_money())
p.set_money("100")
print(p.get_money())
# 3. 使用property来获取()
