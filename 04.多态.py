class Person(object):
    def __init__(self):
        self.name = "小明"
        self.age = 20
    def run(self):
        print("会跑")
        print("="*10)
# object:为使用类创建出来的对象使用额
def put(object):
    # python不关心函数（方法）中参数的类型，只要这个参数有这个属性和方法，就可以使用
    # python是弱类型，即无论传递过来的是什么，obj变量都能够指向它，这也就没有所谓的多态了（弱化了这个概念）
    print(object.name)
    print(object.age)
    object.run()

xiaoming = Person()

class Animal(object):
    def __init__(self):
        self.name = "柯基"
        self.age = 2

    def run(self):
        print("会跑")

keji = Animal()
# print(xiaoming.name)
# print(xiaoming.age)
# xiaoming.run()
put(xiaoming)
put(keji)