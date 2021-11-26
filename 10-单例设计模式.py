class Singleton:
    __instance = None  # 类属性

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            # 申请内存，创建一个对象，并把对象的类型设置为cls
            cls.__instance = object.__new__(cls)

        return cls.__instance

    def __init__(self, a, b):
        self.a = a
        self.b = b


# 1. 调用__new__方法申请内存
# 如果不重写__new__方法，会调用object的__new__方法
# object 的__new__方法会申请内存
# 如果重写了__new__方法，需要自己手动的申请内存
s1 = Singleton('呵呵', '嘿嘿嘿')
s2 = Singleton('哈哈', '嘻嘻嘻')
print(s1 is s2)
