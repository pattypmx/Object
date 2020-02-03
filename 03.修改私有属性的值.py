
class Student(object):
    def __init__(self):
        self.name = "李同学"
        self.__age = 50

    # get_xxx()方法和set_xxx()方法来获取和修改私有属性值。
    # 间接获取私有属性
    def get_age(self):
        return self.__age

    # 间接修改私有属性
    def set_age(self, new_age):
        self.__age = new_age

student1 = Student()
# 使用对象调用私有属性
print(student1.get_age())
# 使用对象设置私有属性的值
student1.set_age(55)
# 打印修改后的值
print(student1.get_age())