# 设计两个类：
# 一个点类，属性包括x,y坐标
# 一个Rectangle类，属性上有左上角和右下角坐标
# 方法：1，计算矩形的面积；2，判断点是否在矩形内
# 实例化一个点对象，一个矩形对象，输出矩形的面积，输出点是否在矩形内
class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Rectangle(object):
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def get_area(self):
        # 面积 = 长*宽
        length = abs(self.bottom_right.x - self.top_left.x)
        width = abs(self.top_left.y - self.bottom_right.y)
        return length*width

    def is_inside(self, point):
        # if self.bottom_right.x >= point.x >= self.top_left.x and self.top_left.y >= point.y >= self.bottom_right.y:
        #     return True
        # else:
        #     return False
        return self.bottom_right.x >= point.x >= self.top_left.x and self.top_left.y >= point.y >= self.bottom_right.y


p1 = Point(4, 20)
p2= Point(30,8)
r = Rectangle(p1,p2)
print(r.get_area())

p = Point(20,30)
print(r.is_inside(p))
