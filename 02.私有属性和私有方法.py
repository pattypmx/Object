class Master(object):
    def __init__(self):
        self.name = "师傅教的"
        # 以__开头，表示此属性为私有属性
        # 私有属性只能当前类使用
        self.__money = 1000

    def make_cake(self):
        print("我做的蛋糕是%s" % self.name)
        print("制作费用是：%d" %self.__money)
        # 私有属性只能在本类内部使用
        print(student1.__money)

    # 私有方法不可以继承
    # def __make_cake(self):
    #     print("我做的蛋糕是%s" % self.name)
    #     print("制作费用是：%d" %self.__money)
    #     # 私有属性只能在本类内部使用
    #     print(student1.__money)

class Student(Master):
    pass

student1 = Student()
# 私有方法不可继承，找不到__make_cake
# student1.__make_cake
student1.make_cake()
print(student1.name)
# 私有属性不可以通过对象访问
# 私有属性不可以继承  找不到__money
# print(student1.__)
