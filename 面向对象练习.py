# 房子(House) 有 户型、总面积、剩余面积和家具名称列表 属性
# 新房子没有任何的家具
# 将家具的名称 追加到家具名称列表中
# 判断 家具的面积是否 超过剩余面积，如果超过，提示不能添加这件家具。
class House(object):
    def __init__(self, house_type, total_area, fru_list=None):
        if fru_list is None:  # 如果这个值是None
            fru_list = []  # 将fru_list设置为空列表
        self.house_type = house_type
        self.total_area = total_area
        self.free_area = total_area * 0.6
        self.fru_list = fru_list
        print(self.fru_list)

    def add_fru(self, x):
        if self.free_area < x.area:
            print('剩余面积不足')
        else:
            self.fru_list.append(x.name)
            self.free_area -= x.area

    def __str__(self):
        return f'户型={self.house_type},总面积={self.total_area},剩余面积={self.free_area},家具列表 = {self.fru_list}'


class Furniture(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area


# 创建房间对象的时候，传入户型和总面积
house = House('两室一厅', 56)

# 家具(Furniture)有 名字 和占地面积属性，其中
# 席梦思(bed)占地4 平米
# 衣柜(chest) 占地2平米
# 餐桌(table)占地1.5平米
# 将以上三件家具添加到房子中
# 打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表


bed = Furniture('席梦思', 4)
chest = Furniture('衣柜', 2)
table = Furniture('餐桌', 1.5)

house.add_fru(bed)
house.add_fru(chest)
house.add_fru(table)
print(house)
