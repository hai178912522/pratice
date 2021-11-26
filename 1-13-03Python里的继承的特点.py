class A(object):
    def demo_a(self):
        print('我是A类里的方法demo_a')
    def foo(self):
        print('我是A类里的foo方法')

class B(object):
    def demo_b(self):
        print('我是B类里的方法demo_b')
    def foo(self):
        print('我是B类里的foo方法')

#python里允许多继承
class C(A,B):
    pass
c= C()
c.demo_a()
c.demo_b()
# 如果两个不同的父类有同名的方法，class C(A,B):会先找A类，因为A在前
c.foo()