class Calculator(object):
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def minus(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b
Calculator.add(1,4)
Calculator.minus(9,2)


class Person(object):
    type = 'human'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print(f'{self.name}' + '正在吃' + food)

    # 如果一个方法里没有用到实例对象的任何属性，可以将这个方法成static
    @staticmethod
    def demo():
        print('hello')

    @classmethod
    def test(cls):  # 如果这个函数只用到了类属性，我们可以把定义成为一个类方法。
        # 类方法有一个参数cls，也不需要手动的传参，会自动传参。
        # cls指的是类对象  cls == Person -->Ture
        print('yes')


p1 = Person('张三', 18)
# 实例对象在调用方法时，不需要给形参self传参，会自动的把实例对象传递给self
p1.eat('红烧牛肉泡面')  # 直接使用实例对象调用方法
# 对象方法还可以使用 类对象来调用。 类名.方法名()
# 这种方式，不会自动给self传参，需要手动的指定self
# Person.eat('西红柿鸡蛋盖饭')
p2 = Person('李四', 19)
Person.eat(p2, '西红柿鸡蛋盖饭')
# p2.eat()


# 静态方法:没有用到实例对象的任何属性
Person.demo()
p1.demo()

# 类方法：可以实例对象和类对象调用
p1.test()
Person.test()
