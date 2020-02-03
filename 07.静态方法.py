class Person():
    __country = "中国"

    # 实例属性
    def __init__(self,name):
        self.name = name
        self.__age = 21

    # 实例方法属性
    # 获取实例属性
    def get_name(self):
        return self.name
    # 修改实例属性
    def set_name(self, new_name):
        self.name = new_name

    # 获取实例方法的私有属性
    def get_age(self):
        return self.__age
    # 修改实例方法的私有属性
    def set_age(self, new_age):
        self.__age = new_age

    # 类方法
    # 获取私有属性类
    @classmethod
    def get_country(cls):
        return cls.__country
    # 修改私有属性类
    @classmethod
    def set_country(cls,new_country):
        cls.__country = new_country

    # 静态方法
    @staticmethod
    def hello():
        print("hello world")


"""
1.实例方法（对象方法）：
--定义格式:	def 实例方法名(self)
--调用格式:	对象名.实例方法名
--使用场景:	在方法中需要self
2.类方法：
--定义格式:	@classmethod
  def 类方法名(cls)
--调用格式:	类名.类方法名
  对象名.类方法名
--使用场景:	在方法中需要cls（类名）

3.静态方法：
--定义格式:	@staticmethod
  def 静态方法名()
--调用格式:	类名.类方法名
  对象名.类方法名
--使用场景:	在方法中不需要self，也不需要cls
"""

