#
class Student:

    # init 自动定义属性
    def __init__(self,weight):
        self.weight = weight

    # 跑步
    def run(self):
        self.weight = self.weight-0.5
        print(f"跑步一次减去0.5kg，当前体重是{self.weight}")

    # 吃喝
    def eat(self):
        self.weight = self.weight+ 2
        print(f"每大吃大喝一次，体重增长2kg，当前体重{self.weight}")

    # str 重写对象属性值
    def __str__(self):
        return f"当前体重{self.weight}kg"

# 测试
if __name__ =='__main__':

# 创建对象
    Stu = Student(100)
    # 调用跑步
    Stu.run()
    # 调用大吃大喝
    Stu.eat()
    # 当前体重
    print(Stu)  #str输出
