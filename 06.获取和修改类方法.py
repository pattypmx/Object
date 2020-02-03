class Person(object):
    # 私有属性
    __country = "中国"

    # 获取类属性
    # 类方法，用classmethod修饰器来进行修饰
    # cls==类名
    @classmethod
    def get_country(cls):
        return cls.__country

    # 修改类属性
    @classmethod
    def set_country(cls, country_name):
        cls.__country = country_name

print(Person.get_country())
# 01.修改属性:类名.类方法
Person.set_country("中华")
# 获取修改后的属性
print(Person.get_country())

# 02 对象.类方法
xioaming = Person()
xioaming.set_country("China")
print(xioaming.get_country())