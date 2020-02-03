class Master(object):
    def make_cake(self):
        print("师傅配方")

class School(object):
    def make_cake(self):
        print("学校配方")

class Student(Master, School):
    # 继承并重写父类方法
    def make_cake(self):
        print("学生的配方")
    #继承且重写父类方法
    def master_make_cake(self):
        # 方法一:单继承，多继承都可用
        # Master.make_cake(self)
        # 方法二：单继承可用，多继承只会继承第一个父类
        # super(Student, self).make_cake()
        # 方法三：方法二的简写
        super().make_cake()

    def school_make_cake(self):
        # School.make_cake(self)
        # super(Student, self).make_cake()
        super().make_cake()

student1 = Student()
student1.make_cake()
student1.master_make_cake()
student1.school_make_cake()