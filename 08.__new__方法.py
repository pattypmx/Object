class Person(object):
    # 监听python使用其类创建对象 并返回对象给__init__
    def __new__(cls, *args, **kwargs):
        print("new")
        return object.__new__(cls)  # 一定要写return，不然返回的就是none，不会往下面走

    # 构造方法，监听python使用其类创建对象完成，给这个对象设置属性
    def __init__(self):
        print("init")
        self.name = "xiaoming"

    # 监听对象属性信息变化
    def __str__(self):
        return "姓名：%s" % self.name

    # 监听对象销毁
    def __del__(self):
        print("删除成功")

xiaoming1 = Person()
print(xiaoming1)
