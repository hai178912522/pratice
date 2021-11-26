# 定义一个类属性，记录通过这个类创建了多少个对象。
class Person(object):
    __count = 0

    def __new__(cls, *args, **kwargs):
        cls.__count += 1
        # 申请了内存，创建一个对象，并设置它的类型是Person
        return object.__new__(cls)

    def __init__(self, name, age):
        # Person.count += 1
        self.name = name
        self.age = age


# 每次创建对象都会调用__new__ 和__init__方法
# 调用__new__方法，用来申请内存
# 如果不重写__new__方法，他会自动找object的 __new__
# object的__new__方法，默认实现是申请了一段内存，创建一个对象
p1 = Person('张三', 18)
p2 = Person('李四', 19)
p3 = Person('Jack', 20)
print(Person.__count)

# p4 = object.__new__(Person)
# p4.__init__('tony', 23)
#
# print(p4)
