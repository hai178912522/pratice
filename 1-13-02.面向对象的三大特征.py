# 面对对象编程有三大特性：封装、继承和多态
# 封装：函数是对语句的封装;类是对函数和变量的封装
# 继承：类和类之间可以认为手动的建立父子关系，父类的属性和方法，子类可以使用。
# 多态：是一种技巧，提供代码的灵活度


# 一个一个的语句
def foo():
    print('我是foo')
def test(name,age):
    print(f"姓名：{name},年龄：{age}")
    a = 23
    b = 2
    a += 3
    foo()
    # print('hello')
    # print('good')
    # print(a)
    return a + b


x = test('zhangsan',18)
print(x)

# class Person(object):
#     type = '人类'
#     def __init__(self):
#         pass
#     def run(self):
#         pass
