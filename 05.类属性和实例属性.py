class Person():
    # 在类下面，实例属性上面的叫做：类属性
    country = "中国"

    def __init__(self, name, age):
        self.name = name
        self.age = age

xiaoming = Person("小明", 22)
# 使用类属性
# 方法1：类名.类属性名
print(Person.country)
# 方法2：对象名.类属性名
print(xiaoming.country)

# 修改实例属性名
xiaoming.name = "小红"
print(xiaoming.name)
# 修改类属性名
Person.country = "中华"
print(Person.country)


