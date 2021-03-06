# 多态是基于继承，通过子类重写父类的方法，
# 达到不同的子类对象调用相同的父类方法，得到不同的结果。
# 提高代码的灵活度
class PoliceDog(object):
    def attact_enemy(self):
        print('警犬正在攻击坏人')


class BlindDog(object):
    def lead_road(self):
        print('导盲犬在领路')

class DrugDog(object):
    def search_dog(self):
        print('缉毒犬在搜毒 ')


class Person(object):
    def __init__(self, name):
        self.name = name

    def work_with_pd(self):
        self.dog.attact_enemy()

    def work_with_bd(self):
        self.dog.lead_road()
    def work_with_dd(self):
        self.dog.search_dog()

p = Person('张三')
pd = PoliceDog()
p.dog = pd
p.work_with_pd()

bd = BlindDog()
p.dog = bd
p.work_with_bd()


dd =DrugDog()
p.dog =dd
p.work_with_dd()
