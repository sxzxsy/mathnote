# 学生信息录入系统

# 创建一个类，要求记录学生的姓名，年龄，地址
print("-----这是一个学生信息录入系统-----")

for i in range(1,11):
    print(f"当前录入第{i}位学生信息,总共录入10位学生")

# 创建一个类，要求记录学生的姓名，年龄，地址
    class Stu_message:
        # 定义构造方法__init__来自动接收成员变量
        def __init__(self,name,age,dizhi):
            self.name = name
            self.age =age
            self.dizhi = dizhi

# 创建对象

    stu = Stu_message(input("请输入学生姓名："),int(input("请输入学生的年龄：")),
                  input("请输入学习的地址："))

    print(f"学生{i}信息录入完成，信息是：学生姓名{stu.name},年龄{stu.age},地址{stu.dizhi}")
